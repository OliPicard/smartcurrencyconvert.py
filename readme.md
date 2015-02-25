<h1>SmartCurrencyConvert.py</h1>
smartcurrencyconvert.py provides a simple command line interface/menu for quickly converting US Dollars to over 40 different currencies. (work in progress. Currently we have 15 currencies!)

smartcurrencyconvert uses [OpenExchangeRates APIs](https://openexchangerates.org/) to get the latest exchange rate (by the hour!) This means all data is live.

Currently supported conversions.

USD to Bitcoin (Powered by Coindesk via OpenExchangeRates)

USD to BRL

USD to GBP

USD to MXN

USD to EUR

USD to CNY

USD to CAD

USD to RUB

USD to AUD

USD to CHF

USD to XAU (Gold)

USD to XAG (Silver)

USD to ZAR

<h2>Install Instructions</h2>
We created this application with Python 3 in mind. Please download the Python 3 runtime.
You can download [Python 3 from python.org](http://python.org).


We used the Python Requests module. You can install Python Requests via PIP by running the following command.
<code>pip install requests</code>

Many Thanks to Kenneth Reitz for this awesome module!


We are using the OpenExchangeRates.org API. You can [sign up for free](https://openexchangerates.org/signup/free)
**Before running the script, be sure to copy over your AppID/API Key into the script** (open the script up in IDLE or a Text editor such as [Atom](http://atom.io)) and change the api-key ='?app_id=00000000000000000000000000000000' to the AppID key supplied by openexchange.org


<h3> License </h3>
The SmarCurrencyConvert.Py script is provided under the GNU GPL 3.0 License (Provided inside the Git Repo)

![GNU GPL 3.0](http://www.gnu.org/graphics/gplv3-127x51.png)

<h3> Credits </h3>
Many Thanks to the following people who helped with Questions, tips and support.

[/r/LearnPython](http://reddit.com/r/learnpython)

/u/TheGrumpyBrewer (for providing a basic analysis of how to fix my dry-run and providing tips on implimenting the program!)

wub_wub (for providing help with the joining .json statements.)

Freenode #Python (For providing me tips on using the requests module instead of urllib.)

OpenExchangeRates.org (for having an awesome, simple to use JSON api!)

Crafted with love by [OliPicard](https://olipicard.com)

a brief mention goes out to my other projects [convert.py](https://github.com/OliPicard/convert.py), [currencyconvert.py](https://github.com/OliPicard/currencyconvert.py) and [UpTime.py](https://github.com/OliPicard/UpTime.py)
