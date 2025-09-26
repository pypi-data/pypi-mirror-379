from __future__ import annotations

import functools
import inspect
import operator
import sys
import threading
import types
from functools import reduce
from typing import Any, Dict, Union, get_args, get_origin, get_type_hints
try:
    # typing.Annotated may not exist in older 3.9 without typing_extensions
    from typing import Annotated  # type: ignore
except Exception:  # pragma: no cover
    Annotated = None  # type: ignore

_UNION_ORIGINS = tuple(
    x for x in (Union, getattr(types, "UnionType", None)) if x is not None
)


"""
======================================================================
 Project: Gedcom-X
 File:    schema.py
 Author:  David J. Cartwright
 Purpose: provide schema for serialization and extensibility

 Created: 2025-08-25
 Updated:
   - 2025-09-03: _from_json_ refactor
   - 2025-09-09: added schema_class
   - 2025-09-12: extras inheritance; robust union rebuild; URI/Resource binding
   - 2025-09-12: make sure extra fields get inherited, and handles by __init__, jsonify returns alphabetized dict

======================================================================
"""


class Schema:
    """
    Central registry of fields for classes.

    - field_type_table: {"ClassName": {"field": <type or type-string>}}
    - URI/Resource preference in unions: URI > Resource > first-declared
    - Optional/None is stripped
    - Containers are preserved; their inner args are normalized recursively
    """

    def __init__(self) -> None:
        self.field_type_table: Dict[str, Dict[str, Any]] = {}
        self._extras: Dict[str, Dict[str, Any]] = {}
        self._toplevel: Dict[str, Dict[str, Any]] = {}

        # NEW: inheritance tracking + inherited extras cache
        self._bases: Dict[str, list[str]] = {}              # class_name -> [base names]
        self._subclasses: Dict[str, set[str]] = {}          # base_name -> {subclass names}
        self._inherited_extras: Dict[str, Dict[str, Any]] = {}  # class_name -> {field: type}

        # Optional binding to concrete classes to avoid name-only matching.
        self._uri_cls: type | None = None
        self._resource_cls: type | None = None

    # ──────────────────────────────
    # Utils
    # ──────────────────────────────
    def _cls_name(self, cls_or_name: type | str) -> str:
        return cls_or_name if isinstance(cls_or_name, str) else cls_or_name.__name__

    # ──────────────────────────────
    # Bind concrete classes (optional)
    # ──────────────────────────────
    def set_uri_class(self, cls: type | None) -> None:
        self._uri_cls = cls

    def set_resource_class(self, cls: type | None) -> None:
        self._resource_cls = cls

    # ──────────────────────────────
    # Public API
    # ──────────────────────────────
    def register_class(
        self,
        cls: type,
        *,
        mapping: Dict[str, Any] | None = None,
        include_bases: bool = True,
        use_annotations: bool = True,
        use_init: bool = True,
        overwrite: bool = False,
        ignore: set[str] | None = None,
        toplevel: bool = False,
        toplevel_meta: Dict[str, Any] | None = None,
    ) -> None:
        """
        Introspect and register fields for a class.

        - reads class __annotations__ (preferred) or __init__ annotations
        - merges base classes (MRO) if include_bases=True
        - applies `mapping` overrides last
        - normalizes each type:
            strip Optional → prefer URI/Resource → collapse union to single
        """
        cname = cls.__name__
        ignore = ignore or set()

        def collect(c: type) -> Dict[str, Any]:
            d: Dict[str, Any] = {}
            if use_annotations:
                d.update(self._get_hints_from_class(c))
            if use_init and not d:
                d.update(self._get_hints_from_init(c))
            # filter private / ignored
            for k in list(d.keys()):
                if k in ignore or k.startswith("_"):
                    d.pop(k, None)
            # normalize each
            for k, v in list(d.items()):
                d[k] = self._normalize_field_type(v)
            return d

        fields: Dict[str, Any] = {}
        classes = list(reversed(cls.mro())) if include_bases else [cls]
        for c in classes:
            if c is object:
                continue
            fields.update(collect(c))

        if mapping:
            for k, v in mapping.items():
                fields[k] = self._normalize_field_type(v)

        # Track inheritance relationships
        bases = [b.__name__ for b in cls.mro()[1:] if b is not object]
        self._bases[cname] = bases
        for b in bases:
            self._subclasses.setdefault(b, set()).add(cname)

        # Apply extras defined directly for this class (if registered earlier)
        direct_extras = dict(self._extras.get(cname, {}))
        if direct_extras:
            for k, v in direct_extras.items():
                fields.setdefault(k, v)

        # Inherit extras from bases (direct + their inherited), without overriding subclass fields
        inherited: Dict[str, Any] = {}
        for bname in bases:
            for src in (self._extras.get(bname, {}), self._inherited_extras.get(bname, {})):
                if not src:
                    continue
                for k, v in src.items():
                    if k not in fields:
                        inherited.setdefault(k, v)

        if inherited:
            merged = self._inherited_extras.get(cname, {})
            merged.update(inherited)
            self._inherited_extras[cname] = merged
            fields.update(inherited)

        # Commit the table
        if not overwrite and cname in self.field_type_table:
            self.field_type_table[cname].update(fields)
        else:
            self.field_type_table[cname] = fields

        if toplevel:
            self._toplevel[cname] = dict(toplevel_meta or {})

    def _propagate_extra_down(self, subclass_name: str, name: str, typ: Any, *, overwrite: bool) -> None:
        """Apply an inherited extra to subclass and its descendants if not overridden."""
        fields = self.field_type_table.setdefault(subclass_name, {})
        if overwrite or name not in fields:
            fields[name] = typ
            inh = self._inherited_extras.setdefault(subclass_name, {})
            inh[name] = typ
        for deeper in self._subclasses.get(subclass_name, set()):
            self._propagate_extra_down(deeper, name, typ, overwrite=overwrite)

    def register_extra(
        self,
        cls: type | str,
        name: str,
        typ: Any,
        *,
        overwrite: bool = False,
    ) -> None:
        """Register a single extra field (normalized) and propagate to subclasses."""
        cname = self._cls_name(cls)
        self.field_type_table.setdefault(cname, {})
        nt = self._normalize_field_type(typ)

        # record on declaring class
        if overwrite or name not in self.field_type_table[cname]:
            self.field_type_table[cname][name] = nt
        self._extras.setdefault(cname, {})[name] = nt

        # propagate to current subclasses
        for sub in self._subclasses.get(cname, set()):
            self._propagate_extra_down(sub, name, nt, overwrite=overwrite)

    def normalize_all(self) -> None:
        """Re-run normalization across all registered fields."""
        for _, fields in self.field_type_table.items():
            for k, v in list(fields.items()):
                fields[k] = self._normalize_field_type(v)

    # lookups
    def get_class_fields(self, type_name: str) -> Dict[str, Any] | None:
        return self.field_type_table.get(type_name)

    def set_toplevel(self, cls: type, *, meta: Dict[str, Any] | None = None) -> None:
        self._toplevel[cls.__name__] = dict(meta or {})

    def is_toplevel(self, cls_or_name: type | str) -> bool:
        name = cls_or_name if isinstance(cls_or_name, str) else cls_or_name.__name__
        return name in self._toplevel

    def get_toplevel(self) -> Dict[str, Dict[str, Any]]:
        return dict(self._toplevel)

    def get_extras(self, cls_or_name: type | str) -> Dict[str, Any]:
        """Direct extras declared on this class (not inherited)."""
        name = cls_or_name if isinstance(cls_or_name, str) else cls_or_name.__name__
        return dict(self._extras.get(name, {}))

    def get_all_extras(self, cls_or_name: type | str) -> Dict[str, Any]:
        """Direct + inherited extras for this class."""
        name = self._cls_name(cls_or_name)
        out = {}
        out.update(self._inherited_extras.get(name, {}))
        out.update(self._extras.get(name, {}))
        return dict(out)

    @property
    def json(self) -> dict[str, dict[str, str]]:
        return schema_to_jsonable(self)

    # ──────────────────────────────
    # Introspection helpers
    # ──────────────────────────────
    def _get_hints_from_class(self, cls: type) -> Dict[str, Any]:
        module = sys.modules.get(cls.__module__)
        gns = dict(module.__dict__) if module else {}
        # Ensure these names exist even if the module didn't import them:
        if self._uri_cls is not None:
            gns.setdefault("URI", self._uri_cls)
        if self._resource_cls is not None:
            gns.setdefault("Resource", self._resource_cls)

        lns = dict(vars(cls))
        try:
            return get_type_hints(cls, include_extras=True, globalns=gns, localns=lns)
        except Exception:
            # fallback keeps strings — but we’ll fix those below
            return dict(getattr(cls, "__annotations__", {}) or {})

    def _get_hints_from_init(self, cls: type) -> Dict[str, Any]:
        """Parameter annotations from __init__ (excluding self/return/*args/**kwargs)."""
        fn = cls.__dict__.get("__init__", getattr(cls, "__init__", None))
        if not callable(fn):
            return {}
        module = sys.modules.get(cls.__module__)
        gns = module.__dict__ if module else {}
        # Ensure these names exist even if the module didn't import them:
        if self._uri_cls is not None:
            gns.setdefault("URI", self._uri_cls)
        if self._resource_cls is not None:
            gns.setdefault("Resource", self._resource_cls)
        lns = dict(vars(cls))
        try:
            hints = get_type_hints(fn, include_extras=True, globalns=gns, localns=lns)
        except Exception:
            hints = dict(getattr(fn, "__annotations__", {}) or {})
        hints.pop("return", None)
        hints.pop("self", None)
        # drop *args/**kwargs
        sig = inspect.signature(fn)
        for pname, p in list(sig.parameters.items()):
            if p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
                hints.pop(pname, None)
        return hints

    # ──────────────────────────────
    # Normalization pipeline
    #   strip Optional -> prefer URI/Resource -> collapse unions
    #   (recurse into containers)
    # ──────────────────────────────
    def _normalize_field_type(self, tp: Any) -> Any:
        tp = self._strip_optional(tp)
        tp = self._prefer_uri_or_resource_or_first(tp)
        tp = self._collapse_unions(tp)
        return tp

    # 1) Remove None from unions and strip Optional[...] wrappers
    def _strip_optional(self, tp: Any) -> Any:
        if isinstance(tp, str):
            return self._strip_optional_str(tp)

        origin = get_origin(tp)
        args = get_args(tp)

        if Annotated is not None and origin is Annotated:
            return self._strip_optional(args[0])

        if origin in _UNION_ORIGINS:
            kept = tuple(a for a in args if a is not type(None))  # noqa: E721
            if not kept:
                return Any
            if len(kept) == 1:
                return self._strip_optional(kept[0])
            # rebuild union (still a union; later steps will collapse)
            return self._rebuild_union_tuple(kept)

        if origin in (list, set, tuple, dict):
            sub = tuple(self._strip_optional(a) for a in args)
            return self._rebuild_param(origin, sub, fallback=tp)

        return tp

    # 2) In any union, prefer URI (if present), else Resource (if present), else first declared
    def _prefer_uri_or_resource_or_first(self, tp: Any) -> Any:
        if isinstance(tp, str):
            # if these are strings but we know the classes, return the classes
            if tp == "URI" and self._uri_cls:
                return self._uri_cls
            if tp == "Resource" and self._resource_cls:
                return self._resource_cls
            return self._prefer_str(tp)  # legacy fallback

        origin = get_origin(tp)
        args = get_args(tp)

        if Annotated is not None and origin is Annotated:
            return self._prefer_uri_or_resource_or_first(args[0])

        if origin in _UNION_ORIGINS:
            # pick URI if present, else Resource, else first
            pick = None
            for a in args:
                name = a if isinstance(a, str) else getattr(a, "__name__", "")
                if (a is self._uri_cls) or (name == "URI"):
                    pick = self._uri_cls or a
                    break
            if pick is None:
                for a in args:
                    name = a if isinstance(a, str) else getattr(a, "__name__", "")
                    if (a is self._resource_cls) or (name == "Resource"):
                        pick = self._resource_cls or a
                        break
            if pick is None:
                pick = args[0]
            return self._prefer_uri_or_resource_or_first(pick)

        if origin in (list, set, tuple, dict):
            sub = tuple(self._prefer_uri_or_resource_or_first(a) for a in args)
            return self._rebuild_param(origin, sub, fallback=tp)

        return tp


    # 3) If any union still remains (it shouldn't after step 2), collapse to first
    def _collapse_unions(self, tp: Any) -> Any:
        if isinstance(tp, str):
            return self._collapse_unions_str(tp)

        origin = get_origin(tp)
        args = get_args(tp)

        if Annotated is not None and origin is Annotated:
            return self._collapse_unions(args[0])

        if origin in _UNION_ORIGINS:
            return self._collapse_unions(args[0])  # first only

        if origin in (list, set, tuple, dict):
            sub = tuple(self._collapse_unions(a) for a in args)
            return self._rebuild_param(origin, sub, fallback=tp)

        return tp

    # ──────────────────────────────
    # Helpers: typing objects
    # ──────────────────────────────
    def _name_of(self, a: Any) -> str:
        if isinstance(a, str):
            return a.strip()
        if isinstance(a, type):
            return getattr(a, "__name__", str(a))
        # typing objects: str(...) fallback
        return str(a).replace("typing.", "")

    def _rebuild_union_tuple(self, args: tuple[Any, ...]) -> Any:
        # Prefer PEP 604 A|B|C; fall back to typing.Union
        try:
            return reduce(operator.or_, args)  # e.g., A | B | C
        except TypeError:
            from typing import Union as _TypingUnion
            return _TypingUnion.__getitem__(args)  # typing.Union[A, B, C]

    def _rebuild_param(self, origin: Any, sub: tuple[Any, ...], *, fallback: Any) -> Any:
        try:
            return origin[sub] if sub else origin
        except TypeError:
            return fallback

    # ──────────────────────────────
    # Helpers: strings
    # ──────────────────────────────
    def _strip_optional_str(self, s: str) -> str:
        s = s.strip().replace("typing.", "")
        # peel Optional[...] wrappers
        while s.startswith("Optional[") and s.endswith("]"):
            s = s[len("Optional["):-1].strip()

        # Union[A, B, None]
        if s.startswith("Union[") and s.endswith("]"):
            inner = s[len("Union["):-1].strip()
            parts = [p for p in self._split_top_level(inner, ",") if p.strip() not in ("None", "NoneType", "")]
            return f"Union[{', '.join(parts)}]" if len(parts) > 1 else (parts[0].strip() if parts else "Any")

        # A | B | None
        if "|" in s:
            parts = [p.strip() for p in self._split_top_level(s, "|")]
            parts = [p for p in parts if p not in ("None", "NoneType", "")]
            return " | ".join(parts) if len(parts) > 1 else (parts[0] if parts else "Any")

        # containers: normalize inside
        for head in ("List", "Set", "Tuple", "Dict", "Annotated"):
            if s.startswith(head + "[") and s.endswith("]"):
                inner = s[len(head) + 1:-1]
                if head == "Annotated":
                    # Annotated[T, ...] -> T
                    items = self._split_top_level(inner, ",")
                    return self._strip_optional_str(items[0].strip()) if items else "Any"
                if head in ("List", "Set"):
                    elem = self._strip_optional_str(inner)
                    return f"{head}[{elem}]"
                if head == "Tuple":
                    elems = [self._strip_optional_str(p.strip()) for p in self._split_top_level(inner, ",")]
                    return f"Tuple[{', '.join(elems)}]"
                if head == "Dict":
                    kv = self._split_top_level(inner, ",")
                    k = self._strip_optional_str(kv[0].strip()) if kv else "Any"
                    v = self._strip_optional_str(kv[1].strip()) if len(kv) > 1 else "Any"
                    return f"Dict[{k}, {v}]"

        return s

    def _prefer_str(self, s: str) -> str:
        s = s.strip().replace("typing.", "")
        # Union[...] form
        if s.startswith("Union[") and s.endswith("]"):
            inner = s[len("Union["):-1]
            parts = [p.strip() for p in self._split_top_level(inner, ",")]
            if "URI" in parts:
                return "URI"
            if "Resource" in parts:
                return "Resource"
            return parts[0] if parts else "Any"

        # PEP 604 bars
        if "|" in s:
            parts = [p.strip() for p in self._split_top_level(s, "|")]
            if "URI" in parts:
                return "URI"
            if "Resource" in parts:
                return "Resource"
            return parts[0] if parts else "Any"

        # containers
        for head in ("List", "Set", "Tuple", "Dict", "Annotated"):
            if s.startswith(head + "[") and s.endswith("]"):
                inner = s[len(head) + 1:-1]
                if head == "Annotated":
                    items = self._split_top_level(inner, ",")
                    return self._prefer_str(items[0].strip()) if items else "Any"
                if head in ("List", "Set"):
                    elem = self._prefer_str(inner)
                    return f"{head}[{elem}]"
                if head == "Tuple":
                    elems = [self._prefer_str(p.strip()) for p in self._split_top_level(inner, ",")]
                    return f"Tuple[{', '.join(elems)}]"
                if head == "Dict":
                    kv = self._split_top_level(inner, ",")
                    k = self._prefer_str(kv[0].strip()) if kv else "Any"
                    v = self._prefer_str(kv[1].strip()) if len(kv) > 1 else "Any"
                    return f"Dict[{k}, {v}]"

        return s

    def _collapse_unions_str(self, s: str) -> str:
        s = s.strip().replace("typing.", "")
        if s.startswith("Union[") and s.endswith("]"):
            inner = s[len("Union["):-1]
            parts = [p.strip() for p in self._split_top_level(inner, ",")]
            return parts[0] if parts else "Any"
        if "|" in s:
            parts = [p.strip() for p in self._split_top_level(s, "|")]
            return parts[0] if parts else "Any"

        # containers
        for head in ("List", "Set", "Tuple", "Dict", "Annotated"):
            if s.startswith(head + "[") and s.endswith("]"):
                inner = s[len(head) + 1:-1]
                if head == "Annotated":
                    items = self._split_top_level(inner, ",")
                    return self._collapse_unions_str(items[0].strip()) if items else "Any"
                if head in ("List", "Set"):
                    elem = self._collapse_unions_str(inner)
                    return f"{head}[{elem}]"
                if head == "Tuple":
                    elems = [self._collapse_unions_str(p.strip()) for p in self._split_top_level(inner, ",")]
                    return f"Tuple[{', '.join(elems)}]"
                if head == "Dict":
                    kv = self._split_top_level(inner, ",")
                    k = self._collapse_unions_str(kv[0].strip()) if kv else "Any"
                    v = self._collapse_unions_str(kv[1].strip()) if len(kv) > 1 else "Any"
                    return f"Dict[{k}, {v}]"
        return s

    def _split_top_level(self, s: str, sep: str) -> list[str]:
        """
        Split `s` by single-char separator (',' or '|') at top level (not inside brackets).
        """
        out: list[str] = []
        buf: list[str] = []
        depth = 0
        for ch in s:
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
            if ch == sep and depth == 0:
                out.append("".join(buf).strip())
                buf = []
            else:
                buf.append(ch)
        out.append("".join(buf).strip())
        return [p for p in out if p != ""]


