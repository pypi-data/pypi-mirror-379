import os

from calm.dsl.decompile.render import render_template
from calm.dsl.decompile.endpoint import render_endpoint
from calm.dsl.decompile.task import render_task_template
from calm.dsl.builtins import VariableType, TaskType, CalmEndpoint as Endpoint
from calm.dsl.decompile.file_handler import get_local_dir
from calm.dsl.log import get_logging_handle
from calm.dsl.constants import VARIABLE

LOG = get_logging_handle(__name__)
SECRET_VAR_FILES = []


def render_variable_template(
    cls,
    entity_context,
    context="",
    variable_context="variable",  # In some case, the spec field might not be variable_list
    secrets_dict=[],
    credentials_list=[],
    rendered_credential_list=[],
    endpoints=[],
    ep_list=[],
    ignore_cred_dereference_error=False,
):

    LOG.debug("Rendering {} variable template".format(cls.__name__))
    if not isinstance(cls, VariableType):
        raise TypeError("{} is not of type {}".format(cls, VariableType))

    if cls.options:
        options = cls.options.get_dict()

    if cls.type in [
        VARIABLE.TYPE.EXEC_LOCAL,
        VARIABLE.TYPE.HTTP_LOCAL,
        VARIABLE.TYPE.EXEC_SECRET,
        VARIABLE.TYPE.HTTP_SECRET,
    ]:
        ep = cls.options.get("exec_target_reference", None)
        if ep:
            endpoint_name = ep.get("name", "")
            if endpoint_name not in ep_list:
                endpoints.append(render_endpoint(Endpoint.use_existing(endpoint_name)))
                ep_list.append(endpoint_name)
        else:
            options.pop("exec_target_reference")

    # Updating the context of variables
    entity_context = entity_context + "_" + variable_context + "_" + cls.__name__
    context = context + variable_context + "_list." + cls.__name__

    user_attrs = cls.get_user_attrs()
    user_attrs["description"] = cls.__doc__ or ""

    # Escape new line character. As it is inline parameter for CalmVariable helper
    user_attrs["description"] = user_attrs["description"].replace("\n", "\\n")

    var_val_type = getattr(cls, "value_type", "STRING")
    var_type = ""
    schema_file = None

    if not cls.options:
        var_type = "simple"

    else:
        choices = options.get("choices", [])
        option_type = options.get("type", "")

        if (not choices) and (option_type == "PREDEFINED"):
            var_type = "simple"

    if cls.regex:
        regex = cls.regex.get_dict()
        user_attrs["regex"] = regex.get("value", None)
        if user_attrs["regex"]:
            user_attrs["regex"] = repr(user_attrs["regex"]).strip("'")
        user_attrs["validate_regex"] = regex.get("should_validate", False)

    else:
        user_attrs["regex"] = None
        user_attrs["validate_regex"] = False

    if cls.editables:
        user_attrs["runtime"] = cls.editables["value"]
    else:
        user_attrs["runtime"] = False

    user_attrs["name"] = cls.__name__

    if var_type == "simple":
        is_secret = True if user_attrs["type"] == "SECRET" else False

        if is_secret:
            secrets_dict.append(
                {
                    "context": context,
                    "secret_name": cls.__name__,
                    "secret_value": getattr(cls, "value", ""),
                }
            )

            user_attrs["value"] = get_secret_var_val(
                entity_context, getattr(cls, "value", "")
            )
            if var_val_type == "STRING":
                schema_file = "var_simple_secret_string.py.jinja2"
            elif var_val_type == "INT":
                schema_file = "var_simple_secret_int.py.jinja2"
            elif var_val_type == "TIME":
                schema_file = "var_simple_secret_time.py.jinja2"
            elif var_val_type == "DATE":
                schema_file = "var_simple_secret_date.py.jinja2"
            elif var_val_type == "DATE_TIME":
                schema_file = "var_simple_secret_datetime.py.jinja2"
            elif var_val_type == "MULTILINE_STRING":
                schema_file = "var_simple_secret_multiline.py.jinja2"

        else:
            if var_val_type == "STRING":
                schema_file = "var_simple_string.py.jinja2"
            elif var_val_type == "INT":
                schema_file = "var_simple_int.py.jinja2"
            elif var_val_type == "TIME":
                schema_file = "var_simple_time.py.jinja2"
            elif var_val_type == "DATE":
                schema_file = "var_simple_date.py.jinja2"
            elif var_val_type == "DATE_TIME":
                schema_file = "var_simple_datetime.py.jinja2"
            elif var_val_type == "MULTILINE_STRING":
                user_attrs["value"] = repr(user_attrs["value"])
                schema_file = "var_simple_multiline.py.jinja2"

    else:
        data_type = cls.data_type
        option_type = options.get("type", "PREDEFINED")

        if option_type == "PREDEFINED":
            user_attrs["choices"] = options.get("choices", [])

            if data_type == "BASE":
                if var_val_type == "STRING":
                    schema_file = "var_with_options_predefined_string.py.jinja2"
                elif var_val_type == "INT":
                    schema_file = "var_with_options_predefined_int.py.jinja2"
                elif var_val_type == "DATE":
                    schema_file = "var_with_options_predefined_date.py.jinja2"
                elif var_val_type == "TIME":
                    schema_file = "var_with_options_predefined_time.py.jinja2"
                elif var_val_type == "DATE_TIME":
                    schema_file = "var_with_options_predefined_datetime.py.jinja2"
                elif var_val_type == "MULTILINE_STRING":
                    user_attrs["value"] = repr(user_attrs["value"])
                    schema_file = "var_with_options_predefined_multiline.py.jinja2"

            else:
                defaults = cls.value
                user_attrs["value"] = defaults.split(",")
                if var_val_type == "STRING":
                    schema_file = "var_with_options_predefined_array_string.py.jinja2"
                elif var_val_type == "INT":
                    schema_file = "var_with_options_predefined_array_int.py.jinja2"
                elif var_val_type == "DATE":
                    schema_file = "var_with_options_predefined_array_date.py.jinja2"
                elif var_val_type == "TIME":
                    schema_file = "var_with_options_predefined_array_time.py.jinja2"
                elif var_val_type == "DATE_TIME":
                    schema_file = "var_with_options_predefined_array_datetime.py.jinja2"
                elif var_val_type == "MULTILINE_STRING":
                    user_attrs["value"] = repr(user_attrs["value"])
                    schema_file = (
                        "var_with_options_predefined_array_multiline.py.jinja2"
                    )

        else:
            options.pop("choices", None)
            task = TaskType.decompile(options)
            task.__name__ = "SampleTask"
            if user_attrs["value"]:  # CALM-45352
                user_attrs["default_value"] = user_attrs.pop("value")
            user_attrs["value"] = render_task_template(
                task,
                entity_context=entity_context,
                credentials_list=credentials_list,
                rendered_credential_list=rendered_credential_list,
                use_calm_var_task=True,
                ignore_cred_dereference_error=ignore_cred_dereference_error,
            )

            if data_type == "BASE":
                if var_val_type == "STRING":
                    schema_file = "var_with_options_fromTask_string.py.jinja2"
                elif var_val_type == "INT":
                    schema_file = "var_with_options_fromTask_int.py.jinja2"
                elif var_val_type == "DATE":
                    schema_file = "var_with_options_fromTask_date.py.jinja2"
                elif var_val_type == "TIME":
                    schema_file = "var_with_options_fromTask_time.py.jinja2"
                elif var_val_type == "DATE_TIME":
                    schema_file = "var_with_options_fromTask_datetime.py.jinja2"
                elif var_val_type == "MULTILINE_STRING":
                    if user_attrs.get("default_value"):
                        user_attrs["default_value"] = repr(user_attrs["default_value"])
                    schema_file = "var_with_options_fromTask_multiline.py.jinja2"
            else:
                if var_val_type == "STRING":
                    schema_file = "var_with_options_fromTask_array_string.py.jinja2"
                elif var_val_type == "INT":
                    schema_file = "var_with_options_fromTask_array_int.py.jinja2"
                elif var_val_type == "DATE":
                    schema_file = "var_with_options_fromTask_array_date.py.jinja2"
                elif var_val_type == "TIME":
                    schema_file = "var_with_options_fromTask_array_time.py.jinja2"
                elif var_val_type == "DATE_TIME":
                    schema_file = "var_with_options_fromTask_array_datetime.py.jinja2"
                elif var_val_type == "MULTILINE_STRING":
                    if user_attrs.get("default_value"):
                        user_attrs["default_value"] = repr(user_attrs["default_value"])
                    schema_file = "var_with_options_fromTask_array_multiline.py.jinja2"

    if not schema_file:
        raise Exception("Unknown variable type")

    text = render_template(schema_file=schema_file, obj=user_attrs)
    return text.strip()


def get_secret_var_val(entity_context, value=""):

    global SECRET_VAR_FILES

    SECRET_VAR_FILES.append(entity_context)
    file_location = os.path.join(get_local_dir(), entity_context)

    with open(file_location, "w+") as fd:
        fd.write(value)

    # Replace read_local_file by a constant
    return entity_context


def get_secret_variable_files():
    """return the global local files used for secret variables"""

    return SECRET_VAR_FILES


def init_variable_globals():

    global SECRET_VAR_FILES
    SECRET_VAR_FILES = []
