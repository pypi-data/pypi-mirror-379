import sys

from calm.dsl.decompile.render import render_template
from calm.dsl.store import Cache
from calm.dsl.constants import CACHE
from calm.dsl.log import get_logging_handle

LOG = get_logging_handle(__name__)


def render_ahv_vm_nic(cls):

    # Note cls.get_dict() may not contain subnet name
    # So it will fail. So use class attributes instead of getting dict object
    subnet_ref = cls.subnet_reference
    if subnet_ref:
        subnet_ref = subnet_ref.get_dict()

    nic_type = cls.nic_type
    network_function_nic_type = cls.network_function_nic_type

    user_attrs = {}
    ip_endpoints = []
    for ip in cls.ip_endpoint_list:
        ip_endpoints.append((ip.get_dict()["ip"]))
    if ip_endpoints:
        user_attrs["ip_endpoint_list"] = ip_endpoints
    subnet_uuid = subnet_ref.get("uuid", "")
    if subnet_uuid.startswith("@@{") and subnet_uuid.endswith("}@@"):
        user_attrs["subnet_name"] = subnet_uuid
    else:
        subnet_cache_data = Cache.get_entity_data_using_uuid(
            entity_type=CACHE.ENTITY.AHV_SUBNET, uuid=subnet_uuid
        )
        if not subnet_cache_data:
            LOG.error("Subnet with uuid '{}' not found".format(subnet_uuid))
            sys.exit(-1)

        user_attrs["subnet_name"] = subnet_cache_data["name"]
        if subnet_cache_data.get("vpc_name", ""):
            user_attrs["vpc_name"] = subnet_cache_data["vpc_name"]
        else:
            user_attrs["cluster_name"] = subnet_cache_data["cluster_name"]

    schema_file = ""
    if nic_type == "NORMAL_NIC":
        if network_function_nic_type == "INGRESS":
            schema_file = "ahv_normal_ingress_nic.py.jinja2"

        elif network_function_nic_type == "EGRESS":
            schema_file = "ahv_normal_egress_nic.py.jinja2"

        elif network_function_nic_type == "TAP":
            schema_file = "ahv_normal_tap_nic.py.jinja2"

        else:
            LOG.error(
                "Unknown network function nic type '{}'".format(
                    network_function_nic_type
                )
            )
            sys.exit(-1)

    elif nic_type == "DIRECT_NIC":
        if network_function_nic_type == "INGRESS":
            schema_file = "ahv_direct_ingress_nic.py.jinja2"

        elif network_function_nic_type == "EGRESS":
            schema_file = "ahv_direct_egress_nic.py.jinja2"

        elif network_function_nic_type == "TAP":
            schema_file = "ahv_direct_tap_nic.py.jinja2"

        else:
            LOG.error(
                "Unknown network function nic type '{}'".format(
                    network_function_nic_type
                )
            )
            sys.exit(-1)

    else:
        LOG.error("Unknown nic type '{}'".format(nic_type))
        sys.exit(-1)

    text = render_template(schema_file=schema_file, obj=user_attrs)
    return text.strip()