# ──────────────────────────────
# Stringification helpers (JSON dump)
# ──────────────────────────────
def type_repr(tp: Any) -> str:
    if isinstance(tp, str):
        return tp

    origin = get_origin(tp)
    args = get_args(tp)

    if origin is None:
        if isinstance(tp, type):
            return tp.__name__
        return str(tp).replace("typing.", "")

    if origin in _UNION_ORIGINS:
        return " | ".join(type_repr(a) for a in args)

    if origin is list:
        return f"List[{type_repr(args[0])}]" if args else "List[Any]"
    if origin is set:
        return f"Set[{type_repr(args[0])}]" if args else "Set[Any]"
    if origin is tuple:
        return "Tuple[" + ", ".join(type_repr(a) for a in args) + "]" if args else "Tuple"
    if origin is dict:
        k, v = args or (Any, Any)
        return f"Dict[{type_repr(k)}, {type_repr(v)}]"

    return str(tp).replace("typing.", "")


def schema_to_jsonable(schema: Schema) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for cls_name in sorted(schema.field_type_table):
        fields = schema.field_type_table[cls_name]
        out[cls_name] = {fname: type_repr(fields[fname]) for fname in sorted(fields)}
    return out


def schema_class(
    mapping: Dict[str, Any] | None = None,
    *,
    include_bases: bool = True,
    use_annotations: bool = True,
    use_init: bool = True,
    overwrite: bool = False,
    ignore: set[str] | None = None,
    toplevel: bool = False,
    toplevel_meta: Dict[str, Any] | None = None,
):
    """Decorator to register a class with SCHEMA at import time."""
    def deco(cls: type):
        SCHEMA.register_class(
            cls,
            mapping=mapping,
            include_bases=include_bases,
            use_annotations=use_annotations,
            use_init=use_init,
            overwrite=overwrite,
            ignore=ignore,
            toplevel=toplevel,
            toplevel_meta=toplevel_meta,
        )
        return cls
    return deco


