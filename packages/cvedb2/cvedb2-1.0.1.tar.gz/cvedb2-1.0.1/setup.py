import os
from setuptools import setup, find_packages

SETUP_DIR = os.path.dirname(os.path.realpath(__file__))
README_PATH = os.path.join(SETUP_DIR, "README.md")

with open(README_PATH, "r") as readme:
    README = readme.read()

setup(
    name="cvedb2",
    description="Yet another CVE database",
    long_description=README,
    long_description_content_type="text/markdown",
    license="LGPL-3.0-or-later",
    url="https://github.com/ahntenna/cvedb2",
    author="ahntenna",
    version="1.0.1",
    packages=find_packages(exclude=["test"]),
    python_requires=">=3.6",
    install_requires=[
        "cvss>=3.6",
        # dataclasses were added in Python 3.7, so use this backport for earlier versions of Python
        "dataclasses;python_version<'3.7'",
        "python-dateutil>=2.8.1",
        "tqdm==4.66.3"
    ],
    package_data={
        "cvedb2": ["data/*.json.gz", "data/*.meta"]
    },
    extras_require={
        "dev": ["flake8", "pytest", "rstr~=2.2.6", "twine"]
    },
    entry_points={
        "console_scripts": [
            "cvedb2 = cvedb2.__main__:main"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities"
    ]
)
