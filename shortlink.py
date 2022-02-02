import pyshorteners
url="vscode://vscode.github-authentication/did-authenticate?windowid=1&code=97206c805d62abd81a7a&state=2435d842-e388-4504-925d-2e4c6e293e8b"
link=pyshorteners.Shortener()
sh=link.tinyurl.short(url)
print(sh)