# ──────────────────────────────
# Accept unknown kwargs (propagates to subclasses)
# ──────────────────────────────
def accept_extras(*, stash_attr: str = "_extras",
                  allow_only=None  # e.g., lambda cls: set(SCHEMA.get_all_extras(cls).keys())
                 ):
    """
    Wraps the class __init__ to swallow unknown kwargs, and propagates to subclasses.
    - If a subclass defines its own __init__, it gets wrapped automatically via __init_subclass__.
    - Unknown kwargs are attached as attributes, or stashed in `stash_attr` if __slots__ present.
    - If `allow_only` is provided (callable(cls) -> set[str]), only those keys are accepted.
    """
    WRAPPED_FLAG = "__extras_wrapped__"
    lock = threading.RLock()

    def _wrap_init(klass):
        with lock:
            if getattr(klass, WRAPPED_FLAG, False):
                return
            orig = klass.__init__
            sig = inspect.signature(orig)

            @functools.wraps(orig)
            def __init__(self, *args, **kwargs):
                # Split known from extras using THIS class's signature
                known = {}
                for name, p in sig.parameters.items():
                    if name == "self":
                        continue
                    if name in kwargs:
                        known[name] = kwargs.pop(name)

                # Call original with only known kwargs
                orig(self, *args, **known)

                # Filter extras if requested
                extras = kwargs
                if allow_only is not None:
                    allowed = set(allow_only(self.__class__) or ())
                    extras = {k: v for k, v in extras.items() if k in allowed}

                if extras:
                    if hasattr(self, "__slots__"):
                        stash = getattr(self, stash_attr, None)
                        if stash is None:
                            object.__setattr__(self, stash_attr, {})
                            stash = getattr(self, stash_attr)
                        stash.update(extras)
                    else:
                        for k, v in extras.items():
                            setattr(self, k, v)

            klass.__init__ = __init__
            setattr(klass, WRAPPED_FLAG, True)

    def _decorator(klass):
        # wrap the base class now
        _wrap_init(klass)

        # chain any existing __init_subclass__
        prev = getattr(klass, "__init_subclass__", None)
        prev_func = prev.__func__ if isinstance(prev, classmethod) else prev

        @classmethod
        def __init_subclass__(subcls, **kw):
            if prev_func:
                prev_func(**kw)  # call original
            _wrap_init(subcls)   # wrap subclass' __init__ too

        klass.__init_subclass__ = __init_subclass__  # propagate to future subclasses
        return klass

    return _decorator

