from setuptools import setup

setup(
    name="python-dropbox-cli",
    version="0.1",
    py_modules=["python_dropbox_cli", "main"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "python-dropbox-cli=python_dropbox_cli:cli",
        ],
    }
)
