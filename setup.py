#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: stdrickforce (Tengyuan Fan)
# Email:  <stdrickforce@gmail.com> <fantengyuan@baixing.com>

from setuptools import (
    setup,
    find_packages,
)

entry_points = {
    'console_scripts': [
    ],
}

setup(
    name="s2m",
    version="1.0",
    description=u"国服魔兽世界大秘境天梯分析工具",
    long_description='',
    author="stdrickforce",
    author_email="fantengyuan@baixing.com",
    url='https://github.com/stdrickforce/s2m',
    package_data={},
    entry_points=entry_points,
    packages=find_packages(),
    install_requires=[
        "Scrapy==1.2.1",
    ],
)
