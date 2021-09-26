# Python-Assignment-1


## Title: 

Pulls the data from coingecko.com and filters out top N cryptocurrencies by market capitalization.

## Installation

You must install pycoingecko library to work with this program

PyPI
```
pip install pycoingecko
```
  
or from source
```
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

## Usage

To read data from API use
```
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

## Examples

Enter the number in console
```
number = int(input('Enter the number of coins: '))
```

You enter 4, the result: 
Enter the number of coins: 4
1 : Bitcoin 816866713014 
2 : Ethereum 356772871514
3 : Cardano 73070958410  
4 : Tether 69570075821   

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
