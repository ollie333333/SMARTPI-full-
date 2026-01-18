from setuptools import setup, find_packages

setup(
    name="smartpi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "smartpi-chat=smartpi.gui:run_gui"
        ],
    },
)
