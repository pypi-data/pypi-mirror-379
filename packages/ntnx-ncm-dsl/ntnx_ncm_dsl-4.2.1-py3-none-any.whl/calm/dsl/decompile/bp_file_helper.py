import click
import sys
import traceback
import os
from io import StringIO
import json
import ast
from Crypto.Cipher import AES

from calm.dsl.decompile.render import render_template
from calm.dsl.decompile.service import render_service_template
from calm.dsl.decompile.package import render_package_template
from calm.dsl.decompile.vm_disk_package import render_vm_disk_package_template

from calm.dsl.decompile.substrate import render_substrate_template
from calm.dsl.decompile.deployment import render_deployment_template
from calm.dsl.decompile.profile import render_profile_template
from calm.dsl.decompile.credential import render_credential_template, get_cred_files

from calm.dsl.decompile.blueprint import render_blueprint_template
from calm.dsl.decompile.metadata import render_metadata_template
from calm.dsl.decompile.variable import get_secret_variable_files
from calm.dsl.decompile.ref_dependency import update_entity_gui_dsl_name
from calm.dsl.decompile.file_handler import get_local_dir
from calm.dsl.builtins import BlueprintType, ServiceType, PackageType
from calm.dsl.builtins import DeploymentType, ProfileType, SubstrateType
from calm.dsl.builtins import get_valid_identifier
from calm.dsl.log import get_logging_handle
from calm.dsl.builtins import ConfigAttrs
from calm.dsl.decompile.config_spec import render_config_attr_template


LOG = get_logging_handle(__name__)

SECRETS_FILE_ENCRYPTION_KEY = (
    b"dslengine@calm23"  # the key must be a multiple of 16 bytes
)