def extensible(*, allow_only=None, **schema_kwargs):
    """
    Apply schema_class then accept_extras in the right order.
    Example: @extensible(toplevel=True)
    """
    def deco(cls):
        # 1) register class with schema (inner)
        cls = schema_class(**schema_kwargs)(cls)
        # 2) wrap for extras (outer) using an effective allow_only
        eff_allow = allow_only or (lambda c: set(SCHEMA.get_all_extras(c).keys()))
        cls = accept_extras(allow_only=eff_allow)(cls)
        return cls
    return deco

def extensible_dataclass(*d_args, allow_only=None, **schema_kwargs):
    from dataclasses import dataclass as _dc
    def deco(cls):
        cls = _dc(*d_args)(cls)                          # generate __init__
        cls = schema_class(**schema_kwargs)(cls)         # register with SCHEMA
        eff_allow = allow_only or (lambda c: set(SCHEMA.get_all_extras(c).keys()))
        cls = accept_extras(allow_only=eff_allow)(cls)   # wrap for extras
        return cls
    return deco

# put this in your schemas.py (or a shared helpers module)
import inspect

class ExtrasAwareMeta(type):
    """
    Intercepts cls(*args, **kwargs) and ensures registered extras are accepted:
      - Only pass constructor-known kwargs into __init__
      - Allowed extras (from SCHEMA) are attached after construction
    """
    def __call__(cls, *args, **kwargs):
        # what extras are allowed for this class?
        allow_fn = getattr(cls, "__extras_allow__", None)
        allowed = set(allow_fn(cls)) if callable(allow_fn) else set(SCHEMA.get_all_extras(cls).keys())

        # inspect the CURRENT __init__ (dataclass/custom OK)
        try:
            sig = inspect.signature(cls.__init__)
        except (TypeError, ValueError):
            sig = None

        known = {}
        accepts_varkw = False
        if sig:
            accepts_varkw = any(p.kind == p.VAR_KEYWORD for p in sig.parameters.values())
            for name, p in sig.parameters.items():
                if name == "self" or p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
                    continue
                if name in kwargs:
                    known[name] = kwargs.pop(name)

        # call __init__: pass only known, and optionally extras if it already accepts **kwargs
        call_kwargs = {**known, **(kwargs if accepts_varkw else {})}
        obj = super().__call__(*args, **call_kwargs)

        # attach remaining extras that are allowed
        extras = {k: v for k, v in kwargs.items() if k in allowed}
        if extras:
            if hasattr(obj, "__slots__"):
                stash = getattr(obj, "_extras", None)
                if stash is None:
                    object.__setattr__(obj, "_extras", {})
                    stash = obj._extras
                stash.update(extras)
            else:
                for k, v in extras.items():
                    setattr(obj, k, v)
        return obj



