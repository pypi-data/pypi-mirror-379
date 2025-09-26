from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.build import build
import os
import subprocess
import sys
import shutil


_entrypoint_name = "entrypoint.py"
_binary_name = "njoy"
_lib_name = "libnjoy.a"

class CMakeBuild(build_ext):
    def run(self):
        build_directory = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "build"
        )
        os.makedirs(build_directory, exist_ok=True)

        subprocess.check_call(
            [
                "cmake",
                "-DCMAKE_BUILD_TYPE=Release",
                "-Dstatic_libraries=ON",
                "-Dstatic_njoy=ON",
                "-DCMAKE_EXE_LINKER_FLAGS=-static",
                "../njoy",
            ],
            cwd=build_directory,
        )

        subprocess.check_call(["make", "-j8"], cwd=build_directory)

        ep_directory  = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'njoy')
        bin_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'njoy', 'bin')
        lib_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'njoy', 'lib')
        os.makedirs(bin_directory, exist_ok=True)
        os.makedirs(lib_directory, exist_ok=True)
        binary_dest = os.path.join(bin_directory, _binary_name)
        lib_dest = os.path.join(lib_directory, _lib_name)
        ep_dest = os.path.join(ep_directory, _entrypoint_name)

        binary_src = os.path.join(build_directory, _binary_name)
        lib_src = os.path.join(build_directory, _lib_name)

        shutil.copy(binary_src, binary_dest)
        os.chmod(binary_dest, 0o755)
        shutil.copy(lib_src, lib_dest)

        # entrypoint
        shutil.copy(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), _entrypoint_name
        ), ep_dest)


class CustomBuild(build):
    def run(self):
        # Build the extension before building the package
        self.run_command('build_ext')
        # Now call the original build command of setuptools
        super().run()

setup(
    name="NJOY",
    version="2016.78",
    description="The NJOY Nuclear Data Processing System is a modular computer code designed to read evaluated data in ENDF format, transform the data in various ways, and output the results as libraries designed to be used in various applications from LANL.",
    packages=["njoy"],
    include_package_data=True,
    install_requires=[],
    cmdclass={
        "build_ext": CMakeBuild,
        'build': CustomBuild,
    },
    entry_points={
        'console_scripts': [
            'njoy = njoy.entrypoint:main',
        ],
    },
    classifiers=[
        'Programming Language :: Fortran',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.7',
)
