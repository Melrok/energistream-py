# encoding: utf-8
import requests
import warnings
import pandas as pd
import sys

#
# Globals
#

_LOAD_TYPES = {1: 'hvac', 2: 'heating', 3: 'cooling', 4: 'chilledwater',
               5: 'ventilation', 6: 'lighting', 7: 'indoorlighting',
               8: 'outdoorlighting', 9: 'plugload', 10: 'campus',
               11: 'building', 12: 'floor', 13: 'room', 14: 'roof',
               15: 'basement', 16: 'warehouse', 17: 'industrial',
               18: 'datacenter', 19: 'otherequipment', 20: 'otherlocation',
               21: 'electricity', 22: 'temperature', 23: 'humidity',
               24: 'power', 25: 'smoke', 26: 'motion', 27: 'sound',
               28: 'light', 29: 'entry', 20000: 'board', 20001: 'gateway',
               20002: 'daqdevice'}

_RESOLUTIONS = {'T': 'OneMinute',
                '5T': 'FiveMinute',
                '10T': 'TenMinute',
                '15T': 'FifteenMinute',
                '30T': 'ThirtyMinute',
                'H': 'Hourly',
                'D': 'Daily',
                'W': 'Weekly',
                'M': 'Monthly',
                'Y': 'Yearly'}


