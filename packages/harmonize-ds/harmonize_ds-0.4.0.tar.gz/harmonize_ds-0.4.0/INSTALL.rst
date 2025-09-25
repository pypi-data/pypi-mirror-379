..
    This file is part of Python Client Library for Harmonize Datasources.
    Copyright (C) 2025 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.


Installation
============

Please, read the instructions below in order to install ``harmonize_ds``.

Production Installation
------------------------

Install via pypi::

    pip install harmonize-ds


Development Installation
------------------------

Clone the Software Repository::

    git clone https://github.com/Harmonize-Brazil/harmonize-ds.git


Go to the source code folder::

    cd harmonize_ds


Install in development mode::

    pip3 install -e .[all]


.. note::

    If you want to create a new *Python Virtual Environment*, please, follow this instruction:

    *1.* Create a new virtual environment linked to Python 3.11::

        python3.11 -m venv venv


    **2.** Activate the new environment::

        source venv/bin/activate


    **3.** Update pip and setuptools::

        pip3 install --upgrade pip setuptools wheel


Run the Tests
+++++++++++++

Run the tests::

    ./run-test.sh

Build the Documentation
+++++++++++++++++++++++

You can generate the documentation based on Sphinx with the following command::

    sphinx-build docs/sphinx docs/sphinx/_build/html


The above command will generate the documentation in HTML and it will place it under::

    docs/sphinx/_build/html/


You can open the above documentation in your favorite browser, as::

    firefox docs/sphinx/_build/html/index.html
