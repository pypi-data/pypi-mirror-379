from pydantic import BaseModel, Field
from typing import List, Optional, Literal


class ColumnMetaModel(BaseModel):
    column: str = Field(..., description="Nome da coluna no banco de dados.")
