# -*- coding: utf-8 -*-
"""Installer for the redturtle.gritterize package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='redturtle.gritterize',
    version='0.9.0',
    description="Plone integration with Gritter",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Python',
    author='RedTurtle Technology',
    author_email='sviluppoplone@redturtle.it',
    url='http://pypi.python.org/pypi/redturtle.gritterize',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['redturtle'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone',
        'setuptools',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'flake8',
            'jarn.mkrelease',
            'niteoweb.loginas',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'zest.releaser',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
