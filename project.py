from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
res = cg.get_coins_markets(vs_currency='usd')
def myFunction(length):
    listOfMarketCaps = []
    listOfNames = []
    for i in range(length):
        listOfMarketCaps.append(int(res[i]['market_cap']))
        listOfNames.append(res[i]['name'])

    for i in range(length):
        print(i + 1, ':', listOfNames[i], listOfMarketCaps[i])

number = int(input('Enter the number of coins: '))
myFunction(number)