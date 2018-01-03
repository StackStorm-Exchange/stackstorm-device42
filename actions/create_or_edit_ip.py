from lib.base_action import BaseAction


class CreateIP(BaseAction):
    def run(self, subnet=None, 
            vrf_group_id=None, vrf_group=None,
            ipaddress=None, macaddress=None, ip_type=None, tags=None,
            device_name=None, available=None, clear_all=None,
            debug=False):
        
        payload = {
            "ipaddress": ipaddress, "subnet": subnet,
            "macaddress": macaddress, "ip_type": ip_type,
            "tags": tags, "device": device_name
        }

        print("payload: %s" % payload)
        d42_headers = {'Accept': 'application/json'} 
        response = self.post( endpoint="ips/", payload=payload, headers=d42_headers)
        
        if type(response) is dict:  # d42 api agent returns response.json(0) if response.ok...:
            return response
        else:
            return response.text 
