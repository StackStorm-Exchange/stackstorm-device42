import requests
from st2common.runners.base_action import Action
from six.moves.urllib.parse import urlparse


class Device42BaseException(Exception):
    pass


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)

        self.d42_server = self.config.get('d42_server', None)
        # self.d42_server += self.config.get('d42_api_path', None)

        if not self.d42_server:
            raise ValueError('"d42_server" config value is required')
            # d42_server should be aproximately -> https://00.00.00.00/api/1.0/

        self.d42_username = self.config.get('d42_username', None)
        if not self.d42_username:
            raise ValueError('"d42_username" config value is required')

        self.d42_password = self.config.get('d42_password', None)
        if not self.d42_password:
            raise ValueError('"d42_password" config value is required')

        self.verify = self.config.get('verify_certificate', False)

        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def getAPI(self, endpoint, params, headers=None):

        if headers is None:
            headers = self.headers

        r = requests.get(
            "%s%s" % (self.d42_server, endpoint),
            params=params,
            auth=(self.d42_username, self.d42_password),
            verify=self.verify,
            headers=headers
        )
        if r.ok:
            return r.json()
        else:
            return r

    def putAPI(self, endpoint, params=None, payload=None):
        r = requests.put(
            "%s%s" % (self.d42_server, endpoint),
            params=params,
            data=payload,
            auth=(self.d42_username, self.d42_password),
            verify=self.verify
        )
        if r.ok:
            return r.json()
        else:
            return r

    def postAPI(self, endpoint, params=None, payload=None):
        r = requests.post(
            "%s%s" % (self.d42_server, endpoint),
            params=params,
            data=payload,
            auth=(self.d42_username, self.d42_password),
            verify=self.verify
        )
        if r.ok:
            return r.json()
        else:
            return r

    def post(
        self,
        endpoint,
        headers=None,
        params=None,
        payload=None,
        doql_query=None
    ):

        # allow for the doql_query input parameter to call D42 via the
        # doql API URI not the regular API
        if doql_query is True:
            d42_url_split = urlparse(self.d42_server)
            d42_server = "%s://%s/" % (
                d42_url_split.scheme, d42_url_split.netloc
            )
            print("d42_server: %s" % d42_server)
        else:
            d42_server = self.d42_server

        url = "%s%s" % (d42_server, endpoint)
        r = requests.post(
            url=url,
            auth=('admin', 'adm!nd42'),
            headers=headers,
            params=params,
            data=payload,
            verify=self.verify,
        )
        print("url: %s" % url)
        if r.ok:
            if doql_query is True:
                return r
            else:
                return r.json()
        else:
            return r
