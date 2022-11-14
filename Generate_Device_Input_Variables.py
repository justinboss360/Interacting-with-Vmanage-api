import requests
import json

url = "https://10.10.10.1:8443/dataservice/template/device/config/input"

payload = json.dumps({
  "templateId": "6afd3d0a-47a3-4096-a1e1-01f3342a4e02",
  "deviceIds": [
    "ISR4331/K9-FDO23140Y3Q"
  ],
  "isEdited": False,
  "isMasterEdited": False
})
headers = {
  'X-XSRF-TOKEN': 'FCC01EA950D48D453017F54BCB2F30ED6318DD58370D260A9E99C0F481C945B5AD24B8A437CE05D99344A3DD2256C81B5CCB',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