class EnergiStreamClient(object):

    def __init__(self, username=None, password=None,
                 maintain_authentication=False,
                 base_uri='http://energisaas.com', include_sensors=False,
                 attempt_login=True):
        """
        Instantiates a client for the EnergiStream API, allowing for
        establishing a unique session with temporary credentials.

        Parameters
        ----------
        username : str (default None)
            The account username
        password : str (default None)
            The account password
        maintain_authentication : bool (default False)
            If True, client instance maintains authentication with the API via
            detecting credentials loss and reauthenticating using cached
            username and password.
        base_uri : str
            The default URI of the EnergiSaaS web services
        include_sensors : bool (default False)
            If True, client instantiation and group population includes
            sensor levels
        attempt_login : (default True)
           If False, client does not attempt to authenticate upon
           instantiation
        """
        self._base_uri = base_uri
        self._melrok_uri = 'com.melrok.energy.services/sv'
        self._maintain_authentication = maintain_authentication
        self._username = username
        self._password = password
        self._include_sensors = include_sensors
        # Attempt to login if credentials provided

        self.groups = None
        if (username is not None) & (password is not None) & attempt_login:
            self._authenticate()
            self.groups = self._get_groups()

            if self._include_sensors:
                # Clean up sensor listings in group entries
                m = self.groups.sensors.map(lambda x: x == [])
                self.groups.loc[m, 'sensors'] = None
                self.sensors = self._get_sensors()

    def _authenticate(self):
        """
        Authenticates the client connection via user credentials.
        """
        if (self._username is None) | (self._password is None):
            raise ValueError('Authentication error, both username and password'
                             ' must be specified.')

        rel_resource_path = 'authentication/authenticate_account'
        params = {'username': self._username,
                  'password': self._password}
        #Sample URL for authentication
        #http://energisaas.com/com.melrok.energy.services/sv/authentication/
        #authenticate_account?username=[username]&password=[password]
        self.auth_response = self._perform_request(rel_resource_path,
                                                   params=params,
                                                   reauthenticate=False)
        response_dict = self.auth_response.json()
        self.account_id = response_dict['accountId']
        self.token_id = response_dict['tokenId']

    @property
    def _is_authenticated(self):
        """
        Returns True if the EnergiStreamClient instance session is
        authenticated, otherwise False. If response returned is not
        recognized, raises TypeError.
        """
        #http://energisaas.com/com.melrok.energy.services/sv/
        #authentication/verify_account_token?tokenid=222
        #{"accountId":0,"code":"INVALID_TOKEN","duration":8}
        rel_resource_path = 'authentication/verify_account_token'
        handled_errors = ["INVALID_TOKEN"]
        response = self._perform_request(rel_resource_path,
                                         tokenid=self.token_id,
                                         handled_errors=handled_errors,
                                         reauthenticate=False)
        status = response.json()['code']
        if status == "INVALID_TOKEN":
            return False
        elif status == "OK":
            return True
        else:
            raise TypeError("Unexpected response status={0}".format(status))

    def _get_time_zone_info(self, data_format='df'):
        """
        Returns time zone information from energisaas services
        """
        rel_resource_path = 'information/timezones'
        response = self._perform_request(rel_resource_path,
                                         reauthenticate=False)
        if data_format == 'json':
            return response.json()
        elif data_format == 'df':
            raw_json = response.json()['timeZoneInfos']
            df = pd.DataFrame(raw_json)
            df.set_index('timeZoneId', inplace=True)
            return df

    def _get_sensor_data(self, group_id, metric, start=None, end=None, tz=None,
                         resolution='15T', data_format='df'):
        raise(NotImplementedError)

    def get_weather(self, weather_id=102, start=None, end=None, tz=None,
                    to_hour_mark=True):
        """
        Returns hourly weather time series data for a weather station
        location.

        Parameters
        ----------

        weather_id : int (default, 102 -- UC Irvine's)
            The id of the weather station. Note that `weather_id` is an
            EnergiStream unique key for the weather station and does not
            relate to references by external sources to the same weather data.
        start : str, int (default, None)
            The starting datetime of the time range. If None, defaults to one
            month before the ending time set in `end`.
        end : str, int (default, None)
            The ending datetime of the time range. If None, defaults to
            today's time (i.e., the current local timestamp).
        tz : str (default, None)
            The time zone for time range of the query. By default, queries in
            the local time zone of the group (specified in the `time_zone`
            column of the `.groups` attribute). Additionally, one can also
            query for a time range based on other time zones by specifying
            an IANA (Olson) time zone format (e.g. 'UTC', 'US/Pacific',
            'Europe/Berlin', 'America/Argentina/Buenos_Aires')
        to_hour_mark : bool (default, True)
            Normalizes (via resampling) the weather times series to exist 'on
            the hour' timestamps.

        Returns
        -------
        weather: Series

        """
        #Sample URL:
        #http://energisaas.com/com.melrok.energy.services/sv/data/weather?
        #accountid=4&tokenid=1EFAF5BE2B924EC0ABDAF4691DAD4793613017EE&
        #stationid=102&fromtime=20140519060001&totime=20140520070000

        #Convert to properly formatted timestamp representations
        start, end = _sanitize_dates(start, end, tz=tz)

        rel_resource_path = 'data/weather'
        params = {'tokenid': self.token_id,
                  'accountid': self.account_id,
                  'stationid': weather_id,
                  'fromtime': start,
                  'totime': end}
        response = self._perform_request(rel_resource_path, params=params)
        raw_json = response.json()['values']
        #format df
        df = pd.DataFrame(raw_json)

        dti = pd.DatetimeIndex(df['ts'])  # + pd.offsets.Second(1)
        df.index = dti.tz_localize('UTC')
        if tz:
            df.index = df.index.tz_convert(tz)
        df = df.drop(['ts'], axis=1)
        df.name = weather_id
        if to_hour_mark:
            df = df.resample('H', closed='right')
        weather = df
        return weather

    @property
    def get_boards(self):
        """
        Queries for all boards belonging to customer account
        """
        #Sample URL:
        #http://energisaas.com/com.melrok.energy.services/sv/information/
        #boards?accountid=4&tokenid=AAE1025A554F286A9275728F68F5F841FBDCBFFE
        rel_resource_path = 'information/boards'
        params = {'accountid': self.account_id,
                  'tokenid': self.token_id}
        response = self._perform_request(rel_resource_path, params=params)
        raw_json = response.json()['boards']
        df = pd.DataFrame(raw_json)
        df.set_index('serialNumber', inplace=True)
        df.name = 'boards_info'
        return df

    def get_board_sensors(self, board_sn):
        """
        Queries and returns all sensors that belong to a board.


        """
        #Sample URL:
        #http://energisaas.com/com.melrok.energy.services/sv/information/
        #boards/sensors?accountid=4&tokenid
        # =AAE1025A554F286A9275728F68F5F841FBDCBFFE
        #&boardsn=XXXXXXXXXXX
        rel_resource_path = 'information/boards/sensors'
        params = {'accountid': self.account_id,
                  'tokenid': self.token_id,
                  'boardsn': board_sn}
        response = self._perform_request(rel_resource_path, params=params)
        raw_json = response.json()['sensors']
        #return raw_json
        df = pd.DataFrame(raw_json)
        df.set_index('sensorId', inplace=True)
        df.name = 'boards_info'
        return df

    def get_energy(self, sensor_id, start=None, end=None, tz='local'):
        """
        Returns raw energy data for the sensor_id.
        """
        #Sample URL:
        # http://energisaas.com/com.melrok.energy.services/sv/data/energy?
        # sensorid=529&fromtime=20140301000000&totime=20140302000000&
        # tokenid=1EFAF5BE2B924EC0ABDAF4691DAD4793613017EE

        #Convert to properly formatted timestamp representations
        group = self.sensors_unique().loc[sensor_id]
        if tz is 'local':
            tz = group['time_zone']
        start, end = _sanitize_dates(start, end, tz=tz)
        rel_resource_path = 'data/energy'

        params = {'tokenid': self.token_id,
                  'sensorid': sensor_id,
                  'fromtime': start,
                  'totime': end}
        response = self._perform_request(rel_resource_path, params=params)
        raw_json = response.json()['measurements']
        #format df
        df = pd.DataFrame(raw_json)

        dti = pd.DatetimeIndex(df['timestamp'])  # + pd.offsets.Second(1)
        df.index = dti.tz_localize('UTC')
        if tz:
            df.index = df.index.tz_convert(tz)
        df = df.drop(['timestamp'], axis=1)
        df.name = sensor_id
        energy = df
        return energy



    def get_demand(self, group_id, start=None, end=None, tz='local',
                   resolution='15T', data_format='pd', completed_flag=False):
        """
        Returns demand time series data for a specific sensor / sensor group
        id over a time range specified.

        Parameters
        ----------

        group_id : int (required)
            The id of the sensor or group resource. ID's of all sensors and
            groups are available in the `.groups` or `.sensors` attribute.
        start : str, int (default, None)
            The starting datetime of the time range. If None, defaults to one
            month before the ending time set in `end`.
        end : str, int (default, None)
            The ending datetime of the time range. If None, defaults to
            today's time (i.e., the current local timestamp).
        tz : str (default 'local')
            The time zone for time range of the query. By default, queries in
            the local time zone of the group (specified in the `time_zone`
            column of the `.groups` attribute). Additionally, one can also
            query for a time range based on other time zones by specifying
            an IANA (Olson) time zone format (e.g. 'UTC', 'US/Pacific',
            'Europe/Berlin', 'America/Argentina/Buenos_Aires')
        resolution : str (default '15T')
            The time resolution of the time series in pandas offset alias
            format. Can be one of: ['T', '5T', '10T', '15T' '30T', 'H', 'D',
            'W', 'M', 'Y']
        data_format : str (default 'df')
            The format of the demand time series data returned. Can be one of:
            'json' : the raw JSON response
            'pd'   : a formatted pandas object (e.g., Series or DataFrame)

        Returns
        -------
        demand: str, Series, DataFrame, GroupLoad

        """
        #Sample URL query
        #http://energisaas.com/com.melrok.energy.services/sv/data/consumption/
        #?accountid=4&#tokenid=AAE1025A554F286A9275728F68F5F841FBDCBFFE&
        #sensorgroupid=115&fromtime=20130831064501&totime=20130901070000&
        #metric=EnergyDemand&resolution=FifteenMinute

        #Check data_format
        _data_formats = ['pd', 'json']
        if data_format not in _data_formats:
            msg = ('Value \'{0}\' for `data_format` not '
                   'recognized. Must be one of {1}').format(data_format,
                                                            _data_formats)
            raise ValueError

        #
        # Define function parameters
        #
        #Check resolution, follows pandas offset alias convention:
        #pandas.pydata.org/pandas-docs/dev/timeseries.html#offset-aliases
        if resolution not in list(_RESOLUTIONS.values()):
            if resolution not in list(_RESOLUTIONS.keys()):
                msg = ('Value \'{0}\' for `resolution` not recognized. Must '
                       'be one of {1}').format(resolution,
                                               _RESOLUTIONS)
                raise ValueError
            resolution = _RESOLUTIONS[resolution]
        metric = 'EnergyDemand'
        group_data = self.groups.loc[group_id]
        #Convert to properly formatted timestamp representations
        if tz is 'local':
            tz = group_data['time_zone']
        start, end = _sanitize_dates(start, end, tz=tz)

        #Generate parameters and perform request
        params = {'accountid': self.account_id,
                  'tokenid': self.token_id,
                  'fromtime': start,
                  'totime': end,
                  'metric': metric,
                  'resolution': resolution}

        if isinstance(group_id, int):
            params['sensorgroupid'] = group_id
            response = self._request_demand(data_format, params, tz)

        else:  # assume iterable
            response_dict = {}
            for sensor_group in group_id:
                #print 'Response Dict: ' + str(response_dict)
                params['sensorgroupid'] = sensor_group
                response = self._request_demand(data_format, params, tz)
                if response is not None:
                    response_dict[sensor_group] = response
                else:
                    msg = 'No Data returned for sensor group {0}'
                    msg = msg.format(sensor_group)
                    warnings.warn(msg)
            response = response_dict

        if data_format == 'json':
            return response
        if isinstance(response, dict):
            response = pd.DataFrame(response)
        if data_format == 'pd':
            if completed_flag:
                return response
            else:
                return response['kW']

        raise ValueError('Unexpected data_format {0}'.format(data_format))

    def get_group_data(self, group_id):
        if self.groups is None:
            self.groups = self._get_groups()
        return self.groups.loc[group_id]


    #TODO: document that this raises exception in case where demand data is empty
    def _request_demand(self, response_format, params, tz=None):
        #print response_format
        #print params
        rel_resource_path = 'data/consumption'
        group_id = params['sensorgroupid']
        response = self._perform_request(rel_resource_path, params=params)

        #Parse JSON response
        raw_json = response.json()['consumptions']
        if response_format == 'json':
            return raw_json
        try:
            #print 'HERE'
            df = pd.DataFrame(raw_json)
            df.columns = ['completed', 'start_time', 'end_time', 'kW']
            dti = pd.DatetimeIndex(df.end_time)  # + pd.offsets.Second(1)
            df.index = dti.tz_localize('UTC')
            if tz:
                df.index = df.index.tz_convert(tz)
            demand = df.drop(['start_time', 'end_time'], axis=1)
            demand.name = group_id
        except:
            e = sys.exc_info()[0]
            msg = 'GroupId {0} contains no demand data, skipping. Captured error: {1}'
            msg = msg.format(group_id, e)
            warnings.warn(msg)
            raise
        if response_format == 'pd':
            return demand

    def _get_groups(self, denorm_col='sensorGroups',
                    drop_cols=['groupVersion', 'multiplier', 'iconId',
                               'timeZoneId']):
        """
        Returns the groups list for a customer account, with an option to
        return the sensors.
        """
        #Sample URL query
        #http://energisaas.com/com.melrok.energy.services/sv/information/
        #sensorgroups?accountid=[AccountId]&tokenid=[tokenId of the session]
        #&includesensors=[true|false]

        rel_resource_path = 'information/sensorgroups'

        params = {'accountid': self.account_id,
                  'tokenid': self.token_id,
                  'includesensors': self._include_sensors}
        response = self._perform_request(rel_resource_path, params=params)
        raw_json = response.json()[denorm_col]
        groups_df = _denormalize_json(raw_json, denorm_col,
                                      index='sensorGroupId')
        # Map iconId to load types
        groups_df['load_type'] = groups_df['iconId'].map(_LOAD_TYPES)
        # Map timeZoneId to IANA time zone
        tz_df = self._get_time_zone_info()
        time_zones = groups_df['timeZoneId'].map(tz_df['javaTimeZoneInfoId'])
        groups_df['time_zone'] = time_zones

        #Drop columns and reorganize DataFrame
        groups_df = groups_df.drop(drop_cols, axis=1)

        if self._include_sensors:
            reordered = ['name', 'description', 'load_type',
                         'sensorGroups', 'sensors', 'groupMultiplier',
                         'time_zone', 'weatherStationId',
                         'base_group_level']
        else:
            reordered = ['name', 'description', 'load_type',
                         'sensorGroups', 'groupMultiplier',
                         'time_zone', 'weatherStationId',
                         'base_group_level']

        groups_df = groups_df[reordered]

        return groups_df

    def _get_sensors(self):
        m = self.groups.sensors.isnull()
        sensor_df = []
        for sensors in self.groups.sensors[~m].values:
            sensor_df.append(pd.DataFrame(sensors))

        sensor_df = pd.concat(sensor_df)
        sensor_df.set_index('sensorId', inplace=True)

        # Map timeZoneId to IANA time zone
        tz_df = self._get_time_zone_info()
        time_zones = sensor_df['timeZoneId'].map(tz_df['javaTimeZoneInfoId'])
        sensor_df['time_zone'] = time_zones
        sensor_df.drop('timeZoneId', axis=1, inplace=True)

        return sensor_df

    def search_group_tree(self, pat, case=False):
        m1 = self.groups.name.str.contains(pat, case=case)
        m2 = self.groups.description.str.contains(pat, case=case)
        return self.groups[m1 | m2]

    def _perform_request(self, rel_resource_path, params=None,
                         handled_errors=None, reauthenticate=None,
                         **kwargs):
        """
        Constructs and performs query to EnergiStream API, returns
        requests (as in requests Python library) instance.
        """
        if reauthenticate is None:
            reauthenticate = self._maintain_authentication  # True or False
        if reauthenticate:
            try:
                response = self._request(rel_resource_path, params,
                                         handled_errors, **kwargs)
            except UnauthorizedAccess:
                self._authenticate()
                warnings.warn('Reauthenticated client instance.')
                params['tokenid'] = self.token_id
                response = self._request(rel_resource_path, params,
                                         handled_errors, **kwargs)
        else:
            response = self._request(rel_resource_path, params,
                                     handled_errors, **kwargs)
        return response

    def _request(self, rel_resource_path, params,
                 handled_errors, **kwargs):

        url = '{0}/{1}/{2}'.format(self._base_uri, self._melrok_uri,
                                   rel_resource_path);
        args_dict = dict()
        if params is not None:
            args_dict.update(params)
        if kwargs is not None:
            args_dict.update(kwargs)

        response = requests.get(url, params=args_dict)

        try:
            response_code = response.json()['code']
        except:
            warnings.warn('Unable to parse response as json: response={0}'.format(response.text))
            raise

        if handled_errors is None:
            handled_errors = []
        handled_errors.append('OK')
        if response_code in handled_errors:
            return response
        elif response_code == 'UNAUTHORIZED_ACCESS':
            msg = ('Resource accessed unauthorized ({0}). Check query '
                   'parameters and/or reauthenticate client '
                   'token id.').format(rel_resource_path)
            raise UnauthorizedAccess
        else:  # unknown response code
            msg = ('Resource response code ({0}) not recognized by '
                   'client.').format(response_code)
            raise TypeError


    def sensors_unique(self):
        s = self.sensors
        return s.groupby(s.index).first()

