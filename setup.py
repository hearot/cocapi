# A Python wrapper for the Clash of Clans API
# Copyright (C) 2019 Gabriel Hearot
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as file:
        long_description = file.read()
except Exception:
    long_description = ""

setuptools.setup(
    name="clashapi",
    version="1.0.0",
    author="Gabriel Hearot",
    author_email="gabriel@hearot.it",
    description="A Python wrapper for the Clash of Clans API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hearot/clashapi",
    install_requires=['requests'],
    keywords=['Clash of Clans', 'Supercell', 'API'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)
