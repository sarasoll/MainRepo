import requests
res=requests.get("https://ipinfo.io/")
data=res.json()
print("ip= "+data['ip'])
print('from= '+data['from'])
