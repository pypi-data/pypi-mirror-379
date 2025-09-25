from __future__ import annotations
import sqlite3
from struct import pack, unpack
from typing import Iterable, List, Optional, Sequence, Union
from sqlalchemy import Float, cast, event
from sqlalchemy.sql import func
from sqlalchemy.types import LargeBinary, TypeDecorator
from sqlalchemy.engine import Engine
import sqlite_vec
from sqlite_vec import serialize_float32, serialize_int8

def enable_sqlite_vec(engine: Engine):
    @event.listens_for(engine, "connect")
    def load_sqlite_vec_extension(dbapi_connection: sqlite3.Connection, connection_record):
        dbapi_connection.enable_load_extension(True)
        sqlite_vec.load(dbapi_connection)
        dbapi_connection.enable_load_extension(False)


VectorArg = Union[str, bytes, bytearray, memoryview, Sequence[float], Sequence[int]]


def _to_vector_text(value: Union[Sequence[float], Sequence[int]]) -> str:
    return "[" + ", ".join(str(float(v)) for v in value) + "]"


def _coerce_distance_arg(value: VectorArg) -> Union[str, bytes, memoryview, bytearray, None]:
    if value is None:
        return None
    if isinstance(value, (bytes, bytearray, memoryview)):
        return value
    if isinstance(value, str):
        return value
    return _to_vector_text(value)


class Vector(TypeDecorator):
    """
    SQLite vector type stored as BLOB for use with sqlite-vec extension.

    - Python -> DB: serialize sequence (float32 by default) or accept bytes as-is
    - DB -> Python: return bytes as-is
    - Comparators: l2_distance / cosine_distance / l1_distance map to
      vec_distance_* SQL functions
    """

    impl = LargeBinary
    cache_ok = True

    def __init__(self, dim: Optional[int] = None, *, dtype: str = "f32"):
        super().__init__()
        self.dim = dim
        self.dtype = dtype  # "f32" or "i8"

    def bind_processor(self, dialect):
        dim = self.dim
        dtype = self.dtype

        def process(value):
            if value is None:
                return None
            if isinstance(value, (bytes, bytearray, memoryview)):
                return value
            if isinstance(value, str) and value.startswith("[") and value.endswith("]"):
                try:
                    parts = [float(x.strip()) for x in value[1:-1].split(",") if x.strip()]
                except Exception:
                    parts = []
                if dim is not None and len(parts) != dim:
                    raise ValueError(f"expected {dim} dimensions, not {len(parts)}")
                if dtype == "f32":
                    return serialize_float32(parts)  # type: ignore[arg-type]
                return serialize_int8([int(round(p)) for p in parts])
            if isinstance(value, Iterable):
                as_list = list(value)
                if dim is not None and len(as_list) != dim:
                    raise ValueError(f"expected {dim} dimensions, not {len(as_list)}")
                if dtype == "f32":
                    return serialize_float32([float(v) for v in as_list])
                return serialize_int8([int(v) for v in as_list])
            return value

        return process

    def result_processor(self, dialect, coltype):
        dim = self.dim
        dtype = self.dtype

        def process(value):
            if value is None:
                return None
            if isinstance(value, (bytes, bytearray, memoryview)):
                raw = bytes(value)
                if dtype == "f32" and dim is not None:
                    expected_bytes = dim * 4
                    if len(raw) == expected_bytes:
                        return list(unpack(f"{dim}f", raw))
                if dtype == "i8":
                    length = dim if dim is not None else len(raw)
                    if len(raw) == length:
                        return list(unpack(f"{length}b", raw))
            return value

        return process

    class comparator_factory(TypeDecorator.Comparator):
        def l2_distance(self, other: VectorArg):
            return cast(func.vec_distance_L2(self.expr, _coerce_distance_arg(other)), Float)

        def cosine_distance(self, other: VectorArg):
            return cast(func.vec_distance_cosine(self.expr, _coerce_distance_arg(other)), Float)

        def l1_distance(self, other: VectorArg):
            return cast(func.vec_distance_L1(self.expr, _coerce_distance_arg(other)), Float)


def vec_distance_L2(column_or_expr, vector: VectorArg):
    return cast(func.vec_distance_L2(column_or_expr, _coerce_distance_arg(vector)), Float)


def vec_distance_cosine(column_or_expr, vector: VectorArg):
    return cast(func.vec_distance_cosine(column_or_expr, _coerce_distance_arg(vector)), Float)


def vec_distance_L1(column_or_expr, vector: VectorArg):
    return cast(func.vec_distance_L1(column_or_expr, _coerce_distance_arg(vector)), Float)


__all__ = [
    "Vector",
    "serialize_float32",
    "serialize_int8",
    "vec_distance_L2",
    "vec_distance_cosine",
    "vec_distance_L1",
    "enable_sqlite_vec",
]
