import enum
from typing import List


class PrimitiveTypes(enum.Enum):
    # TODO Validar esses tipos
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"
    UUID = "uuid"
    CURRENCY = "currency"
    QUANTITY = "quantity"
    CPF = "cpf"
    CNPJ = "cnpj"
    CPF_CNPJ = "cpf_cnpj"
    EMAIL = "email"
    DATE = "date"
    DATETIME = "datetime"


MAPPING_PRIMITIVE_TYPES_TO_PYTHON = {
    PrimitiveTypes.STRING: "str",
    PrimitiveTypes.NUMBER: "float",
    PrimitiveTypes.INTEGER: "int",
    PrimitiveTypes.BOOLEAN: "bool",
    PrimitiveTypes.ARRAY: "List",
    PrimitiveTypes.OBJECT: "dict",
    PrimitiveTypes.UUID: "uuid.UUID",
    PrimitiveTypes.CURRENCY: "float",
    PrimitiveTypes.QUANTITY: "float",
    PrimitiveTypes.CPF: "str",
    PrimitiveTypes.CNPJ: "str",
    PrimitiveTypes.CPF_CNPJ: "str",
    PrimitiveTypes.EMAIL: "str",
    PrimitiveTypes.DATE: "datetime.date",
    PrimitiveTypes.DATETIME: "datetime.datetime",
}

BasicTypes = int | bool | float | str
DefaultTypes = BasicTypes | List[BasicTypes]
