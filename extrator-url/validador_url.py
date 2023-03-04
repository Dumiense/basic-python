import re

url = 'bytebank.com/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError('a url não é válida')

else:
    print('a url é válida')