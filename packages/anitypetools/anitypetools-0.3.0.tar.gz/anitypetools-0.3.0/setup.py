from setuptools import setup, find_packages

setup(
    name="anitypetools",
    version="0.3.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ant=ant_cli.__main__:main",
        ],
    },
    python_requires=">=3.7",
    install_requires=[
        "colorama>=0.4.6",
        "m3u8>=3.6.0",
    ]
)
