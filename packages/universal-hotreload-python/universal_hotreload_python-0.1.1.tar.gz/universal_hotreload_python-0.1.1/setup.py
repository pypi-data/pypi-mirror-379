from setuptools import setup, find_packages
from pathlib import Path

# README einlesen
this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="universal-hotreload-python",
    version="0.1.1",
    description="Easy HotReload for Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="naXan",
    python_requires=">=3.10",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "watchdog>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "hotreload=HotReload.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
