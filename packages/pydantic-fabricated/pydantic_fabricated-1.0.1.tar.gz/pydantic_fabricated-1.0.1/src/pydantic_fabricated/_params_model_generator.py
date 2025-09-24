import inspect
from typing import Any

from pydantic import BaseModel, create_model


def create_constructor_params_model(class_: type[Any]) -> type[BaseModel]:
    """
    Create a Pydantic model from a class's constructor parameters.

    :param class_: The class to generate a Pydantic model for
    :return: A Pydantic BaseModel subclass with fields matching the class's constructor parameters
    """
    fields: dict[str, tuple[str, Any]] = {}
    for param_name, param in inspect.signature(class_.__init__).parameters.items():
        if param_name == 'self':
            continue
        if param.annotation is param.empty:
            msg = f"Parameter '{param_name}' in {class_.__name__}.__init__ is missing a type annotation"
            raise ValueError(msg)
        if param.kind in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
            msg = (
                f"Parameter '{param_name}' in {class_.__name__}.__init__ is a variadic parameter, "
                f'which is not supported'
            )
            raise ValueError(msg)
        if param.kind == param.POSITIONAL_ONLY:
            msg = (
                f"Parameter '{param_name}' in {class_.__name__}.__init__ is a positional-only parameter, "
                f'which is not supported'
            )
            raise ValueError(msg)
        if param.default is not param.empty:
            fields[param_name] = (param.annotation, param.default)
        else:
            fields[param_name] = (param.annotation, ...)

    return create_model(f'{class_.__name__}ConstructorParamsModel', __base__=BaseModel, **fields)  # type: ignore [no-any-return, call-overload]
