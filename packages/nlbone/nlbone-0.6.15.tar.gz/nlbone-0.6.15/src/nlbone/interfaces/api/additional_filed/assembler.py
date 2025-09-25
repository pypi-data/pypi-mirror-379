import inspect
from typing import Any, Dict

from pydantic import BaseModel

from nlbone.container import Container
from nlbone.interfaces.api.additional_filed.field_registry import FieldRule, ResourceRegistry


def assemble_response(
    obj: Any,
    reg: ResourceRegistry,
    selected_rules: Dict[str, FieldRule],
    base_schema: type[BaseModel] | None,
    session,
) -> Dict[str, Any]:
    base = {f: getattr(obj, f, None) for f in reg.default_fields - set(reg.rules.keys())}
    if base_schema:
        base = base_schema.model_validate(base).model_dump()

    ctx = {"file_service": Container.file_service(), "entity": obj, "db": session}
    for name, rule in selected_rules.items():
        if rule.loader:
            value = inject_dependencies(rule.loader, dependencies=ctx)
        else:
            value = _get_nested_attr(obj, name)
        _put_nested_key(base, name, value)

    return base


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {name: dependency for name, dependency in dependencies.items() if name in params}
    return handler(**deps)


def _get_nested_attr(obj: Any, dotted: str):
    cur = obj
    for part in dotted.split("."):
        if cur is None:
            return None
        cur = getattr(cur, part, None)
    return cur


def _put_nested_key(base: Dict[str, Any], dotted: str, value: Any):
    parts = dotted.split(".")
    cur = base
    for p in parts[:-1]:
        if p not in cur or not isinstance(cur[p], dict):
            cur[p] = {}
        cur = cur[p]
    cur[parts[-1]] = value
