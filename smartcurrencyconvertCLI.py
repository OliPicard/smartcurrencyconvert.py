__author__ = 'OliPicard'
import math
import re
import requests
import requests.exceptions
import json
import json.decoder

#===========================#
#SmartCurrencyConvertCLI.py #
#===========================#

# Full Open Source code (GPL 3.0) is avalible from https://github.com/OliPicard/smartcurrencyconvert.py

#Please input your API key before running this script! (It will fail to compile otherwise.)

api_key = '00000000000000000000000000000000000000'#insert your API code here.
url = 'http://openexchangerates.org/api/latest.json?app_id=' #don't change this unless you know what your doing.

payload = (url + api_key)

try:
    json_obj = requests.get(payload)
    dataq = json_obj.json()
except requests.exceptions.MissingSchema:
    print('It seems the site has been modified. Have you considered checking to see if you have modified the site from https://openexchangerates.org/api/latest.json')
except requests.exceptions.Timeout:
    print('The API is timing out, please try again later.')

convert=input('')

words = re.findall(r'[a-z]|[A-Z]',convert) #regexing the letters.
numbers = re.findall(r'\d+',convert) #regexing the numbers.
result = [float (n) for n in numbers] #converting the regex numbers into whole numbers.


if words == ['u', 's', 'd', 'e', 'u', 'r']: #lowercase EUR
    a = result[0]
    b = dataq['rates']['EUR']
    c = (a * b)
    print ('=>',c)
    input('press [enter] to exit.')
if words == ['U', 'S', 'D', 'E', 'U', 'R']: #uppercase EUR
    a = result[0]
    b = dataq['rates']['EUR']
    c = (a * b)
    print ('=>',c)
    input('press [enter] to exit.')
if words == ['u','s','d','b','t','c']:
    a = result[0]
    b = dataq ['rates']['BTC']
    c = (a * b)
    print ('=>',c)
    input('press [enter] to exit.')
if words == ['U','S','D','B','T','C']: #uppercase btc
    a = result [0]
    b = dataq['rates']['BTC']
    c = a * b
    print ('=>',c)
    input('press [enter] to exit.')
if words == ['U','S','D','G','B','P']:
    a = result [0]
    b = dataq['rates']['GBP']
    c = a * b
    print ('=>', c)
    input('press [enter] to exit.')
if words == ['u','s','d','g','b','p']:
    a = result [0]
    b = dataq['rates']['GBP']
    c = a * b
    print ('=>', c)
    input('press [enter] to exit.')
if words == ['U','S','D','X','A','U']:
    a = result [0]
    b = dataq['rates']['XAU']
    c = a * b
    print ('=>', c)
    input('press [enter] to exit.')
if words == ['u','s','d','x','a','u']:
    a = result[0]
    b = dataq['rates']['XAU']
    c = a * b
    print('=>', c)
    input('press [enter] to exit.')
if words == ['U','S','D','X','A','G']:
    a = result [0]
    b = dataq[0]
    b = dataq['rates']['XAG']
    c = a * b
    print('=>', c)
    input('press [enter] to exit.')
if words == ['u','s','d','x','a','g']:
    a = result [0]
    b = dataq['rates']['XAG']
    c = a * b
    print('=>', c)
    input('press [enter] to exit.')
if words == ['U','S','D','M','X','N']:
    a = result [0]
    b = dataq['rates']['MXN']
    c = a * b
    print('=>',c)
    input('press [enter] to exit.')
if words == ['u','s','d','m','x','n']:
    a = result[0]
    b = dataq['rates']['MXN']
    c = a * b
    print ('=>',c)
    input('press [enter] to exit.')
if words == ['U','S','D','B','R','L']:
    a = result[0]
    b = dataq['rates']['BRL']
    c = a * b
    print('=>',c)
    input('press [enter] to exit.')
if words == ['u','s','d','b','r','l']:
    a = result[0]
    b = dataq['rates']['BRL']
    c = a * b
    print('=>',c)
    input('press [enter] to exit.')
if words == ['U','S','D','C','A','D']:
    a = result [0]
    b = dataq['rates']['CAD']
    c = a * b
    print ('=>',c)
if words == ['u','s','d','c','a','d']:
    a = result[0]
    b = dataq['rates']['CAD']
    c = a * b
    print('=>',c)
    input('press [enter] to exit.')
if words == ['U','S','D','A','U','D']:
    a = result[0]
    b = dataq['rates']['AUD']
    c = a * b
    print('=>',c)
    input('press [enter] to exit.')
if words == ['u','s','d','a','u','d']:
    a = result[0]
    b = dataq['rates']['aud']
    c = a * b
    print('=>',c)
    input('press [enter] to exit')

