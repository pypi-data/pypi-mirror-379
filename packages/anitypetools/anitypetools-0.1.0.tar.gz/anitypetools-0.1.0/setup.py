from setuptools import setup, find_packages

setup(
    name="anitypetools",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ant=ant_cli.__main__:main",
        ],
    },
    python_requires=">=3.7",
)
