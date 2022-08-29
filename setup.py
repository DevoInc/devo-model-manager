# coding: utf-8

"""
    Devo Model Manager API

    Devo API for machine learning  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: machine.learning@devo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "devo-model-manager"
VERSION = "1.8.7"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Devo Model Manager API",
    author_email="machine.learning@devo.com",
    url="",
    keywords=["Swagger", "Devo Model Manager API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test*"]),
    include_package_data=True,
    long_description="""\
    Devo API for machine learning  # noqa: E501
    """
)
