import requests
res=requests.get("https://ipinfo.io/")
data=res.json()
print("ip= "+data[' Ur ip... '])
print('from= '+data['U R from... '])




