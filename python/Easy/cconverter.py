import requests
import json


def converter(currency):
    r = requests.get('https://www.floatrates.com/daily/' + currency + '.json')
    json_string = r.content
    with open('rates.json', 'wb') as json_file:
        json_file.write(json_string)


rate = input()
converter(rate)

with open('rates.json', 'r') as json_file:
    py_object = json.load(json_file)

empty_list = ['eur', 'usd']
while True:
    exchange = input()
    if exchange == '':
        break
    amount = float(input())
    print('Checking the cache...')
    if str(exchange) in empty_list:
        print('Oh! It is in the cache!')
        converted = amount * py_object[exchange]['rate']
        print('You received ' + str(converted) + ' ' + str(exchange))
        empty_list.append(str(exchange))
    else:
        print('Sorry, but it is not in the cache!')
        converted = amount * py_object[exchange]['rate']
        print('You received ' + str(converted) + ' ' + str(exchange))
        empty_list.append(str(exchange))
