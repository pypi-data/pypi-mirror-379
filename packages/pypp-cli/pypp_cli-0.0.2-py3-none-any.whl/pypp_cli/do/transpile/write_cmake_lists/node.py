from dataclasses import dataclass
from pathlib import Path

from pypp_cli.do.transpile.find_libs.z.find_all_libs import PyppLibs
from pypp_cli.do.transpile.y.transpiler_config_models import (
    TranspilerConfigModelsDict,
)
from pypp_cli.do.transpile.y.py_file_tracker import PyFilesTracker


def _calc_link_libs_lines(link_libs: list[str]) -> list[str]:
    # target_link_libraries(pypp_common PUBLIC glfw)
    if len(link_libs) == 0:
        return []
    return [
        "target_link_libraries(",
        "    pypp_common PUBLIC",
        *[f"    {lib}" for lib in link_libs],
        ")",
    ]


@dataclass(frozen=True, slots=True)
class CMakeListsWriter:
    _cpp_dir: Path
    _libs: PyppLibs
    _cmake_minimum_required_version: str
    _py_files_tracker: PyFilesTracker
    _transpiler_config_models: TranspilerConfigModelsDict

    def write(self):
        main_files, src_files = self._calc_main_and_src_files()
        add_lines, link_libs = self._calc_add_lines_and_link_libs_from_libraries()
        cmake_lines = [
            f"cmake_minimum_required(VERSION {self._cmake_minimum_required_version})",
            "set(CMAKE_CXX_COMPILER clang++)",
            "set(CMAKE_C_COMPILER clang)",
            "project(pypp LANGUAGES C CXX)",
            "",
            "set(CMAKE_CXX_STANDARD 23)",
            "set(CMAKE_EXPORT_COMPILE_COMMANDS ON)",
            "",
            *add_lines,
            "",
            "set(SRC_FILES",
            *src_files,
            ")",
            "file(GLOB_RECURSE pypp_FILES pypp/*.cpp)",
            "file(GLOB_RECURSE LIB_FILES libs/*.cpp)",
            "",
            "add_library(",
            "    pypp_common STATIC",
            "    ${SRC_FILES}",
            "    ${pypp_FILES}",
            "    ${LIB_FILES}",
            ")",
            "target_include_directories(",
            "    pypp_common PUBLIC",
            "    ${CMAKE_SOURCE_DIR}",
            "    ${CMAKE_SOURCE_DIR}/pypp",
            "    ${CMAKE_SOURCE_DIR}/libs",
            ")",
            *_calc_link_libs_lines(link_libs),
            "",
        ]

        for py_file in main_files:
            exe_name = py_file.stem
            cmake_lines.append(f"add_executable({exe_name} {exe_name}.cpp)")
            cmake_lines.append(f"target_link_libraries({exe_name} PRIVATE pypp_common)")
            cmake_lines.append("")

        cmake_content = "\n".join(cmake_lines)

        cmake_path: Path = self._cpp_dir / "CMakeLists.txt"
        cmake_path.write_text(cmake_content)

        print("CMakeLists.txt generated to cpp project directory")

    def _calc_main_and_src_files(self) -> tuple[list[Path], list[str]]:
        main_files: list[Path] = []
        src_files: list[str] = []
        for f in self._py_files_tracker.all_files:
            if f.name == "__init__.py":
                continue
            if f in self._py_files_tracker.main_files:
                main_files.append(f)
            else:
                # replace stem with cpp
                cpp_file: Path = f.with_suffix(".cpp")
                if (self._cpp_dir / cpp_file).exists():
                    src_files.append(cpp_file.as_posix())
        return main_files, src_files

    def _calc_add_lines_and_link_libs_from_libraries(
        self,
    ) -> tuple[list[str], list[str]]:
        add_lines: list[str] = []
        link_libs: list[str] = []
        for v in self._transpiler_config_models.values():
            if v.models.cmake_lists is not None:
                if v.models.cmake_lists.add_lines is not None:
                    add_lines.extend(v.models.cmake_lists.add_lines)
                if v.models.cmake_lists.link_libraries is not None:
                    link_libs.extend(v.models.cmake_lists.link_libraries)
        return add_lines, link_libs