def render_bp_file_template(
    cls, with_secrets=False, metadata_obj=None, contains_encrypted_secrets=False
):

    if not isinstance(cls, BlueprintType):
        raise TypeError("{} is not of type {}".format(cls, BlueprintType))

    user_attrs = cls.get_user_attrs()
    user_attrs["name"] = cls.__name__
    user_attrs["description"] = cls.__doc__

    secrets_dict = []
    # endpoints contains rendered endpoints, and ep_list contains the names in a list to avoid duplication
    endpoints = []
    ep_list = []
    # Find default cred
    default_cred = cls.default_cred
    default_cred_name = getattr(default_cred, "name", "") or getattr(
        default_cred, "__name__", ""
    )

    credential_list = []
    cred_file_dict = dict()
    for _, cred in enumerate(cls.credentials):
        cred_name = getattr(cred, "name", "") or cred.__name__
        cred_type = cred.type
        cred_file_name = "BP_CRED_{}_{}".format(
            get_valid_identifier(cred_name), cred_type
        )

        if default_cred_name and cred_name == default_cred_name:
            cred.default = True

        credential_list.append(render_credential_template(cred))
        cred_file_dict[cred_file_name] = getattr(cred, "secret", "").get("value", "")
        secrets_dict.append(
            {
                "context": "credential_definition_list." + cred_name,
                "secret_name": cred_name,
                "secret_value": cred_file_dict[cred_file_name],
            }
        )

    # Map to store the [Name: Rendered template for entity]
    entity_name_text_map = {}

    # Edges map to store the edges (dependencies) between entities
    entity_edges = {}

    for service in cls.services:
        entity_name_text_map[service.get_ref().name] = service

        # Edge from services to other entities
        for dep in service.dependencies:
            add_edges(entity_edges, dep.get_ref().name, service.get_ref().name)

    downloadable_img_list = []
    vm_images = []
    for package in cls.packages:
        if getattr(package, "__kind__") == "app_package":
            entity_name_text_map[package.get_ref().name] = package

            # Edge from package to service
            for dep in package.services:
                add_edges(entity_edges, dep.get_ref().name, package.get_ref().name)

        else:
            downloadable_img_list.append(render_vm_disk_package_template(package))
            vm_images.append(package.get_ref().name)
            # Printing all the downloadable images at the top, so ignore its edges

    for substrate in cls.substrates:
        entity_name_text_map[substrate.get_ref().name] = substrate

    deployments = []
    for profile in cls.profiles:
        entity_name_text_map[profile.get_ref().name] = profile

        # Deployments
        deployments.extend(profile.deployments)
        for dep in deployments:
            add_edges(entity_edges, dep.get_ref().name, profile.get_ref().name)
        for patch_config_attr in profile.patch_list:
            entity_name_text_map[
                get_valid_identifier(patch_config_attr.patch_attrs[0].__name__)
            ] = patch_config_attr.patch_attrs[0]

    for deployment in deployments:
        entity_name_text_map[deployment.get_ref().name] = deployment

        # Edges from deployment to package
        for dep in deployment.packages:
            add_edges(entity_edges, dep.get_ref().name, deployment.get_ref().name)

        # Edges from deployment to substrate
        add_edges(
            entity_edges, deployment.substrate.get_ref().name, deployment.get_ref().name
        )

        # Other dependencies
        for dep in deployment.dependencies:
            add_edges(entity_edges, dep.get_ref().name, deployment.get_ref().name)

    # Getting the local files used for secrets
    secret_files = get_secret_variable_files()
    secret_files.extend(get_cred_files())

    if with_secrets or contains_encrypted_secrets:
        # If contains_encrypted_secrets is True then populate secrets directly from payload
        # Fill the secret if flag is set
        if secret_files and (not contains_encrypted_secrets):
            click.secho("Enter the value to be used in secret files")
        for file_name in secret_files:
            if contains_encrypted_secrets:
                try:
                    secret_val = cred_file_dict[file_name]
                except Exception as exp:
                    LOG.debug("Got traceback\n{}".format(traceback.format_exc()))
                    LOG.error("Secret value not found due to {}".format(exp))
                    sys.exit(-1)
            else:
                secret_val = click.prompt(
                    "\nValue for {}".format(file_name),
                    default="",
                    show_default=False,
                    hide_input=True,
                )
            file_loc = os.path.join(get_local_dir(), file_name)
            with open(file_loc, "w+") as fd:
                fd.write(secret_val)

    dependepent_entities = []
    dependepent_entities = get_ordered_entities(entity_name_text_map, entity_edges)

    # Constructing map of patch attribute class name to update config name
    patch_attr_update_config_map = {}
    for k, v in enumerate(dependepent_entities):
        if isinstance(v, ProfileType):
            if not v.patch_list:
                continue
            for update_config in v.patch_list:
                patch_attr_name = update_config.patch_attrs[0].__name__
                update_config_name = get_valid_identifier(update_config.__name__)
                patch_attr_update_config_map[patch_attr_name] = update_config_name

    # Constructing reverse map of above
    update_config_patch_attr_map = dict(
        (v, k) for k, v in patch_attr_update_config_map.items()
    )

    # Setting dsl class and gui display name of entity in beginning.
    # Case: when vm power actions are used in service level then dsl class name of substrate is needed.
    # As service class is rendered before substrate we need to explicitly create substrate ui dsl map initially.
    # This will help in targetting correct substrate to vm power actions
    # TODO move all gui to dsl class mapping to entity.py
    for k, v in enumerate(dependepent_entities):
        update_entity_gui_dsl_name(v.get_gui_name(), v.__name__)

    # Stores config attr classes to be rendered
    config_attr_classes = {}

    # Rendering templates
    for k, v in enumerate(dependepent_entities):
        if isinstance(v, ServiceType):
            dependepent_entities[k] = render_service_template(
                v, secrets_dict, endpoints=endpoints, ep_list=ep_list
            )

        elif isinstance(v, ConfigAttrs):
            config_attr_classes[k] = v

        elif isinstance(v, PackageType):
            dependepent_entities[k] = render_package_template(
                v, secrets_dict, endpoints=endpoints, ep_list=ep_list
            )

        elif isinstance(v, ProfileType):
            dependepent_entities[k] = render_profile_template(
                v,
                update_config_patch_attr_map,
                secrets_dict,
                endpoints=endpoints,
                ep_list=ep_list,
            )

        elif isinstance(v, DeploymentType):
            dependepent_entities[k] = render_deployment_template(v)

        elif isinstance(v, SubstrateType):
            dependepent_entities[k] = render_substrate_template(
                v,
                vm_images=vm_images,
                secrets_dict=secrets_dict,
                endpoints=endpoints,
                ep_list=ep_list,
            )

    """"
    Render config attr class after all other classes are rendered because it may have dependency on other classes. For instance:

    Case 1:
      -> Multiple service classes present
      -> Config attr contains tasks that have call runbook task for a service
      -> Config attr class comes before a service class in dependepent_entities list
    
    In this case service class hasn't stored it's action map (RUNBOOK_ACTION_MAP) and config attr class gets rendered first,
    then a look up for matching action in RUNBOOK_ACTION_MAP will fail and decompile fails.

    Solution: Store all config attr classes encountered in dependepent_entities and render them later when all other classes are rendered.
    """

    for k, v in config_attr_classes.items():
        dependepent_entities[k] = render_config_attr_template(
            v,
            patch_attr_update_config_map,
            secrets_dict,
            endpoints=endpoints,
            ep_list=ep_list,
        )

    is_any_secret_value_available = False
    for _e in secrets_dict:
        if _e.get("secret_value", ""):
            is_any_secret_value_available = True
            break

    if is_any_secret_value_available:
        LOG.info("Creating secret metadata file")
        encrypt_decompile_secrets(secrets_dict=secrets_dict)

    blueprint = render_blueprint_template(cls)

    # Render blueprint metadata
    metadata_str = render_metadata_template(metadata_obj)

    user_attrs.update(
        {
            "secret_files": secret_files,
            "credentials": credential_list,
            "vm_images": downloadable_img_list,
            "dependent_entities": dependepent_entities,
            "blueprint": blueprint,
            "metadata": metadata_str,
            "contains_encrypted_secrets": contains_encrypted_secrets,
            "endpoints": endpoints,
        }
    )

    text = render_template("bp_file_helper.py.jinja2", obj=user_attrs)
    return text.strip()


