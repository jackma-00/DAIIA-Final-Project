"""Package setup"""
from setuptools import setup, find_packages

setup(
    name="auction",
    version="0.1.0",
    author="Jacopo Maragna and Abdelrahman Saleh",
    description="LLM-based auction",
    packages=find_packages(),
    install_requires=[
        "pyautogen",
    ],
    extras_require={
        "dev": [
            "black==23.1.0",
            "pylint==2.17.0",
            "pytest==7.3.1",
        ]
    },
)
