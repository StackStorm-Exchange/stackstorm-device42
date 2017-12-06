from lib.base_action import BaseAction


class CreateIP(BaseAction):
    def run(self, subnet=None, 
            vrf_group_id=None, vrf_group=None,
            ipaddress=None, macaddress=None, ip_type=None, tags=None,
            device_name=None, available=None, clear_all=None
            ):
        response = self.post("ips/", {
            #"subnet": subnet,
            "ipaddress": ipaddress,
            "type": ip_type,
            "tags": tags,
            #"vrf_group_id": vrf_group_id,
            #"vrf_group": vrf_group,
            #"device": device_name,
            #"available": available,
            #"clear_all": clear_all
        })

        return response.text
