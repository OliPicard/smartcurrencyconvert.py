# coding: utf-8

__author__ = 'OliPicard'
import requests
import requests.exceptions
import json.decoder
import json

#SmartCurrencyConvert.py - http://github.com/smartcurrencyconvert.py
#Developed by OliPicard
#Licenced under the GPL 3.0 Licence. (Included in the repo.)

api_key = '?app_id=13cd00020d8547ee9a452e8b2314a2ee'  # change this to your API/APPID key, include the ? too!

url = ('https://openexchangerates.org/api/latest.json')  # Default API URL. Do not change this!




#--------------------------#
# HTTPs Handling           #
#--------------------------#

payload = (url + api_key) #combining the URL with the API key.

#print(payload)
try:
   json_obj = requests.get(payload)
   dataq = json_obj.json() #Thank you Wub_Wub from LearnPython. You are awesome!
except requests.exceptions.MissingSchema as site_one:
    print('It seems the site has been modified. Have you considered checking to see if you have modified the site from https://openexchangerates.org/api/latest.json')
except requests.exceptions.Timeout:
    print('It seems the API is timing out. Please try again later.')





#----------------------#
#        Menu          #
#----------------------#

def menu():
    print("-" * 25)
    print("Welcome to the SmartCurrencyConvert.py script.\n Please read the setup instructions at https://github.com/olipicard before use.")
    print(".1 USD to GBP")
    print(".2 USD to BTC")
    print(".3 USD to EUR")
    print(".4 USD to XAU")
    print(".5 USD to XAG")
    print(".6 USD to MXN")
    print(".7 USD to BRL")
    print(".8 USD to CAD")
    print(".9 USD to AUD")
    print(".10 USD to UGX")
    print(".11 USD to RUB")
    print(".12 USD to CNY")
    print(".13 USD to CHF")
    print(".14 USD to ZAR")
    print(".15 To Quit/Terminate the Application.")
    print("-" * 25)

#----------------------#
#    The variables     #
#----------------------#

def usd_to_gbp(a):
    b = dataq['rates']['GBP']
    c = a * b
    return(a, float(c))

def usd_to_btc(a):
    b = dataq['rates']['BTC']
    c = a * b
    return(a, float(c))

def usd_to_eur(a):
    b = dataq['rates']['EUR']
    c = a * b
    return(a, float(c))


def usd_to_xau(a):
    b = dataq['rates']['XAU']
    c = a * b
    return(a, float(c))

def usd_to_xag(a):
    b = dataq['rates']['XAG']
    c = a * b
    return(a, float(c))

def usd_to_mxn(a):
    b = dataq['rates']['MXN']
    c = a * b
    return(a, float(c))

def usd_to_brl(a):
    b = dataq['rates']['BRL']
    c = a * b
    return(a, float(c))

def usd_to_cad(a):
    b = dataq['rates']['CAD']
    c = a * b
    return(a, float(c))

def usd_to_aud(a):
    b = dataq['rates']['AUD']
    c = a * b
    return(a, float(c))

def usd_to_ugx(a):
    b = dataq['rates']['UGX']
    c = a * b
    return(a, float(c))

def usd_to_rub(a):
    b = dataq['rates']['RUB']
    c = a * b
    return(a, float(c))

def usd_to_cny(a):
    b = dataq['rates']['CNY']
    c = a * b
    return(a, float(c))

def usd_to_chf(a):
    b = dataq['rates']['CHF']
    c = a * b
    return(a, float(c))

def usd_to_zar(a):
    b = dataq['rates']['ZAR']
    c = a * b
    return(a, float(c))

def check_input(user_input):
    try:
        converted_number = float (user_input)
    except ValueError:
        return -1
    return converted_number


##############
#logic       #
##############
loop = True
while loop:
    menu()
    choice=int(input('Please pick an item from the menu and press enter to confirm. '))
    if choice not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        print('Sorry that number is invaild. Please pick an item from the menu again.')
        menu()
        choice=int(input('Pick an item from the menu.'))
    if choice == 1:
        print("Converting US Dollars (USD) to Great British Pounds (GBP)")
        usd = check_input(input('$'))
        result = usd_to_gbp(usd)
        print('-' * 25)
        print('$ {} = £ {}'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 2:
        print("Converting US Dollars (USD) to Bitcoins (BTC)")
        usd = check_input(input('$'))
        result = usd_to_btc(usd)
        print('-' * 25)
        print('$ {} = btc {}'.format(*result))
        escape = input('Press [Enter] to return back to the main menu.')
    if choice == 3:
        print("Converting US Dollars (USD) to Euros (EUR)")
        usd = check_input(input('$'))
        result = usd_to_eur(usd)
        print ('-' * 25)
        print ('${} = EUR{}'.format(*result))
        escape = input('Press [Enter] to return back to the main menu.')
    if choice == 4:
        print('Converting US Dollars (USD) to (XAU) Gold -troy ounce')
        usd = check_input(input('$'))
        result = usd_to_xau(usd)
        print('-' * 25)
        print('$ {} = {} XAU'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 5:
        print('Converting US Dollars (USD) to (XAG) Silver -troy ounce')
        usd = check_input(input('$'))
        result = usd_to_xag(usd)
        print ('-' * 25)
        print('$ {} = {} XAG'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 6:
        print('Converting US Dollars (USD) to Mexican Peso (MXN)')
        usd = check_input(input('$'))
        result = usd_to_mxn(usd)
        print ('-' * 25)
        print('${} USD = ${} MXN'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 7:
        print('Converting US Dollars (USD) to Brazilian Real (BRL)')
        usd = check_input(input('$'))
        result = usd_to_brl(usd)
        print('$ {} = R$ {}'.format(*result))
        escape = input ('Press any key to return back to the main menu.')
    if choice == 8:
        print('Converting US Dollars (USD) to Canadian Dollars (CAD)')
        usd = check_input(input('$'))
        result = usd_to_cad(usd)
        print('$ USD {} = $ {} CAD'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 9:
        print('Converting US Dollars (USD) to Australian Dollars (AUD)')
        usd = check_input(input('$'))
        result = usd_to_aud(usd)
        print('$ USD {} = $ {} AUD'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 10:
        print ('Converting US Dollars (USD) to Ugandan Shillings (UGX)')
        usd = check_input(input('$'))
        result = usd_to_ugx(usd)
        print('$ USD {} = {} Ugandan Shillings (UGX)'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 11:
        print('Converting US Dollars (USD) to Russian Rubles (RUB)')
        usd = check_input(input('$'))
        result = usd_to_rub(usd)
        print('${} = ₽{}'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 12:
        print('Converting US Dollars (USD) to Chinese Yuan (CNY)')
        usd = check_input(input('$'))
        result = usd_to_cny(usd)
        print('${} = ¥ {}'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 13:
        print('Converting US Dollars (USD) to Swiss Franc (CHF)')
        usd = check_input(input('$'))
        result = usd_to_chf(usd)
        print('${} = CHF{}'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 14:
        print('Converting US Dollars (USD) to South African Rand (ZAR)')
        usd = check_input(input('$'))
        result = usd_to_zar(usd)
        print('$ {} = R{}'.format(*result))
        escape = input('Press any key to return back to the main menu.')
    if choice == 15:
        print('Thank you for using the SmartCurrencyConvert.py script!\nIf you found any bugs feel free to open a ticket at http://github.com/olipicard')
        escape = input('press any key to terminate the application.')
        loop = False
