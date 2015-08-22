'''
SmartCurrencyConvert.py - https://github.com/OliPicard/smartcurrencyconvert.py/
Developed by OliPicard (github.com/olipicard)
Licenced under the GPL 3.0 licence.
'''
import requests
import requests.exceptions
import sys

api_key = "?app_id=00000000000000000000000000"  # please place your own API key here.
url = "https://openexchangerates.org/api/latest.json"


'''
Basic Maths - round 2 places
'''


def convert(x, y):
    a = (x * y)
    t = round(a, 2)
    return t

'''
main controller
'''


def letsgo(x):
    question = 'would you like to convert another amount? y/n '
    i = showtime()
    t = convert(i, data(currency='%s' % x))
    print(t)
    reload(input(question))

''' Model '''


def data(currency):
    payload = url + api_key
    try:
        json_obj = requests.get(payload)
        dataq = json_obj.json()
        back = dataq['rates'][currency]
        return back
    except requests.exceptions.MissingSchema:
        print('It seems the site has been modified. Have you considered checking to see '
              'if you have modified the site from https://openexchangerates.org/api/latest.json')


def showtime():
    d = input("Enter the amount: ")
    a = float(d)
    return a


def reload(resp):
    if resp == 'y':
        interface()
    if resp == 'n':
        sys.exit()


def interface():
    menu = 'Press 1 to convert to USD\nPress 2 to convert to GBP.\nPress 3 to convert to CAD.\n'\
           'Press 4 to convert to ERN\nPress 5 to convert to BTC\nPress 6 to convert to XUG\n' \
           'Press 7 to convert to XAG\nPress 8 to convert to MXN\nPress 9 to convert to BRL\n' \
           'Press 10 to convert to AUD\nPress 11 to convert to UGX\nPress 12 to convert to RUB\n' \
           'Press 13 to convert to BRL\nPress 14 to convert to CNY\nPress 15 to convert to CHF\n' \
           'Type exit to exit.'
    a = input(menu)
    if a == '1':
        letsgo('USD')
    if a == '2':
        letsgo('GBP')
    if a == '3':
        letsgo('CAD')
    if a == '4':
        letsgo('ERN')
    if a == '5':
        letsgo('BTC')
    if a == '6':
        letsgo('XAU')
    if a == '7':
        letsgo('XAG')
    if a == '8':
        letsgo('MXN')
    if a == '9':
        letsgo('BRL')
    if a == '10':
        letsgo('AUD')
    if a == '11':
        letsgo('UGX')
    if a == '12':
        letsgo('RUB')
    if a == '13':
        letsgo('BRL')
    if a == '14':
        letsgo('CNY')
    if a == '15':
        letsgo('CHF')
    if a == 'exit':
        sys.exit()


def main():
    interface()


if __name__ == "__main__":
    main()
