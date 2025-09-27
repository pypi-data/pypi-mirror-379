from pydantic import BaseModel, Field

from nsj_rest_lib2.compiler.edl_model.primitives import BasicTypes, PrimitiveTypes


class TraitPropertyMetaModel(BaseModel):
    type: PrimitiveTypes = Field(..., description="Tipo da propriedade.")
    value: BasicTypes = Field(
        ..., description="Valor fixo da propriedade de condicionamento do trait."
    )
