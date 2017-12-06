import requests
from st2common.runners.base_action import Action


class Device42BaseException(Exception):
    pass


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)

        self.d42_server = self.config.get('d42_server', None)
        if not self.d42_server:
            raise ValueError('"d42_server" config value is required')

        self.d42_username = self.config.get('d42_username', None)
        if not self.d42_username:
            raise ValueError('"d42_username" config value is required')

        self.d42_password = self.config.get('d42_password', None)
        if not self.d42_password:
            raise ValueError('"d42_password" config value is required')

        self.verify = self.config.get('verify_certificate', False)

    def getAPI(self, endpoint, params):
        r = requests.get(
            "%s%s" % (self.d42_server, endpoint),
            params=params,
            auth=(self.d42_username, self.d42_password),
            verify=self.verify
        )
        if r.ok:
            return r.json() 
        else: 
            # return "url - %s%s \n response - %s" % (self.d42_server, endpoint, r)         
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

    def post(self, endpoint, headers=None, params=None, payload=None):

        r = requests.post(
                url="%s%s" % (self.d42_server, endpoint),
                auth=('admin', 'adm!nd42'),
                params=params,
                data=payload,
                verify=self.verify,
        )

        if r.ok:
            return r.json()
        else:
            return r
