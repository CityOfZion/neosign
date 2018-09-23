Utility for signing arbitrary messages with NEP2 Keypairs or WIF


* Compatible with Python 3.5+
* https://pypi.python.org/pypi/neosign




nep2 usage
----------

.. code-block:: console

    $ neosign abcabc -n
    [nep2 key]> ********************
    [nep2 key password]> ****************
    Signing With Address AWeZnH735EavQJKbJPC5F8fxutBnJFhukW
    pubkey, sig: 02029e81b26c573fd19af392fbb0187a0faf01e1a6ab54141699a1e19cf74738c3 1fbcbcc1dbd44af6dea843b84b10cb461925279c8b76cc389932c2463892aec1662fc940bbedc9a479cc6197acaddb3044c19242ee68629ce4199156a9a88fb2


wif usage
---------

.. code-block:: console

    $ neosign abcabc -w L447RbcX5FospWVCT9XkAZze2GG4xhgBhuZgtBrAJvTk5ZgeYcyB
    Signing With Address AWeZnH735EavQJKbJPC5F8fxutBnJFhukW
    pubkey, sig: 02029e81b26c573fd19af392fbb0187a0faf01e1a6ab54141699a1e19cf74738c3 1fbcbcc1dbd44af6dea843b84b10cb461925279c8b76cc389932c2463892aec1662fc940bbedc9a479cc6197acaddb3044c19242ee68629ce4199156a9a88fb2


pass input file
---------------

.. code-block:: console
    $ neosign --input myfile.txt -w L447RbcX5FospWVCT9XkAZze2GG4xhgBhuZgtBrAJvTk5ZgeYcyB
    Signing With Address AWeZnH735EavQJKbJPC5F8fxutBnJFhukW
    pubkey, sig: 02029e81b26c573fd19af392fbb0187a0faf01e1a6ab54141699a1e19cf74738c3 1fbcbcc1dbd44af6dea843b84b10cb461925279c8b76cc389932c2463892aec1662fc940bbedc9a479cc6197acaddb3044c19242ee68629ce4199156a9a88fb2


Getting started
---------------

You need Python 3.5 or higher!

You can install `neosign` from PyPI with ``easy_install`` or ``pip``:

.. code-block:: console

    $ pip install -U neosign

Alternatively, if you want to work on the code, clone this repository and setup your venv:

* Clone the repo: ``git clone https://github.com/CityOfZion/neosign.git``
* Create a Python 3 virtual environment and activate it:

.. code-block:: console

    $ python3 -m venv venv
    $ source venv/bin/activate

* Then install the requirements:

.. code-block:: console

    $ pip install -e .

