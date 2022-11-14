import requests

url = "https://10.10.10.1:8443/dataservice/client/token"

payload={}
headers = {
  'X-XSRF-TOKEN': 'FCC01EA950D48D453017F54BCB2F30ED6318DD58370D260A9E99C0F481C945B5AD24B8A437CE05D99344A3DD2256C81B5CCB'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
