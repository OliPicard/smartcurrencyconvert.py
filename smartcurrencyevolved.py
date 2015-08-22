'''
SmartCurrencyConvert.py - https://github.com/OliPicard/smartcurrencyconvert.py/
Developed by OliPicard (github.com/olipicard)
Licenced under the GPL 3.0 licence.
'''
import requests
import requests.exceptions
import sys

api_key = "?app_id=00000000000000000000000000000000"  # please place your own API key here.
url = "https://openexchangerates.org/api/latest.json"


def convert(x, y):
    a = (x * y)
    t = round(a, 2)
    return t


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
        check()
    if resp == 'n':
        sys.exit()


def check():
    menu = 'Press 1 to convert to USD\nPress 2 to convert to GBP.\nPress 3 to convert to CAD.\n'\
           'Press 4 to convert to ERN\nPress 5 to convert to BTC\nPress 6 to convert to XUG\n' \
           'Press 7 to convert to XAG\nPress 8 to convert to MXN\nPress 9 to convert to BRL\n' \
           'Press 10 to convert to AUD\nPress 11 to convert to UGX\nType exit to exit.'
    a = input(menu)
    question = 'would you like to convert another number? y/n'
    if a == '1':
        i = showtime()
        t = convert(i, data(currency='USD'))
        print(t)
        reload(input(question))
    if a == '2':
        i = showtime()
        t = convert(i, data(currency='GBP'))
        print(t)
        reload(input(question))
    if a == '3':
        i = showtime()
        t = convert(i, data(currency='CAD'))
        print(t)
        reload(input(question))
    if a == '4':
        i = showtime()
        t = convert(i, data(currency='ERN'))
        print(t)
        reload(input(question))
    if a == '5':
        i = showtime()
        t = convert(i, data(currency='BTC'))
        print(t)
        reload(input(question))
    if a == '6':
        i = showtime()
        t = convert(i, data(currency='XAU'))
        print(t)
        reload(input(question))
    if a == '7':
        i = showtime()
        t = convert(i, data(currency='XAG'))
        print(t)
        reload(input(question))
    if a == '8':
        i = showtime()
        t = convert(i, data(currency='MXN'))
        print(t)
        reload(input(question))
    if a == '9':
        i = showtime()
        t = convert(i, data(currency='BRL'))
        print(t)
        reload(input(question))
    if a == '10':
        i = showtime()
        t = convert(i, data(currency='AUD'))
        print(t)
        reload(input(question))
    if a == '11':
        i = showtime()
        t = convert(i, data(currency='UGX'))
        print(t)
        reload(input(question))
    if a == '12':
        i = showtime()
        t = convert(i, data(currency='RUB'))
        print(t)
        reload(input(question))
    if a == '13':
        i = showtime()
        t = convert(i, data(currency='CNY'))
        print(t)
        reload(input(question))
    if a == '14':
        i = showtime()
        t = convert(i, data(currency='CNY'))
        print(t)
        reload(input(question))
    if a == '15':
        i = showtime()
        t = convert(i, data(currency='CHF'))
        print(t)
        reload(input(question))
    if a == 'exit':
        sys.exit()


def main():
    check()


if __name__ == "__main__":
    main()
