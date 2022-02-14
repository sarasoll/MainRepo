import urllib.request
import urllib
url = input("Enter the Host...")
req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
cookies = response.info()['Set-Cookie']
cookies = response.read()
response.close()
print(cookies, content)
