from lib.base_action import BaseAction


class SuggestNextIp(BaseAction):
    def run(self, subnet_id=None, subnet=None, name=None,
            vrf_group_id=None, vrf_group=None,
            reserved_ip=None, return_ip_only=0
            ):
        response = self.getAPI("/suggest_ip/", {
            "subnet_id": subnet_id,
            "subnet": subnet,
            "name": name,
            "vrf_group_id": vrf_group_id,
            "vrf_group": vrf_group,
            "reserved_ip": reserved_ip,
        })
        if not return_ip_only:
            return response
        else:
            return response['ip']
