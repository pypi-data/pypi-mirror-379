from setuptools import setup, find_packages

setup(
    name="universal-hotreload-python",
    version="0.1.0",
    description="Easy HotReload for Python projects",
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
