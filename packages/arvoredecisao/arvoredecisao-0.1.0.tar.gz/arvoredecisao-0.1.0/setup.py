from setuptools import setup, find_packages

setup(
    name="arvoredecisao",
    version="0.1.0",
    description="Implementações de ID3, C4.5 e CART do zero",
    author="Seu Nome",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
)
