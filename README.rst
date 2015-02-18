EnergiStream
************

EnergiStream is an open source Python client for interacting with EnergiStream API, from MelRok.

Installation
^^^^^^^^^^^^

To install EnergiStream from source, clone the git repository to your local machine:

```sh
$ git clone git@github.com:melrok/energistream-py.git
```

In the ```energistream``` root directory (same one where you found this file after cloning the git repo), execute:

```sh
$ sudo pip install -e .
```

Dependencies
^^^^^^^^^^^^

EnergiStream has a few key dependancies:

* [pandas](http://pandas.pydata.org/) : >= 0.14.1
* [requests](http://docs.python-requests.org/) : >= 1.2.3
* [testfixtures](https://pythonhosted.org/testfixtures/)

All requirements are specified in the `requirements.txt`. One can attempt to install these alongside the `EnergiStream` installation via:

```
$ sudo pip install -r requirements.txt -e .
```

EnergiStream Guide
******************

A quick guide to some of the core EnergiStream functionality.

**Note** : Always refer to the doctrings for all methods for a detailed summary of the functionality.

Importing
^^^^^^^^^

To import the energistream library.

```python
import energistream as es # Imports the Energistream Library
```

Client Instantiation and Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

EnergiStreamClient takes a valid username and password and establishes a unique session with temporary credentials.

```python
stream = es.EnergiStreamClient('***REMOVED***', '***REMOVED***', include_sensors=True)
```

Authenticate uses the user credentials to authenticate the instantiated client in the event that authentication was not previously established or has lapsed.

```python
stream.authenticate
```

The `is_authenticated` method returns a simple boolean true or false when asked if the client authentication is still valid.

```python
stream.is_authenticated
```

External Data
^^^^^^^^^^^^^

The `get_weather` method returns a dataframe of hourly temperature and relative humidity data for the instantiated client's associated physical location.
>**Note**: This data is collected from third party sources. Weather ID is an energistream unique key and not associated to any third party ID schema.

```python
stream.get_weather(weather_id = 102, start = '12/29/2014', end = '1/29/2015')
```

Energistream Data and Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `get_energy` method accepts a sensor ID and returns a dataframe relating active and reactive energy, current and voltage RMS, and total Energy.

```python
stream.get_energy(3505, start = '12/29/2014', end = '1/29/2015', tz = 'local')
```

The `search_group_tree` method accepts a keyword and searches the instantiated client for matching sensor groups returning group names, sensor group ID, and assigned sensors.

```python
stream.search_group_tree('Engineering', case = False)
```

The `base_group_level` column designates the grouping hierarchy by levels, with 0 being root groups.

```python
stream.groups[stream.groups.base_group_level == 0]
```

The `sensors` method returns a dataframe describing the individual sensors associated with the instantiated energistream client ID. This includes the sensor ID, the associated group ID, time zone, and a multiplier based on the method of measurement i.e. one, two, or three channel.

```python
stream.sensors
```

The `get_boards` method returns a dataframe describing the boards associated with the instantiated energistream client ID. This includes
the boards serial number, version, display name, and model.

```python
stream.get_boards
```

The `get_demand` method returns power data for a given sensor group(demand or generation) at multiple resolutions (1, 5, 10, 15, and 30 minutes, daily, weekly, monthly, and yearly). Start and end date may be specified as well as the timezone and desired resolution.

**Note**: Defaults to the last thirty days and fifteen minute resolution.

```python
stream.get_demand(157)
```
