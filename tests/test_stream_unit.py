import unittest
import json
import logging
import energistream as es

from energistream import UnauthorizedAccess
from testfixtures import log_capture

from mock import MagicMock
from mock import patch
from verify import Verify


class UnitTestsEnergiStreamClientWithMocks(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.verify = Verify()

    def setUp(self):
        self.username = 'johncleese'
        self.password = 'opensesame'
        self.account_id = 'A42'
        self.token_id = 'T000032'
        self.es_client = es.EnergiStreamClient(username=self.username, password=self.password, attempt_login=False)
        self.es_client._username = self.username
        self.es_client._password = self.password

        self.es_client.token_id = self.token_id
        self.es_client.account_id = self.account_id

    def tearDown(self):
        print('tearDown()')

    @log_capture()
    def test_given_username_none_auth_error(self, lc):
        # setup
        self.es_client._username = None
        self.es_client._password = self.password
        try:
            # unit under test
            self.es_client._authenticate()
            self.fail('Expected ValueError to be thrown')
        except ValueError as err:
            # expected case
            self.logger.info('Error message: {0}'.format(err.message))
            lc.check((__name__, 'INFO',
                     'Error message: Authentication error, both username and '
                     'password must be specified.'))

    @log_capture()
    def test_given_password_none_auth_error(self, lc):
        # setup
        self.es_client._username = self.username
        self.es_client._password = None
        try:
            # unit under test
            self.es_client._authenticate()
            self.fail('Expected ValueError to be thrown')
        except ValueError as err:
            # expected case
            self.logger.info('Error message: {0}'.format(err.message))
            lc.check((
                __name__, 'INFO',
                'Error message: Authentication error, both username and '
                'password must be specified.'))

    def test_given_successful_auth_returns_ok_response(self):
        # setup
        with patch('requests.get') as mock_requests_get:
            mock_requests_get.return_value = self.mock_auth_response_ok()

            # unit under test
            self.es_client._authenticate()

            # verify
            self.verify.str_equal(self.account_id, self.es_client.account_id,
                                  'expected account id to be stored on client')
            self.verify.str_equal(self.token_id, self.es_client.token_id,
                                  'expected token id to be stored on client')

    @log_capture()
    def test_auth_returns_failure_response(self, lc):
        # setup
        with patch('requests.get') as mock_requests_get:
            mock_requests_get.return_value = self.mock_auth_response_fail()

            # unit under test
            try:
                # unit under test
                self.es_client._authenticate()
                # verify
                self.fail('Expected failure')
            except TypeError as err:
                self.logger.info(err.message)
                lc.check((__name__, 'INFO',
                         'Resource response code (FAILURE) not recognized by '
                         'client.'))

    def test_is_authenticated_invalid_token_returns_false(self):
        # setup
        self.es_client._perform_request = MagicMock()
        self.es_client._perform_request.return_value = \
            self.mock_auth_response_invalid_token()

        # unit under test
        self.authenticated = self.es_client._is_authenticated

        # verify
        assert self.authenticated is False

    def test_is_authenticated_ok_response_returns_true(self):
        # setup
        self.es_client._perform_request = MagicMock()
        self.es_client._perform_request.return_value = \
            self.mock_auth_response_ok()
        # unit under test
        is_auth = self.es_client._is_authenticated

        # verify
        assert is_auth is True

    def test_is_authenticated_ok_unexpected_response_raises_error(self):
        # setup
        self.es_client._perform_request = MagicMock()
        self.es_client._perform_request.return_value = \
            self.mock_auth_response_fail()

        raised_type_error = False
        try:
            # unit under test
            self.es_client._is_authenticated
            # verify
            self.fail('Expected raises TypeError')
        except TypeError:
            # expected case
            raised_type_error = True
        assert raised_type_error

    def test_get_timezone_info_returns_data_frame(self):
        # setup
        self.es_client._perform_request = MagicMock()
        mock_response = self.mock_response_json(
            {"timeZoneInfos": {"timeZoneId": ["A1"], "data": ["US/Pacific"]}})
        self.es_client._perform_request.return_value = mock_response
        # unit under test
        data_frame = self.es_client._get_time_zone_info(data_format='df')

        # verify
        self.verify.str_equal(
            '<class \'pandas.core.frame.DataFrame\'>', str(
                type(data_frame)), 'Expected pandas dataframe type')
        self.verify.str_equal('US/Pacific', data_frame.values[0][0],
                              'Expected timezone to be properly parsed')

    def test_get_timezone_info_returns_json(self):
        # setup
        self.es_client._perform_request = MagicMock()
        mock_response = self.mock_response_json(
            {"timeZoneInfos": {"timeZoneId": ["A1"], "data": ["US/Pacific"]}})
        self.es_client._perform_request.return_value = mock_response
        # unit under test
        response = self.es_client._get_time_zone_info(data_format='json')
        # verify
        tz = response['timeZoneInfos']['data'][0]
        self.verify.str_equal('<type \'dict\'>', str(type(response)),
                              'Expected dictionary type')
        self.verify.str_equal('US/Pacific', tz,
                              'Expected timezone to be properly parsed')

    def test_get_demand_invalid_data_format(self):
        # setup
        try:
            # unit under test
            self.es_client.get_demand(group_id='123', data_format='bunk')
            # verify
            self.fail('Expected failure')
        except ValueError as err:
            self.verify.str_in(
                err.message,
                'Value \'bunk\' for `data_format` not recognized')

    def test_get_demand_invalid_resolution(self):
        # setup
        try:
            # unit under test
            self.es_client.get_demand(group_id='123', resolution="5Y")
            # verify
            self.fail('Expected failure')
        except ValueError as err:
            self.verify.str_in(err.message,
                               'Value \'5Y\' for `resolution` not recognized')

    def test_request_returns_response_when_ok(self):
        # setup
        with patch('requests.get') as mock_requests_get:
            mock_requests_get.return_value = self.mock_auth_response_ok()
            rel_path = 'good/stuff.html'
            params = dict()
            handled_errors = None
            # unit under test
            response = self.es_client._request(rel_path, params,
                                               handled_errors)
            # verify
            self.verify.str_equal(response.json()['code'], 'OK',
                                  'Expected ok response')

    def test_request_given_unauthorized_access_raises_exception(self):
        # setup
        with patch('requests.get') as mock_requests_get:
            mock_requests_get.return_value = self.mock_response_str(
                '{"code":"UNAUTHORIZED_ACCESS"}')
            rel_path = 'secret/stuff.html'
            params = dict()
            handled_errors = None
            # unit under test
            try:
                self.es_client._request(rel_path, params, handled_errors)
                self.fail('Expected unauthorized access ValueError')
            except ValueError as err:
                # verify
                self.verify.str_in(
                    err.message,
                    'Resource accessed unauthorized (secret/stuff.html)',
                    'Expected unauthorized access error')

    def test_perform_request_returns_response_when_ok(self):
        # setup
        self.es_client._maintain_authentication = False
        mocked_request_method = MagicMock(
            return_value=self.mock_auth_response_ok())
        self.es_client._request = mocked_request_method
        rel_path = 'good/stuff.html'
        params = {'potatos': 2, 'potattos': 3}
        handled_errors = ['BOOM']
        # unit under test
        response = self.es_client._perform_request(rel_path, params,
                                                   handled_errors)
        # verify
        self.verify.str_equal('OK', response.json()['code'],
                              'Expected ok response')
        mocked_request_method.assert_called_with(rel_path, params,
                                                 handled_errors)

    def test_get_weather(self):
        # setup
        self.es_client._perform_request = MagicMock()
        self.es_client._perform_request.return_value = \
            self.mock_simple_weather_response()

        # unit under test
        weather_pd = self.es_client.get_weather(tz='US/Pacific')

        # verify
        self.verify.str_equal('<class \'pandas.core.frame.DataFrame\'>',
                              type(weather_pd), 'Expected pandas dataframe')
        self.verify.str_equal(
            18.9,
            weather_pd['c']['2014-12-19 11:00'],
            'celsius temperature should have been passed through and parsable')
        self.verify.str_equal(
            20.0,
            weather_pd['c']['2014-12-19 12:00'],
            'celsius temperature should have been passed through and parsable')
        self.verify.str_equal(
            20.6,
            weather_pd['c']['2014-12-19 13:00'],
            'celsius temperature should have been passed through and parsable')

        self.verify.str_equal(
            49.0,
            weather_pd['h']['2014-12-19 11:00'],
            'humidity should have been passed through and parsable')
        self.verify.str_equal(
            45.0,
            weather_pd['h']['2014-12-19 12:00'],
            'humidity should have been passed through and parsable')
        self.verify.str_equal(
            49.0,
            weather_pd['h']['2014-12-19 13:00'],
            'humidity should have been passed through and parsable')

        self.verify.str_equal(
            66.0,
            weather_pd['f']['2014-12-19 11:00'],
            'fahrenheit temperature should have been passed through and '
            'parsable')
        self.verify.str_equal(
            68.0,
            weather_pd['f']['2014-12-19 12:00'],
            'fahrenheit temperature should have been passed through and '
            'parsable')
        self.verify.str_equal(
            66.0,
            weather_pd['f']['2014-12-19 13:00'],
            'fahrenheit temperature should have been passed through and '
            'parsable')

    def test_request_demand_returns_raw_json(self):
        # setup
        self.es_client._perform_request = MagicMock()
        self.es_client._perform_request.return_value = \
            self.mock_simple_request_demand()

        params = {'accountid': self.es_client.account_id,
                  'tokenid': self.es_client.token_id, 'sensorgroupid': 216,
                  'metric': 'EnergyDemand', 'fromtime': 20130831064501,
                  'totime': 20130901070000, 'tz': 'local',
                  'resolution': 'FifteenMinute'}
        # unit under test
        demand = self.es_client._request_demand(response_format='json',
                                                params=params)
        # verify
        self.verify.str_equal(
            5432.606866,
            demand[0]['value'],
            'demand should have been passed through and parsable')
        self.verify.str_equal(
            1234.877266,
            demand[1]['value'],
            'demand should have been passed through and parsable')
        self.verify.str_equal(
            1111.028733,
            demand[2]['value'],
            'demand should have been passed through and parsable')

    def test_request_demand_returns_pandas_data_frame(self):
        # setup
        self.es_client._perform_request = MagicMock()
        self.es_client._perform_request.return_value = \
            self.mock_simple_request_demand()

        params = {'accountid': self.es_client.account_id,
                  'tokenid': self.es_client.token_id, 'sensorgroupid': 216,
                  'metric': 'EnergyDemand', 'fromtime': 20130831064501,
                  'totime': 20130901070000, 'tz': 'local',
                  'resolution': 'FifteenMinute'}

        # unit under test
        demand = self.es_client._request_demand(response_format='pd',
                                                params=params)
        # verify
        self.verify.str_equal("<class 'pandas.core.frame.DataFrame'>",
                              type(demand))
        self.verify.str_equal(
            5432.606866,
            demand['kW'][0],
            'demand should have been passed through and parsable')
        self.verify.str_equal(
            1234.877266,
            demand['kW'][1],
            'demand should have been passed through and parsable')
        self.verify.str_equal(
            1111.028733,
            demand['kW'][2],
            'demand should have been passed through and parsable')

    def test_request_demand_group_id_has_no_demand_data(self):
        # setup
        self.es_client._perform_request = MagicMock()
        self.es_client._perform_request.return_value = self.mock_response_json(
            {'consumptions': []})
        params = {'accountid': self.es_client.account_id,
                  'tokenid': self.es_client.token_id, 'sensorgroupid': None,
                  'metric': 'EnergyDemand', 'fromtime': 20130831064501,
                  'totime': 20130901070000, 'tz': 'local',
                  'resolution': 'FifteenMinute'}

        # unit under test
        try:
            demand = self.es_client._request_demand(response_format='pd',
                                                    params=params)
            self.fail('Expected value error due to empty data set')
        except ValueError as err:
            self.verify.str_in(err.message, 'Length mismatch')

    # This test loads actual data returned from the service with some json
    # formatting repairs.
    # The requests library seems to handle problems with the json,
    # where json.loads() will not.
    # This test needs a clean dataset and could use
    # another set of eyes and needs some verification at the end.
    # Ignoring test for now, intend to fix it when possible
    # We should also be mocking other internal calls within _get_groups such
    #  as: _denormalize_json.
    def IGNORE_get_groups_returns_pandas_data_frame(self):
        # setup
        self.es_client._perform_request = MagicMock()
        self.es_client._perform_request.return_value = \
            self.mock_deep_get_groups()
        # unit under test
        demand = self.es_client._get_groups()
        #
        # # verify
        # TODO: validate something

    # ---Functions that create mocks---
    def mock_auth_response_ok(self):
        return self.mock_response_str(
            '{{"code":"OK", "accountId":"{account}", "tokenId":"{'
            'token}"}}'.format(
                account=self.account_id, token=self.token_id))

    def mock_auth_response_fail(self):
        return self.mock_response_str(
            '{"code":"FAILURE", "message":"Unable to authenticate account"}')

    def mock_auth_response_invalid_token(self):
        return self.mock_response_str(
            '{"code":"INVALID_TOKEN", "message":"Token is invalid"}')

    def mock_auth_response_unauthorized_access(self):
        return self.mock_response_str(
            '{"code":"INVALID_TOKEN", "message":"Token is invalid"}')

    def mock_response_str(self, json_str):
        mock_response = MagicMock()
        json_response = json.loads(json_str)
        mock_response.json = MagicMock(return_value=json_response)
        return mock_response

    def mock_response_json(self, json):
        response = MagicMock()
        response.json = MagicMock(return_value=json)
        return response

    def mock_simple_weather_response(self):
        json_data = {"values": [
            {'h': 49.0, 'c': 18.9, 'ts': '20141219185300', 'f': 66.0},
            {'h': 45.0, 'c': 20.0, 'ts': '20141219195300', 'f': 68.0},
            {'h': 49.0, 'c': 20.6, 'ts': '20141219205300', 'f': 66.0}]}
        return self.mock_response_json(json_data)

    def mock_simple_request_demand(self):
        json_data = {'consumptions': [
            {'to': '20130831065959', 'completed': False,
             'from': '20130831064500', 'value': 5432.606866},
            {'to': '20130831071459', 'completed': False,
             'from': '20130831070000', 'value': 1234.877266},
            {'to': '20130831072959', 'completed': False,
             'from': '20130831071500', 'value': 1111.028733}]}
        return self.mock_response_json(json_data)

    def mock_simple_get_groups(self):
        json_data = {'timeZoneId': 67,
                     'name': 'Some Electric Meter Sub Groups',
                     'sourceId': 0,
                     'iconId': 10,
                     'sensorGroupId': 222,
                     'groupVersion': 0,
                     'multiplier': 1,
                     'weatherStationId': 99,
                     'capacityAmps': 100,
                     'sensorGroups': [{'timeZoneId': 67,
                                        'name': 'Some Electric Meter Sub Groups',
                                        'sourceId': 0,
                                        'iconId': 10,
                                        'sensorGroupId': 222,
                                        'groupVersion': 0,
                                        'multiplier': 1,
                                        'weatherStationId': 99,
                                        'capacityAmps': 100}],
                     'description': 'Total Electric Load for Some Campus'}
        return self.mock_response_json(json_data)

    def mock_deep_get_groups(self):
        f = open('energiscore/tests/data/groupdata-corrected.json')
        json_str = f.read()
        mock_response = MagicMock()
        json_response = json.loads(json_str)
        mock_response.json = MagicMock(return_value=json_response)
        return mock_response
