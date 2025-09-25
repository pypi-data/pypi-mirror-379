from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="pyast-remaked",
    version="0.1.1",
    author="slimeyyummy",
    author_email="zernokram@gmail.com",
    description="Extended Python AST library with parsing, transformation, and analysis tools",
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/slimeyyummy/pyast",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],  # add dependencies if any
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
