Utility for signing arbitrary messages with NEP2 Keypairs or WIF


* Compatible with Python 3.5+
* https://pypi.python.org/pypi/neosign

``neosign`` examples:

.. code-block:: console

    $ neosign -h
    usage: np-sign [-h] [-n] [--wif WIF] message

    A utility for signing messages. Example usage: "neosign myhexmessage -w MYWIF"

    positional arguments:
      message               The message in string format to be signed

    optional arguments:
      -h, --help            show this help message and exit
      -n, --nep2            Whether to use an NEP2 passhrase
      -w, --wif             If using a wif pass in the wif



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

