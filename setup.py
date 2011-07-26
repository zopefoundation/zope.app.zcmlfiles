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

from setuptools import setup, find_packages

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
    version='3.7.1',
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
        extras_require = dict(
        test=['zope.app.testing',
              ]),
    install_requires=['setuptools',
                      'zope.annotation',
                      'zope.component',
                      'zope.componentvocabulary',
                      'zope.copypastemove',
                      'zope.dublincore',
                      'zope.formlib',
                      'zope.i18n',
                      'zope.location',
                      'zope.publisher',
                      'zope.size',
                      'zope.traversing',
                      'zope.app.applicationcontrol',
                      'zope.app.appsetup',
                      'zope.app.basicskin',
                      'zope.app.broken',
                      'zope.app.component',
                      'zope.app.container',
                      'zope.app.content',
                      'zope.app.dependable',
                      'zope.app.error',
                      'zope.app.exception',
                      'zope.app.folder',
                      'zope.app.form',
                      'zope.app.generations',
                      'zope.app.http',
                      'zope.app.i18n',
                      'zope.app.locales >= 3.6.0',
                      'zope.app.pagetemplate',
                      'zope.app.principalannotation',
                      'zope.app.publication',
                      'zope.app.publisher',
                      'zope.app.rotterdam',
                      'zope.app.schema',
                      'zope.app.security',
                      'zope.app.wsgi',
                      'zope.app.zopeappgenerations',
                      ],
    zip_safe=False,
    )
