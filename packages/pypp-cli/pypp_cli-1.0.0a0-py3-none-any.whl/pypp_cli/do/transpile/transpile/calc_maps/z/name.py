from pypp_cli.do.transpile.transpile.y.d_types import (
    PyImp,
    AngInc,
    QInc,
)
from pypp_cli.do.transpile.transpile.y.maps.exceptions import (
    EXCEPTION_NAME_MAP,
)
from pypp_cli.do.transpile.transpile.y.maps.d_types import (
    ToStringEntry,
    NameMap,
)


NAME_MAP: NameMap = {
    "str": {None: ToStringEntry("pypp::PyStr", [QInc("py_str.h")])},
    # NOTE: technically I don't think this is necessary since int and int are the same
    "int": {None: ToStringEntry("int", [])},
    "float": {None: ToStringEntry("double", [])},
    "float32": {PyImp("pypp_python", "float32"): ToStringEntry("float", [])},
    "int8_t": {
        PyImp("pypp_python", "int8_t"): ToStringEntry(
            "int8_t",
            [AngInc("cstdint")],
        )
    },
    "int16_t": {
        PyImp("pypp_python", "int16_t"): ToStringEntry(
            "int16_t",
            [AngInc("cstdint")],
        )
    },
    "int32_t": {
        PyImp("pypp_python", "int32_t"): ToStringEntry(
            "int32_t",
            [AngInc("cstdint")],
        )
    },
    "int64_t": {
        PyImp("pypp_python", "int64_t"): ToStringEntry(
            "int64_t",
            [AngInc("cstdint")],
        )
    },
    "uint8_t": {
        PyImp("pypp_python", "uint8_t"): ToStringEntry("uint8_t", [AngInc("cstdint")])
    },
    "uint16_t": {
        PyImp("pypp_python", "uint16_t"): ToStringEntry("uint16_t", [AngInc("cstdint")])
    },
    "uint32_t": {
        PyImp("pypp_python", "uint32_t"): ToStringEntry("uint32_t", [AngInc("cstdint")])
    },
    "uint64_t": {
        PyImp("pypp_python", "uint64_t"): ToStringEntry("uint64_t", [AngInc("cstdint")])
    },
    "list": {None: ToStringEntry("pypp::PyList", [QInc("py_list.h")])},
    "dict": {None: ToStringEntry("pypp::PyDict", [QInc("py_dict.h")])},
    "defaultdict": {
        PyImp("pypp_python", "defaultdict"): ToStringEntry(
            "pypp::PyDefaultDict", [QInc("py_dict_default.h")]
        )
    },
    "tuple": {None: ToStringEntry("pypp::PyTup", [QInc("py_tuple.h")])},
    "set": {None: ToStringEntry("pypp::PySet", [QInc("py_set.h")])},
    "range": {None: ToStringEntry("pypp::PyRange", [QInc("py_range.h")])},
    "slice": {None: ToStringEntry("pypp::PySlice", [QInc("slice/py_slice.h")])},
    "enumerate": {None: ToStringEntry("pypp::PyEnumerate", [QInc("py_enumerate.h")])},
    "zip": {None: ToStringEntry("pypp::PyZip", [QInc("py_zip.h")])},
    "reversed": {None: ToStringEntry("pypp::PyReversed", [QInc("py_reversed.h")])},
    "Uni": {
        PyImp("pypp_python", "Uni"): ToStringEntry("pypp::Uni", [QInc("pypp_union.h")])
    },
    "Random": {
        PyImp("pypp_python.stl", "Random"): ToStringEntry(
            "pypp::random::Random", [QInc("pypp_random.h")]
        )
    },
    **EXCEPTION_NAME_MAP,
}
