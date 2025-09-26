from .entity import EntityType, Entity

from calm.dsl.log import get_logging_handle
from .validator import PropertyValidator
from calm.dsl.constants import ENTITY
from .utils import is_compile_secrets

LOG = get_logging_handle(__name__)

# AHV Account


class AhvAccountType(EntityType):
    __schema_name__ = "AhvAccount"
    __openapi_type__ = ENTITY.OPENAPI_TYPE.AHV

    def compile(cls):
        cdict = super().compile()

        pswd = cdict.pop("password", "")
        cdict["password"] = {
            "value": pswd if is_compile_secrets() else "",
            "attrs": {"is_secret_modified": True},
        }

        return cdict


class AhvAccountValidator(PropertyValidator, openapi_type=ENTITY.OPENAPI_TYPE.AHV):
    __default__ = None
    __kind__ = AhvAccountType


def ahv_account(**kwargs):
    name = kwargs.pop("name", None)
    bases = (Entity,)
    return AhvAccountType(name, bases, kwargs)


AhvAccountData = ahv_account()
