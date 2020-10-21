import json
import requests
import urllib.request

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# main control 
def main():
    coins = get_coins()
    bitcoin_rate = convert_bitcoins_to_dollars(coins)
    display_results(coins, bitcoin_rate)

# getting the number of coins and testing so user only enter valid entities 
def get_coins():
    while True:
        try:
            dollars = float(input('Enter the number of coins: '))
            if dollars >= 0:
                return dollars
            else:
                print('Enter a number greater than 0')
        except ValueError:
            print('Enter a valid number.')


#convertion of number of coin into us dollars
def convert_bitcoins_to_dollars(coins):
    exchange_rate = requests_rate(coins)
    bitcoin = math_conversion(coins, exchange_rate)
    return bitcoin


#requesting and pulling data from the database
def requests_rate(rate):
    try:
        response = requests.get(url)
        data = response.json()
        dollars_exchange_rate = data['bpi']['USD']['rate_float']
        return(dollars_exchange_rate)
    except Exception as e:
        print(f'Error making request', 0)

#Math conversion coins times bitcoin rate
def math_conversion(coins, bitcoin_rate):
    return coins * bitcoin_rate

#ptinting the output 
def display_results(coins, bitcoin_rate):
    print(f'{coins} coins is equal to ${bitcoin_rate:.2f}')




if __name__ == '__main__':
    main()