# Singleton instance
SCHEMA = Schema()

# -------------
def fact_from_even_tag(even_value):
    from .fact import FactType
    gedcom_even_to_fact = {
        # Person Fact Types
        "ADOP": FactType.Adoption,
        "CHR": FactType.AdultChristening,
        "EVEN": FactType.Amnesty,  # and other FactTypes with no direct GEDCOM tag
        "BAPM": FactType.Baptism,
        "BARM": FactType.BarMitzvah,
        "BASM": FactType.BatMitzvah,
        "BIRT": FactType.Birth,
        "BIRT, CHR": FactType.Birth,
        "BLES": FactType.Blessing,
        "BURI": FactType.Burial,
        "CAST": FactType.Caste,
        "CENS": FactType.Census,
        "CIRC": FactType.Circumcision,
        "CONF": FactType.Confirmation,
        "CREM": FactType.Cremation,
        "DEAT": FactType.Death,
        "EDUC": FactType.Education,
        "EMIG": FactType.Emigration,
        "FCOM": FactType.FirstCommunion,
        "GRAD": FactType.Graduation,
        "IMMI": FactType.Immigration,
        "MIL": FactType.MilitaryService,
        "NATI": FactType.Nationality,
        "NATU": FactType.Naturalization,
        "OCCU": FactType.Occupation,
        "ORDN": FactType.Ordination,
        "DSCR": FactType.PhysicalDescription,
        "PROB": FactType.Probate,
        "PROP": FactType.Property,
        "RELI": FactType.Religion,
        "RESI": FactType.Residence,
        "WILL": FactType.Will,

        # Couple Relationship Fact Types
        "ANUL": FactType.Annulment,
        "DIV": FactType.Divorce,
        "DIVF": FactType.DivorceFiling,
        "ENGA": FactType.Engagement,
        "MARR": FactType.Marriage,
        "MARB": FactType.MarriageBanns,
        "MARC": FactType.MarriageContract,
        "MARL": FactType.MarriageLicense,
        "SEPA": FactType.Separation,

        # Parent-Child Relationship Fact Types
        # (Note: Only ADOPTION has a direct GEDCOM tag, others are under "EVEN")
        "ADOP": FactType.AdoptiveParent
        }
    return gedcom_even_to_fact.get(even_value,None)

