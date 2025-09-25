from pypp_cli.do.transpile.transpile.y.d_types import PyImp
from pypp_cli.do.transpile.transpile.y.maps.d_types import FnArgByValueMap

PRIMITIVE_TYPES: FnArgByValueMap = {
    "int": {None},
    "double": {None},  # python float
    "bool": {None},
    "float": {PyImp("pypp_python", "float32")},  # python float32
    "int8_t": {PyImp("pypp_python", "int8_t")},
    "int16_t": {PyImp("pypp_python", "int16_t")},
    "int32_t": {PyImp("pypp_python", "int32_t")},
    "int64_t": {PyImp("pypp_python", "int64_t")},
    "uint8_t": {PyImp("pypp_python", "uint8_t")},
    "uint16_t": {PyImp("pypp_python", "uint16_t")},
    "uint32_t": {PyImp("pypp_python", "uint32_t")},
    "uint64_t": {PyImp("pypp_python", "uint64_t")},
}
