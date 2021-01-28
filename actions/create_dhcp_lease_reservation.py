import pypureomapi
from lib.base_action import BaseAction


class CreateDHCPLeaseReservation(BaseAction):
    def run(
        self,
        reserved_ip,
        mac_addr,
        auth_key_name,
        auth_key,
        server_name,
        dhcp_host,
        dhcp_port=7911
    ):
        try:
            # cast auths as bytes
            o = pypureomapi.Omapi(
                dhcp_host, dhcp_port,
                auth_key_name.encode(),
                auth_key.encode()
            )
            response = o.add_host_supersede_name(
                reserved_ip,
                mac_addr,
                server_name
            )
            print("reservation created  for host:")
            print("%s: %s -> %s" % (server_name, reserved_ip, mac_addr))
            return response
        except pypureomapi.OmapiError as err:
            print("error creating host: %s " % str(err))
            return err
