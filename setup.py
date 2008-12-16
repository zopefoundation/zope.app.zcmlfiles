##############################################################################
#
# Copyright (c) 2006, 2007 Zope Corporation and Contributors.
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
"""Setup for zope.app.zcmlfiles package

$Id$
"""

import os

from setuptools import setup, find_packages, Extension

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '========'
    )

setup(
    name='zope.app.zcmlfiles',
    version='3.5.0',
    url='http://pypi.python.org/pypi/zope.app.zcmlfiles',
    author='Zope Corporation and Contributors',
    author_email='zope-dev@zope.org',
    license='ZPL 2.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Framework :: Zope3',
        ],
    description='Zope application server ZCML files',
    long_description=long_description,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope', 'zope.app'],
    include_package_data=True,
    install_requires=['setuptools',
                      'zope.component',
                      'zope.annotation',
                      'zope.app.dependable',
                      'zope.app.content',
                      'zope.publisher',
                      'zope.app.component',
                      'zope.app.generations',
                      'zope.app.interface',
                      'zope.app.publisher',
                      'zope.app.security',
                      'zope.app.form',
                      'zope.app.i18n',
                      'zope.app.locales',
                      'zope.app.zopeappgenerations',
                      'zope.app.principalannotation',
                      'zope.app.basicskin',
                      'zope.app.rotterdam',
                      'zope.app.wsgi',
                      'zope.formlib',
                      'zope.i18n',
                      'zope.app.pagetemplate',
                      'zope.app.schema',
                      'zope.app.container',
                      ],
    zip_safe=False,
    )
