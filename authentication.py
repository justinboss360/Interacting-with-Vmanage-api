import requests

url = "https://10.10.10.1:8443/j_security_check"

payload='j_username=xxx&j_password=********'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
