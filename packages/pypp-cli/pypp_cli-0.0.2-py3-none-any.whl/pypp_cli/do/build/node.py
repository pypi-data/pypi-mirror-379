from pathlib import Path
import subprocess
import shutil


def pypp_build(cpp_dir: Path):
    print("running cmake build...")
    # NOTE: you only need to do the first 'cmake -S . -B build' part if there was file
    #  changes to the code base. However, for simplicity, I will just do it each time.
    # cmake -S . -B build
    # Note: The first cmake command you wana do is something like:
    # cmake -S . -B build -G "Ninja" -DCMAKE_C_COMPILER=clang
    # -DCMAKE_CXX_COMPILER=clang++
    # cmake -S . -B build -G "Ninja" -DCMAKE_C_COMPILER=clang
    # -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE=Release
    # because this sets up the build system to use the clang compiler.
    if shutil.which("cmake") is None:
        raise RuntimeError(
            "cmake not found. To use pypp, install cmake and ensure it is in your PATH."
        )
    # cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
    subprocess.check_call(
        [
            "cmake",
            "-S",
            ".",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_C_COMPILER=clang",
            "-DCMAKE_CXX_COMPILER=clang++",
            "-DCMAKE_BUILD_TYPE=Release",
        ],
        cwd=cpp_dir,
    )
    # cmake --build build --config Release
    subprocess.check_call(
        ["cmake", "--build", "build", "--config", "Release"],
        cwd=cpp_dir,
    )
    print("cmake build finished")
