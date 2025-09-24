# StrictTypePython/types.py
import functools
class Types:
    DEBUG_TYPE_CHECK = True

    _builtin_types = (
        int, float, bool, str, list, dict, set, tuple,
        bytes, bytearray, memoryview, complex, frozenset, range
    )

    @staticmethod
    def _type_wrapper(func, new_allowed):
        # 원본 함수 기준
        origin = getattr(func, "__wrapped__", func)

        existing = getattr(origin, "_allowed_types", ())
        existing = existing if isinstance(existing, tuple) else (existing,)
        new_allowed = new_allowed if isinstance(new_allowed, tuple) else (new_allowed,)
        allowed = tuple(set(existing + new_allowed))

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not Types.DEBUG_TYPE_CHECK:
                return func(*args, **kwargs)

            result = func(*args, **kwargs)
            all_vals = list(args) + list(kwargs.values()) + [result]

            passed = any(isinstance(val, t) for val in all_vals for t in allowed)
            if not passed:
                raise TypeError(
                    f"{func.__name__} argument/return value is not allowed: "
                    f"args={args}, kwargs={kwargs}, return={result}"
                )
            return result

        # origin 기준으로 allowed 누적
        origin._allowed_types = allowed
        wrapper._allowed_types = allowed
        return wrapper

    # --- 단일 타입 ---
    @staticmethod
    def forceInt(func): return Types._type_wrapper(func, int)
    @staticmethod
    def forceFloat(func): return Types._type_wrapper(func, float)
    @staticmethod
    def forceBool(func): return Types._type_wrapper(func, bool)
    @staticmethod
    def forceStr(func): return Types._type_wrapper(func, str)
    @staticmethod
    def forceList(func): return Types._type_wrapper(func, list)
    @staticmethod
    def forceDict(func): return Types._type_wrapper(func, dict)
    @staticmethod
    def forceSet(func): return Types._type_wrapper(func, set)
    @staticmethod
    def forceTuple(func): return Types._type_wrapper(func, tuple)
    @staticmethod
    def forceBytes(func): return Types._type_wrapper(func, bytes)
    @staticmethod
    def forceByteArray(func): return Types._type_wrapper(func, bytearray)
    @staticmethod
    def forceMemoryView(func): return Types._type_wrapper(func, memoryview)
    @staticmethod
    def forceComplex(func): return Types._type_wrapper(func, complex)
    @staticmethod
    def forceFrozenSet(func): return Types._type_wrapper(func, frozenset)
    @staticmethod
    def forceRange(func): return Types._type_wrapper(func, range)

    # 축약형
    Int = forceInt
    Float = forceFloat
    Bool = forceBool
    Str = forceStr
    List = forceList
    Dict = forceDict
    Set = forceSet
    Tuple = forceTuple
    Bytes = forceBytes
    ByteArray = forceByteArray
    MemoryView = forceMemoryView
    Complex = forceComplex
    FrozenSet = forceFrozenSet
    Range = forceRange

    # --- Union 타입 ---
    @staticmethod
    def forceUnion(types):
        def decorator(func):
            return Types._type_wrapper(func, types)
        return decorator

    # --- remain_forceTypeCheck ---
    @staticmethod
    def remain_forceTypeCheck(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            allowed = getattr(func, "_allowed_types", Types._builtin_types)
            passed = any(isinstance(val, t) for val in args + tuple(kwargs.values()) for t in allowed)
            if not passed:
                passed = any(isinstance(result, t) for t in allowed)
            if not passed:
                raise TypeError(
                    f"{func.__name__} argument/return value is not allowed: "
                    f"args={args}, kwargs={kwargs}, return={result}"
                )
            return result
        return wrapper
