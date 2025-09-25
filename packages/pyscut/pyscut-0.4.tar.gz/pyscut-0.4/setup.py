from setuptools import setup, find_packages

setup(
    name="pyscut",
    version="0.4",
    packages=find_packages(),
    install_requires=[
        "pywin32"
    ],
    entry_points={
        "console_scripts": [
            "pyscut = pyscut:createDesktopShortcut "
        ]
    }
)

# Run python setup.py sdist bdist_wheel