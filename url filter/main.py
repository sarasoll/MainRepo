import urllib.request
data=urllib.request.urlopen('http://www.google.com')
print(data.read(500).decode('utf-8'))