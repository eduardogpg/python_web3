cleaimport json
import requests

from web3 import Web3

bsc = 'https://bsc-dataseed.binance.org/'
web3 = Web3(Web3.HTTPProvider(bsc))

ACCESS_TOKEN = 'RZNYKJYMA5KEK1WXK1NCNK7C3F3R27APM3'

def get_abi(address):
    url = f'https://api.bscscan.com/api?module=contract&action=getabi&address={address}&apikey={ACCESS_TOKEN}'
    response = requests.get(url)
    
    if response.status_code == 200:
        payload = response.json()['result']
        data = json.loads(payload)
        
        with open('contract.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        return data


def main():
    if web3.isConnected():
        print(web3.eth.blockNumber)
        
        balance = web3.eth.getBalance('0x9eABE3d0fd1dc5D2846c44047f3d92e7c1904dA3')
        print( web3.fromWei(balance, 'ether') )
        
        nominex_contract = Web3.toChecksumAddress('0xd32d01a43c869edcd1117c640fbdcfcfd97d9d65')
        abi = get_abi(nominex_contract)
        
        contract = web3.eth.contract(address=nominex_contract, abi=abi)
        
        name = contract.functions.name().call()
        symbol = contract.functions.symbol().call()
        total_supply = contract.functions.totalSupply().call()
        
        balanace = contract.functions.balanceOf('0x9eABE3d0fd1dc5D2846c44047f3d92e7c1904dA3').call()
        balanace = web3.fromWei(balanace, 'ether')
        
        print(name)
        print(symbol)
        print(total_supply)
        print(balanace)
    
main()