import requests
import json

url = "https://10.10.10.1:8443/dataservice/template/device/config/attachfeature"

payload = json.dumps({
  "deviceTemplateList": [
    {
      "templateId": "c566d38e-2219-4764-a714-4abeeab607dc",
      "device": [
        {
          "csv-status": "complete",
          "csv-deviceId": "ISR4331/K9-FDO23140Y3Q",
          "csv-deviceIP": "172.45.1.32",
          "csv-host-name": "NG_LA_BO_0092_F01_CE01",
          "//switchport/interface/GigabitEthernet0/1/0/switchport/trunk/allowed/vlan/vlans": "1,43,1021-1023,2045-2046,3397-3399",
          "/43/VPN_43_SVI_Name/interface/if-name": "Vlan43",
          "/43/VPN_43_SVI_Name/interface/ip/address": "10.210.92.26/30",
          "/43//router/bgp/neighbor/VPN_43_bgp_neighbor_add/address": "10.210.92.25",
          "/3/VPN_3_SVI_Name/interface/if-name": "Vlan3399",
          "/3/VPN_3_SVI_Name/interface/ip/address": "10.210.92.42/30",
          "/3//router/bgp/neighbor/VPN_3_bgp_neighbor_add/address": "10.210.92.41",
          "/2/VPN_2_SVI_Name/interface/if-name": "Vlan3398",
          "/2/VPN_2_SVI_Name/interface/ip/address": "10.210.92.38/30",
          "/2//router/bgp/neighbor/VPN_2_bgp_neighbor_add/address": "10.210.92.37",
          "/1/Loopback12/interface/ip/address": "172.16.164.18/32",
          "/1/Loopback11/interface/ip/address": "172.16.188.18/32",
          "/1/Loopback10/interface/ip/address": "172.16.2.156/32",
          "/1/VPN_1_SVI_Name/interface/if-name": "Vlan3397",
          "/1/VPN_1_SVI_Name/interface/ip/address": "10.210.92.34/30",
          "/1//router/bgp/neighbor/VPN_1_bgp_neighbor_add/address": "10.210.92.33",
          "/0/vpn-instance/ip/route/0.0.0.0/0/next-hop/vpn_0_next_hop_ip_address_1/address": "192.168.24.78",
          "/0/vpn-instance/ip/route/0.0.0.0/0/next-hop/vpn_0_next_hop_ip_address_2/address": "172.26.3.29",
          "/0/Type2_vpn_0_interface_name_2/interface/if-name": "GigabitEthernet0/0/1",
          "/0/Type2_vpn_0_interface_name_2/interface/description": "SP2",
          "/0/Type2_vpn_0_interface_name_2/interface/ip/address": "172.26.3.30/30",
          "/0/Type2_vpn_0_interface_name_2/interface/shaping-rate": "10000",
          "/0/Type2_vpn_0_interface_name_1/interface/if-name": "GigabitEthernet0/0/0",
          "/0/Type2_vpn_0_interface_name_1/interface/description": "SP1",
          "/0/Type2_vpn_0_interface_name_1/interface/ip/address": "192.168.24.51/24",
          "/0/Type2_vpn_0_interface_name_1/interface/shutdown": "false",
          "/0/Type2_vpn_0_interface_name_1/interface/shaping-rate": "10000",
          "//system/host-name": "NG_LA_BO_0092_F01_CE01",
          "//system/system-ip": "172.45.1.32",
          "//system/site-id": "124130"
        }
      ],
      "isEdited": False,
      "isMasterEdited": False
    }
  ]
})
headers = {
  'X-XSRF-TOKEN': '',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
