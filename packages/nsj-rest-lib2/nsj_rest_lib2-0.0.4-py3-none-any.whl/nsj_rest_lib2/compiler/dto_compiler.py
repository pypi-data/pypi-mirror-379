import ast

import black

from nsj_rest_lib2.compiler.edl_model.entity_model import EntityModel
from nsj_rest_lib2.compiler.util.str_util import CompilerStrUtil


class DTOCompiler:
    def __init__(self):
        pass

    def compile(
        self,
        entity_model: EntityModel,
        ast_dto_attributes: list[ast.stmt],
        enum_classes: list[ast.stmt],
    ) -> tuple[str, str]:
        """
        Compila o código do DTO a partir do AST e retorna o código compilado.

        :param entity_model: Modelo de entidade
        :type entity_model: EntityModel

        :param ast_dto_attributes: Atributos do DTO
        :type ast_dto_attributes: list[ast.stmt]

        :param enum_classes: Classes de enumeração
        :type enum_classes: list[ast.stmt]

        :return: Código compilado do DTO
        :rtype: str
        """
        imports = [
            # import datetime
            ast.Import(names=[ast.alias(name="datetime", asname=None)]),
            # import enum
            ast.Import(names=[ast.alias(name="enum", asname=None)]),
            # import uuid
            ast.Import(names=[ast.alias(name="uuid", asname=None)]),
            # from nsj_rest_lib.decorator.dto import DTO
            ast.ImportFrom(
                module="nsj_rest_lib.decorator.dto",
                names=[ast.alias(name="DTO", asname=None)],
                level=0,
            ),
            # from nsj_rest_lib.descriptor.dto_field import DTOField
            ast.ImportFrom(
                module="nsj_rest_lib.descriptor.dto_field",
                names=[ast.alias(name="DTOField", asname=None)],
                level=0,
            ),
        ]

        class_name = f"{CompilerStrUtil.to_pascal_case(entity_model.id)}DTO"
        ast_class = ast.ClassDef(
            name=class_name,
            bases=[ast.Name(id="DTOBase", ctx=ast.Load())],
            keywords=[],
            decorator_list=[
                ast.Call(
                    func=ast.Name(id="DTO", ctx=ast.Load()),
                    args=[],
                    keywords=[],
                )
            ],
            body=ast_dto_attributes,
        )

        # Definindo o módulo
        module = ast.Module(
            body=imports + enum_classes + [ast_class],
            type_ignores=[],
        )
        module = ast.fix_missing_locations(module)

        # Compilando o AST do DTO para o código Python
        code = ast.unparse(module)

        # Chamando o black para formatar o código Python do DTO
        code = black.format_str(code, mode=black.FileMode())

        return (class_name, code)
