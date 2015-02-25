EnergiStream
************

EnergiStream is an open source Python client for interacting with EnergiStream API, from MelRok.

Installation
^^^^^^^^^^^^

To install EnergiStream from source, clone the git repository to your local machine ::

  $ git clone git@github.com:melrok/energistream-py.git

In the :code:`energistream` root directory (same one where you found this file after cloning the git repo), execute ::

  $ sudo pip install -e .

Dependencies
^^^^^^^^^^^^

EnergiStream has a few key dependancies:

* `pandas <http://pandas.pydata.org/>`__: >= 0.14.1
* `requests <http://docs.python-requests.org/>`__: >= 1.2.3
* `testfixtures <https://pythonhosted.org/testfixtures/>`__

All requirements are specified in the `requirements.txt`. One can attempt to install these alongside the `EnergiStream` installation via ::

  $ sudo pip install -r requirements.txt -e .

EnergiStream Guide
******************

A quick guide to some of the core EnergiStream functionality. Examples and additional documentation are available at `GitHub Pages <http://melrok.github.io/energistream-py/>`__.

**Note** : Always refer to the doctrings for all methods for a detailed summary of functionality.

Importing
^^^^^^^^^

To import the energistream library :

.. code:: python

  import energistream as es


Client Instantiation and Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:code:`EnergiStreamClient` takes a valid username and password and establishes a unique session with temporary credentials.

.. code:: python

  stream = es.EnergiStreamClient('UCI_Admin', 'UCI_Admin', include_sensors=True)

:code:`authenticate` uses the user credentials to authenticate the instantiated client in the event that authentication was not previously established or has lapsed.

.. code:: python

  stream.authenticate

The :code:`is_authenticated` method returns a simple boolean true or false when asked if the client authentication is still valid.

.. code:: python

  stream.is_authenticated

External Data
^^^^^^^^^^^^^

The :code:`get_weather` method returns a dataframe of hourly temperature and relative humidity data for the instantiated client's associated physical location.

**Note**: This data is collected from third party sources. Weather ID is an energistream unique key and not associated to any third party ID schema.

.. code:: python

  stream.get_weather(weather_id = 102, start = '12/29/2014', end = '1/29/2015')

Energistream Data and Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :code:`get_energy` method accepts a sensor ID and returns a dataframe relating active and reactive energy, current and voltage RMS, and total Energy.

.. code:: python

  stream.get_energy(3505, start = '12/29/2014', end = '1/29/2015', tz = 'local')

The :code:`search_group_tree` method accepts a keyword and searches the instantiated client for matching sensor groups returning group names, sensor group ID, and assigned sensors.

.. code:: python

  stream.search_group_tree('Engineering', case = False)

The :code:`base_group_level` column designates the grouping hierarchy by levels, with 0 being root groups.

.. code:: python

  stream.groups[stream.groups.base_group_level == 0]

The :code:`sensors` method returns a dataframe describing the individual sensors associated with the instantiated energistream client ID. This includes the sensor ID, the associated group ID, time zone, and a multiplier based on the method of measurement i.e. one, two, or three channel.

.. code:: python

  stream.sensors

The :code:`get_boards` method returns a dataframe describing the boards associated with the instantiated energistream client ID. This includes
the boards serial number, version, display name, and model.

.. code:: python

  stream.get_boards

The :code:`get_demand` method returns power data for a given sensor group(demand or generation) at multiple resolutions (1, 5, 10, 15, and 30 minutes, daily, weekly, monthly, and yearly). Start and end date may be specified as well as the timezone and desired resolution.

**Note**: Defaults to the last thirty days and fifteen minute resolution.

.. code:: python

  stream.get_demand(157)