def event_from_even_tag(even_value): 
    from .event import EventType
    gedcom_even_to_evnt = {
        # Person Fact Types
        "ADOP": EventType.Adoption,
        "CHR": EventType.AdultChristening,
        "BAPM": EventType.Baptism,
        "BARM": EventType.BarMitzvah,
        "BASM": EventType.BatMitzvah,
        "BIRT": EventType.Birth,
        "BIRT, CHR": EventType.Birth,
        "BLES": EventType.Blessing,
        "BURI": EventType.Burial,
        
        "CENS": EventType.Census,
        "CIRC": EventType.Circumcision,
        "CONF": EventType.Confirmation,
        "CREM": EventType.Cremation,
        "DEAT": EventType.Death,
        "EDUC": EventType.Education,
        "EMIG": EventType.Emigration,
        "FCOM": EventType.FirstCommunion,
        
        "IMMI": EventType.Immigration,
        
        "NATU": EventType.Naturalization,
        
        "ORDN": EventType.Ordination,
        

        # Couple Relationship Fact Types
        "ANUL": EventType.Annulment,
        "DIV": EventType.Divorce,
        "DIVF": EventType.DivorceFiling,
        "ENGA": EventType.Engagement,
        "MARR": EventType.Marriage
        
    }
    return gedcom_even_to_evnt.get(even_value,None)