from bisect import bisect_right
from operator import contains
import re
from urllib import request
from django.shortcuts import render, redirect
import datetime
import requests
from django.http import HttpResponse
import datetime
from django.template.loader import render_to_string

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def home(request):

    return render(request, 'HTML/home.html')


def dolar(request):
    cota = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
    usd = {'usd': cota['USDBRL']['bid']}
    num = str(usd['usd'])
    corte = str('00.0')
    usdbid = num[:len(corte)]
    

    usd1 = {'usd': cota['USDBRL']['low']}
    num1 = str(usd1['usd'])
    usdlow = num1[:len(corte)]

    usd2 = {'usd': cota['USDBRL']['high']}
    num2 = str(usd2['usd'])
    usdhigt = num2[:len(corte)]
    
    usddicts = {'usddict_low': usdlow, 'usddict_bid': usdbid, 'usddict_higt': usdhigt }

    return render(request, 'HTML/dolar.html', usddicts)


def euro(request):
    cota = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
    euro = {'euro': cota['EURBRL']['bid']}
    num = str(euro['euro'])
    corte = str('00.0')
    eurobid = num[:len(corte)]

    euro1 = {'euro': cota['EURBRL']['low']}
    num1 = str(euro1['euro'])
    eurolow = num1[:len(corte)]

    euro2 = {'euro': cota['EURBRL']['high']}
    num2 = str(euro2['euro'])
    eurohigt = num2[:len(corte)]

    eurodicts = {'euro_low': eurolow, 'euro_bid': eurobid, 'euro_higt': eurohigt}

    return render(request, 'HTML/euro.html', eurodicts)

def bitcoin(request):
    cota = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
    bitcoin = {'bitcoin': cota['BTCBRL']['bid']}
    num = str(bitcoin['bitcoin'])
    corte = str('00.0000')
    bitcoinbid = num[:len(corte)]

    bitcoin1 = {'bitcoin': cota['BTCBRL']['low']}
    num1 = str(bitcoin1['bitcoin'])
    bitcoinlow = num1[:len(corte)]

    bitcoin2 = {'bitcoin': cota['BTCBRL']['high']}
    num2 = str(bitcoin2['bitcoin'])
    bitcoinhigh = num2[:len(corte)]

    bitdicts = {'bitdict_bid': bitcoinbid, 'bitcoin_low':bitcoinlow, 'bitcoin_high': bitcoinhigh }
    
    return render(request, 'HTML/bitcoin.html', bitdicts)
