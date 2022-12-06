import requests

url = "https://172.16.62.138:8443/dataservice/device/action/status/push_feature_template_configuration-3ade0ed0-3d21-41ba-8dbe-3023b933369a"

payload={}
headers = {
  'X-XSRF-TOKEN': 'BC2C5E59B98C92835122D8117D03B7DC78B7546FC8FDF0D4B03ECBB5DA3DCD7404705E9C827EAF3F1B4B583936B49C690316',
  'Cookie': 'JSESSIONID=DV-TMeAg8twtQnJqg8NL39b-WYdhOoVeB6WprrAL.0dd44fb1-5a89-4436-b21c-198db941bb0f'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)