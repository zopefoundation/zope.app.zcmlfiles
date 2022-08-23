##############################################################################
#
# Copyright (c) 2006, 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.app.zcmlfiles package
"""

import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.rst')
)

setup(
    name='zope.app.zcmlfiles',
    version='4.1.0',
    url='http://github.com/zopefoundation/zope.app.zcmlfiles',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    license='ZPL 2.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Framework :: Zope :: 3',
    ],
    description='Zope application server ZCML files',
    long_description=long_description,
    keywords="zope setup configuration standard menu",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope', 'zope.app'],
    include_package_data=True,
    extras_require={
        'test': [
            'webtest',
            'zope.testing',
            'zope.testrunner',
        ],
    },
    install_requires=[
        'setuptools',
        'zope.annotation >= 4.4.1',
        'zope.component >= 4.3.0',
        'zope.componentvocabulary >= 2.0.0',
        'zope.copypastemove >= 4.0.0',
        'zope.dublincore >= 4.1.1',
        'zope.formlib >= 4.3.0',
        'zope.i18n >= 4.2.0',
        'zope.location >= 4.0.3',
        'zope.publisher >= 4.3.2',
        'zope.size >= 4.1.0',
        'zope.traversing >= 4.1.0',
        'zope.app.applicationcontrol >= 4.0.0',
        'zope.app.appsetup >= 4.0.0',
        'zope.app.basicskin >= 4.0.0',
        'zope.app.broken >= 4.0.0',
        'zope.app.component >= 4.0.0',
        'zope.app.container >= 4.0.0',
        'zope.app.content >= 4.0.0',
        'zope.app.dependable >= 4.0.0',
        'zope.app.error >= 4.0.0',
        'zope.app.exception >= 4.0.1',
        'zope.app.folder >= 4.0.0',
        'zope.app.form >= 5.0.0',
        'zope.app.generations >= 4.0.0',
        'zope.app.http >= 4.0.1',
        'zope.app.i18n >= 4.0.0',
        'zope.app.locales >= 4.0.0',
        'zope.app.pagetemplate >= 4.0.0',
        'zope.app.principalannotation >= 4.0.0',
        'zope.app.publication >= 4.2.1',
        'zope.app.publisher >= 4.0.0',
        'zope.app.rotterdam >= 4.0.0',
        'zope.app.schema >= 4.1.0',
        'zope.app.security >= 4.0.0',
        'zope.app.wsgi >= 4.1.0',
    ],
    zip_safe=False,
)