class UnauthorizedAccess(ValueError):
    """
    Custom exception for unauthorized resource access to EnergiStream API.
    """
    pass


def _denormalize_json(raw_json, denorm_col, index=None, base_group_level=0):
    """
    Returns a denormalized DataFrame via parsing a nested JSON object.

    Parameters
    ----------

    denorm_col: str, default None
        The JSON field / key over which to perform denormalization.

    index: str, default None
        The JSON field / key to set as index of DataFrame.

    base_group_level: int, default 0

    Returns
    ------
    denormed_df: DataFrame
    """
    def _contains_data(data_elem):
        if data_elem:
            return True
        else:
            return False

    #Set index of df
    df = pd.DataFrame(raw_json)
    if index:
        df = df.set_index(index)

    #Create column for group multiplier
    df['groupMultiplier'] = None
    df['base_group_level'] = base_group_level
    #Create mask to find children groups
    mask = df[denorm_col].apply(_contains_data)
    if mask.any():
        df_list = []
        index_list = []
        mult_list = []
        for json_from_elem in df.loc[mask, denorm_col]:
            increment = base_group_level + 1
            denormalized_df = _denormalize_json(json_from_elem,
                                                denorm_col=denorm_col,
                                                index=index,
                                                base_group_level=increment)
            df_list.append(denormalized_df)
            index_list.append(denormalized_df.index)
            mult_list.append(denormalized_df.multiplier.tolist())

        df_denormed = pd.concat(df_list)
        df.loc[~mask, denorm_col] = None

        # Fix to mask pandas bug introduced by:
        # https://github.com/pydata/pandas/pull/7552
        # (pandas/core/indexing.py#L435)
        masked_idx = mask[mask].index
        df.loc[mask, denorm_col] = pd.Series(index_list, index=masked_idx)
        df.loc[mask, 'groupMultiplier'] = pd.Series(mult_list,
                                                    index=masked_idx)
        df_denormed = pd.concat([df, df_denormed])
        return df_denormed

    else:
        df[denorm_col] = None
        return df


def _sanitize_dates(start=None, end=None, tz=None, str_format='%Y%m%d%H%M%S'):
    if start is not None:
        start = str(start)
    if end is not None:
        end = str(end)
    if start is None:
        start = pd.datetime.today() - pd.offsets.DateOffset(months=1)
    if end is None:
        end = pd.datetime.today()

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    if tz:
        start = start.tz_localize(tz).tz_convert('UTC')
        end = end.tz_localize(tz).tz_convert('UTC')
    #Format and ensure uniqueness
    start = start.strftime(str_format)
    end = end.strftime(str_format)
    #print start, end
    if start == end:
        msg = 'Demand query start {0} and end {1} times cannot be equal.'
        msg = msg.format(start, end)
        raise ValueError
    return start, end


