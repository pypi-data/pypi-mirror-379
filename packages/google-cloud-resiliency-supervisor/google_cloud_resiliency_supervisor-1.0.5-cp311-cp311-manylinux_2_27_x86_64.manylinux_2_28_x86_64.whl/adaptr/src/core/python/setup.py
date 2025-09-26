from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
import subprocess
import sys
import distutils.dir_util
import os


class BazelBuildExt(build_ext):
    def run(self):
        # Set PYTHON_BIN_PATH based on the current Python executable
        python_path = sys.executable
        os.environ["PYTHON_BIN_PATH"] = python_path

        print(f"Using Python at {python_path} for Bazel builds")

        subprocess.check_call(
            [
                "bazel",
                "build",
                "-c",
                "opt",
                "//adaptr/src/core/cc:adaptr_core.so",
                "--repo_env",
                f"PYTHON_BIN_PATH={python_path}",
            ]
        )

        # Ensure the build directory exists
        self.build_temp = self.build_temp or "build"
        distutils.dir_util.mkpath(self.build_temp)

        # Copy the built library to the build directory
        built_lib_path = os.path.join(
            "bazel-bin", "adaptr", "src", "core", "cc", "adaptr_core.so"
        )
        target_lib_path = self.get_ext_fullpath("adaptr_core")
        os.makedirs(os.path.dirname(target_lib_path), exist_ok=True)
        subprocess.check_call(["cp", built_lib_path, target_lib_path])


setup(
    name="adaptr",
    version="0.1.0",
    author="The adapTr team",
    author_email="adaptr-core@google.com",
    description="adapTr",
    # long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    ext_modules=[Extension("adaptr", sources=[])],
    cmdclass={"build_ext": BazelBuildExt},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
