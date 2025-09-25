#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import re

with open('cool_qrcode/__init__.py', 'r', encoding='utf-8') as f:
    version = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read()).group(1)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

    # Allow the build environment to specify which branch to use for
    # generating absolute URLs (useful for PyPI rendering). Default to
    # 'master' for this repository; CI can override via DOCS_BRANCH.
    branch = os.environ.get('DOCS_BRANCH', 'master')

    # Replace repo-relative image paths with raw.githubusercontent URLs
    # that reference the configured branch so PyPI can fetch them.
    readme = readme.replace(
        "](docs/images/",
        f"](https://raw.githubusercontent.com/xxk59/cool-qrcode/{branch}/docs/images/",
    )

    # Also normalize any blob/main links to use the configured branch.
    readme = readme.replace(
        "github.com/xxk59/cool-qrcode/blob/main/",
        f"github.com/xxk59/cool-qrcode/blob/{branch}/",
    )

setup(
    name='cool-qrcode',
    version=version,
    description='一个用于生成个性化二维码的Python库',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Kelvin Xu',
    author_email='xxk59@hotmail.com',
    url='https://github.com/xxk59/cool-qrcode',
    packages=find_packages(),
    install_requires=[
        'Pillow>=9.0.0',
        'qrcode>=7.0.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='qrcode, qr, cool-qrcode, 二维码',
    python_requires='>=3.7',
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'black>=22.0.0',
            'isort>=5.0.0',
        ],
    },
) 