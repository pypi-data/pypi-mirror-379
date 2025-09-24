# Copyright 2016 Hewlett Packard Enterprise Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import functools

from oslo_log import log as logging
from oslo_serialization import jsonutils as json
from tempest.lib.common import rest_client
from tempest.lib import exceptions as lib_exc
from urllib import parse as urllib_parse

from designate_tempest_plugin.common import models

LOG = logging.getLogger(__name__)


def handle_errors(f):
    """A decorator that allows to ignore certain types of errors."""

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        param_name = 'ignore_errors'
        ignored_errors = kwargs.get(param_name, tuple())

        if param_name in kwargs:
            del kwargs[param_name]

        try:
            return f(*args, **kwargs)
        except ignored_errors as e:
            # Silently ignore errors as requested
            LOG.debug('Ignoring exception of type %s, as requested', type(e))

    return wrapper


class DnsClientBase(rest_client.RestClient):
    """Base Tempest REST client for Designate API"""

    uri_prefix = ''

    CREATE_STATUS_CODES = []
    SHOW_STATUS_CODES = []
    LIST_STATUS_CODES = []
    PUT_STATUS_CODES = []
    UPDATE_STATUS_CODES = []
    DELETE_STATUS_CODES = []

    def serialize(self, data):
        if isinstance(data, str):
            return data
        return json.dumps(data)

    def deserialize(self, resp, object_str):
        if 'content-type' in resp.keys():
            if 'application/json' in resp['content-type']:
                return json.loads(object_str)
            elif 'text/dns' in resp['content-type']:
                return models.ZoneFile.from_text(object_str.decode("utf-8"))
            else:
                raise lib_exc.InvalidContentType()
        else:
            return None

    @classmethod
    def expected_success(cls, expected_code, read_code):
        # the base class method does not check correctly if read_code is not
        # an int. warn about this and cast to int to avoid silent errors.
        if not isinstance(read_code, int):
            message = ("expected_success(%(expected_code)r, %(read_code)r) "
                       "received not-int read_code %(read_code)r" %
                       {'expected_code': expected_code,
                        'read_code': read_code})
            LOG.warning(message)
        return super(DnsClientBase, cls).expected_success(
            expected_code=expected_code, read_code=int(read_code),
        )

    def get_uri(self, resource_name, uuid=None, params=None,
                uuid_prefix_char=None):
        """Get URI for a specific resource or object.
        :param resource_name: The name of the REST resource, e.g., 'zones'.
        :param uuid: The unique identifier of an object in UUID format.
        :param params: A Python dict that represents the query paramaters to
                       include in the request URI.
        :param uuid_prefix_char: applies to override hardcoded ('/')
                prefix UUID character. This parameter enables to set required
                by API character, for example ":" instead of "/".
        :returns: Relative URI for the resource or object.
        """
        uri_pattern = '{pref}/{res}{uuid}{params}'

        if uuid_prefix_char:
            uuid = uuid_prefix_char + '%s' % uuid if uuid else ''
        else:
            uuid = '/%s' % uuid if uuid else ''

        params = '?%s' % urllib_parse.urlencode(params) if params else ''

        return uri_pattern.format(pref=self.uri_prefix,
                                  res=resource_name,
                                  uuid=uuid,
                                  params=params)

    def _create_request(self, resource, data=None, params=None,
                        headers=None, extra_headers=False,
                        expected_statuses=None):
        """Create an object of the specified type.
        :param resource: The name of the REST resource, e.g., 'zones'.
        :param data: A Python dict that represents an object of the
                     specified type (to be serialized) or a plain string which
                     is sent as-is.
        :param params: A Python dict that represents the query paramaters to
                       include in the request URI.
        :param headers (dict): The headers to use for the request.
        :param extra_headers (bool): Boolean value than indicates if the
                                     headers returned by the get_headers()
                                     method are to be used but additional
                                     headers are needed in the request
                                     pass them in as a dict.
        :param expected_statuses: If set, it will override the default expected
                                  statuses list with the status codes provided
                                  by caller function
        :returns: A tuple with the server response and the deserialized created
                 object.
        """
        body = self.serialize(data)
        uri = self.get_uri(resource, params=params)

        resp, body = self.post(uri, body=body, headers=headers,
                               extra_headers=extra_headers)

        if expected_statuses is None:
            self.expected_success(self.CREATE_STATUS_CODES, resp.status)
        else:
            self.expected_success(expected_statuses, resp.status)

        return resp, self.deserialize(resp, body)

    def _show_request(self, resource, uuid, headers=None, params=None,
                      extra_headers=False, uuid_prefix_char=None):
        """Gets a specific object of the specified type.
        :param resource: The name of the REST resource, e.g., 'zones'.
        :param uuid: Unique identifier of the object in UUID format.
        :param params: A Python dict that represents the query paramaters to
                       include in the request URI.
        :param extra_headers (bool): Boolean value than indicates if the
                                     headers returned by the get_headers()
                                     method are to be used but additional
                                     headers are needed in the request
                                     pass them in as a dict.
        :param uuid_prefix_char: applies to override hardcoded ('/')
                prefix UUID character. This parameter enables to set required
                by API character, for example ":" instead of "/".
        :returns: Serialized object as a dictionary.
        """
        uri = self.get_uri(resource, uuid=uuid, params=params,
                           uuid_prefix_char=uuid_prefix_char)

        resp, body = self.get(
            uri, headers=headers, extra_headers=extra_headers)

        self.expected_success(self.SHOW_STATUS_CODES, resp.status)

        return resp, self.deserialize(resp, body)

    def _list_request(self, resource, params=None, headers=None):
        """Gets a list of objects.
        :param resource: The name of the REST resource, e.g., 'zones'.
        :param params: A Python dict that represents the query paramaters to
                       include in the request URI.
        :param headers (dict): The headers to use for the request.
        :returns: Serialized object as a dictionary.
        """
        uri = self.get_uri(resource, params=params)

        resp, body = self.get(uri, headers=headers)

        self.expected_success(self.LIST_STATUS_CODES, resp.status)

        return resp, self.deserialize(resp, body)

    def _put_request(self, resource, uuid, data, params=None,
                     headers=None, extra_headers=False):
        """Updates the specified object using PUT request.
        :param resource: The name of the REST resource, e.g., 'zones'.
        :param uuid: Unique identifier of the object in UUID format.
        :param data: A Python dict that represents an object of the
                     specified type (to be serialized) or a plain string which
                     is sent as-is.
        :param headers (dict): The headers to use for the request.
        :param params: A Python dict that represents the query paramaters to
                       include in the request URI.
        :param headers (dict): The headers to use for the request.
        :param extra_headers (bool): Boolean value than indicates if the
                                     headers returned by the get_headers()
                                     method are to be used but additional
                                     headers are needed in the request
                                     pass them in as a dict.
        :returns: Serialized object as a dictionary.
        """
        body = self.serialize(data)
        uri = self.get_uri(resource, uuid=uuid, params=params)
        resp, body = self.put(
            uri, body=body, headers=headers, extra_headers=extra_headers)

        self.expected_success(self.PUT_STATUS_CODES, resp.status)

        return resp, self.deserialize(resp, body)

    def _update_request(self, resource, uuid, data, params=None, headers=None,
                        extra_headers=False, uuid_prefix_char=None):
        """Updates the specified object using PATCH request.
        :param resource: The name of the REST resource, e.g., 'zones'
        :param uuid: Unique identifier of the object in UUID format.
        :param data: A Python dict that represents an object of the
                     specified type (to be serialized) or a plain string which
                     is sent as-is.
        :param params: A Python dict that represents the query paramaters to
                       include in the request URI.
        :param headers (dict): The headers to use for the request.
        :param extra_headers (bool): Boolean value than indicates if the
                                     headers returned by the get_headers()
                                     method are to be used but additional
                                     headers are needed in the request
                                     pass them in as a dict.
        :param uuid_prefix_char: applies to override hardcoded ('/')
                prefix UUID character. This parameter enables to set required
                by API character, for example ":" instead of "/".
        :returns: Serialized object as a dictionary.
        """
        body = self.serialize(data)
        uri = self.get_uri(
            resource, uuid=uuid, params=params,
            uuid_prefix_char=uuid_prefix_char)

        resp, body = self.patch(uri, body=body,
                                headers=headers, extra_headers=extra_headers)

        self.expected_success(self.UPDATE_STATUS_CODES, resp.status)

        return resp, self.deserialize(resp, body)

    def _delete_request(self, resource, uuid, params=None, headers=None,
                        extra_headers=False):
        """Deletes the specified object.
        :param resource: The name of the REST resource, e.g., 'zones'.
        :param uuid: The unique identifier of an object in UUID format.
        :param params: A Python dict that represents the query paramaters to
                       include in the request URI.
        :param headers (dict): The headers to use for the request.
        :param extra_headers (bool): Boolean value than indicates if the
                                     headers returned by the get_headers()
                                     method are to be used but additional
                                     headers are needed in the request
                                     pass them in as a dict.
        :returns: A tuple with the server response and the response body.
        """
        uri = self.get_uri(resource, uuid=uuid, params=params)

        resp, body = self.delete(
            uri, headers=headers, extra_headers=extra_headers)

        self.expected_success(self.DELETE_STATUS_CODES, resp.status)
        if resp.status == 202:
            body = self.deserialize(resp, body)

        return resp, body

    def get_max_api_version(self):
        """Get the maximum version available on the API endpoint.
        :return: Maximum version string available on the endpoint.
        """
        response, body = self.get('/')
        self.expected_success(200, response.status)

        versions_list = json.loads(body)['versions']

        # Handle the legacy version document format
        if 'values' in versions_list:
            versions_list = versions_list['values']

        current_versions = (version for version in versions_list if
                            version['status'] == 'CURRENT')
        max_version = '0.0'
        for version in current_versions:

            ver_string = version['id']
            if ver_string.startswith("v"):
                ver_string = ver_string[1:]

            ver_split = list(map(int, ver_string.split('.')))
            max_split = list(map(int, max_version.split('.')))

            if len(ver_split) > 2:
                raise lib_exc.InvalidAPIVersionString(version=ver_string)

            if ver_split[0] > max_split[0] or (
                    ver_split[0] == max_split[0] and
                    ver_split[1] >= max_split[1]):
                max_version = ver_string

        if max_version == '0.0':
            raise lib_exc.InvalidAPIVersionString(version=max_version)

        return max_version
