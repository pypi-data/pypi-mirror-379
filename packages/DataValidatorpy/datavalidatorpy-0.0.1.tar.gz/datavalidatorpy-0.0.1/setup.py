from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="DataValidatorpy",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Gerardo Burgos",
    description="una lbreria para validar datos personales y de contacto",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gerarb1/pg2_parcial3.git",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)