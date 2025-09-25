import ast
from dataclasses import dataclass
from pathlib import Path

from pypp_cli.do.transpile.transpile.calc_code.node import calc_code_for_main_file
from pypp_cli.do.transpile.transpile.z.results import TranspileResults
from pypp_cli.do.transpile.transpile.z.main_files.calc_includes import (
    calc_includes_for_main_file,
)
from pypp_cli.do.transpile.transpile.y.maps.d_types import Maps


@dataclass(frozen=True, slots=True)
class MainSingleFileTranspiler:
    _namespace: str
    _cpp_dest_dir: Path
    _py_modules: set[str]
    _lib_namespaces: dict[str, str]
    _maps: Maps
    _r: TranspileResults
    _file: Path
    _file_path: Path
    _py_ast: ast.Module

    def transpile(self):
        main_cpp_code = self._calc_cpp_code()
        self._write_cpp_file(main_cpp_code)

    def _calc_cpp_code(self) -> str:
        cpp_code_minus_includes, cpp_includes = calc_code_for_main_file(
            self._namespace,
            self._py_ast,
            self._maps,
            self._py_modules,
            self._lib_namespaces,
            self._file_path,
        )
        return calc_includes_for_main_file(cpp_includes) + cpp_code_minus_includes

    def _write_cpp_file(self, code: str):
        cpp_file_rel: Path = self._file.with_suffix(".cpp")
        cpp_file: Path = self._cpp_dest_dir / cpp_file_rel
        cpp_file.write_text(code)
        self._r.cpp_files_written += 1
        self._r.files_added_or_modified.append(cpp_file)