def get_ordered_entities(entity_name_text_map, entity_edges):
    """Returns the list in which all rendered templates are ordered according to depedencies"""

    res_entity_list = []
    entity_indegree_count = {}

    # Initializing indegree to each entity by 0
    for entity_name in list(entity_name_text_map.keys()):
        entity_indegree_count[entity_name] = 0

    # Iterate over edges and update indegree count for each entity
    for entity_name, to_entity_list in entity_edges.items():
        for entity in to_entity_list:
            entity_indegree_count[entity] += 1

    # Queue to store entities having indegree 0
    queue = []

    # Push entities having indegree count 0
    for entity_name, indegree in entity_indegree_count.items():
        if indegree == 0:
            queue.append(entity_name)

    # Topological sort
    while queue:

        ql = len(queue)

        # Inserting entities in result
        for entity in queue:
            res_entity_list.append(entity_name_text_map[entity])

        while ql:
            # Popping the top element

            cur_entity = queue.pop(0)

            # Iterating its edges, and decrease the indegree of dependent entity by 1
            for to_entity in entity_edges.get(cur_entity, []):
                entity_indegree_count[to_entity] -= 1

                # If indegree is zero push to queue
                if entity_indegree_count[to_entity] == 0:
                    queue.append(to_entity)

            ql -= 1

    return res_entity_list


def add_edges(edges, from_entity, to_entity):
    """Add edges in map edges"""

    if not edges.get(from_entity):
        edges[from_entity] = []

    edges[from_entity].append(to_entity)


def encrypt_decompile_secrets(key=SECRETS_FILE_ENCRYPTION_KEY, secrets_dict=[]):
    """
    Stores secrets_dict in a file and encrypts the file
    A new encrypted file decompiled_secrets.bin is created
    """

    data = str(secrets_dict).encode("utf-8")

    # pad the data with spaces to make it a multiple of 16 bytes
    data += b" " * (AES.block_size - len(data) % AES.block_size)

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    encrypted_file_path = os.path.join(get_local_dir(), "decompiled_secrets.bin")

    with open(encrypted_file_path, "wb") as f:
        [f.write(x) for x in (cipher.nonce, tag, ciphertext)]


def decrypt_decompiled_secrets_file(key=SECRETS_FILE_ENCRYPTION_KEY, pth=""):
    """
    The encrypted file containing the secrets and context is decrypted
    """

    local_dir_pth = pth + "/.local"
    if pth == "":
        local_dir_pth = get_local_dir()

    encrypted_file_path = os.path.join(local_dir_pth, "decompiled_secrets.bin")
    if not os.path.exists(encrypted_file_path):
        return {}

    # read the contents of the encrypted file
    with open(encrypted_file_path, "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    decrypted_data = cipher.decrypt(ciphertext)

    # verify the integrity of the decrypted data using the tag
    try:
        cipher.verify(tag)
    except ValueError:
        print(
            "Warning! The file has been tampered with and the contents may have been altered."
        )

    decrypted_data = decrypted_data.rstrip()
    decrypted_data = ast.literal_eval(decrypted_data.decode())

    decompiled_secrets = json.dumps(decrypted_data)
    decompiled_secrets = json.loads(decompiled_secrets)

    decompiled_secrets_dict = {}

    for decompiled_secret in decompiled_secrets:
        if (
            decompiled_secret["context"].rsplit(".", 1)[0]
            not in decompiled_secrets_dict
        ):
            decompiled_secrets_dict[decompiled_secret["context"].rsplit(".", 1)[0]] = {}
        decompiled_secrets_dict[decompiled_secret["context"].rsplit(".", 1)[0]][
            decompiled_secret["secret_name"]
        ] = decompiled_secret["secret_value"]

    return decompiled_secrets_dict
