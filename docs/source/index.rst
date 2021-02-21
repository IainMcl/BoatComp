.. boatcomp documentation master file, created by
   sphinx-quickstart on Tue Feb 16 19:25:41 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to boatcomp's documentation!
====================================

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

.. note::
   Full documentation is not available at the moment due to using python 3.9 
   features. Python 3.9 is not currently supported by readthedocs for 
   docstring documentation, but will hopefully be updated soon.

.. toctree::
   :maxdepth: 2
   :caption: User guide

   installation
   contributing

.. toctree::
   :maxdepth: 2
   :caption: Settings and configuration

   settings

.. toctree::
   :maxdepth: 2
   :caption: Modules

   modules

.. toctree::
   :maxdepth: 2
   :caption: Models

   models

.. toctree::
   :maxdepth: 2
   :caption: Database

   database

.. toctree::
   :maxdepth: 2
   :caption: Api

   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
