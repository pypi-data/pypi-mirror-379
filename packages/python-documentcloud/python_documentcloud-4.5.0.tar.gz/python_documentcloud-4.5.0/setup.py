# Third Party
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="python-documentcloud",
    version="4.5.0",
    description="A simple Python wrapper for the DocumentCloud API",
    author="Mitchell Kotler",
    author_email="mitch@muckrock.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muckrock/python-documentcloud",
    license="MIT",
    packages=("documentcloud",),
    include_package_data=True,
    install_requires=(
        "future",
        "listcrunch>=1.0.1",
        "python-dateutil",
        "ratelimit",
        "requests",
        "urllib3",
        "pyyaml",
        "fastjsonschema",
        "python-squarelet",
    ),
    extras_require={
        "dev": [
            "black",
            "coverage",
            "isort",
            "pylint",
            "sphinx",
            "twine",
        ],
        "test": [
            "pytest",
            "pytest-mock",
            "pytest-recording",
            "vcrpy",
        ],
    },
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
    ),
)
