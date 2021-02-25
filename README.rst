========
Boatcomp
========

|docs| |build|

Boatcomp aims to provide high level racing insights to the average racer. 

The aim is to provide minimal setup and automate as many decisions as possible 
so the racer can focus on making their boat go as fast as possible.

Aims 
-----

- Connect to GPS module to receive location data. This will be used as a less
  accurate Speed Over Ground (SOG) sensor as well as a Course Over Ground (COG)
  sensor.

- Think about ways to connect to boat instruments. Use this for Speed, Wind 
  Speed (WS), Depth etc.

- Use GPS to be able to ping locations of racing marks.

- Infer the location of racing marks from GPS track to allow for race insights 
  on next leg.

- Track speed and angle to generate boat performance targets.

- If wind data available. Provide sail selection information from previous race
  wind information - Last race avg, min max; Last 5 minute avg, min, max; 
  Current 3s average.

- Provide a graphql api to be able to interface with the data and display.

- A web view front end to display boat information and useful data.

 **Note**
   Full documentation is not available at the moment due to using python 3.9 
   features. Python 3.9 is not currently supported by readthedocs for 
   docstring documentation, but will hopefully be updated soon.

Installation
------------

Install package with pip
------------------------

To install with pip::

  $ pip install boatcomp # Coming soon

Install from source
-------------------

To install boatcomp from the latest source from `GitHub <https://github.com/IainMcl/BoatComp>`_::

  $ git clone https://github.com/IainMcl/BoatComp 
  $ cd BoatComp

then install with pip::

  $ pip install .

or for development::

  $ pip install -e .[dev]

or for documentation development::

  $ pip install -e .[doc]

Dependencies
------------

All of the following are for base dependencies. A full list of installed 
dependencies i.e. the result of :code:`$ pip freeze` can be found in 
`requirements-all.txt <https://github.com/IainMcl/BoatComp/blob/main/requirements-all.txt>`_.

.. |docs| image:: https://readthedocs.org/projects/docs/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://docs.readthedocs.io/en/latest/?badge=latest

.. |build| image:: https://github.com/IainMcl/BoatComp/actions/workflows/boatcompbuild.yml/badge.svgg
    :alt: Build Status
    :scale: 100%
    :target: https://github.com/IainMcl/BoatComp/actions/workflows/boatcompbuild.yml/badge.svgg
