from WalletCreation import *
from SpendLockFunds import *
import sys

def main():
    mode = sys.argv[1]

    if mode == 'create':
        WalletCreation()
        return
    elif mode == 'spend':
        import argparse
        parser = argparse.ArgumentParser()

        parser.add_argument("-p", "--privatekey", help="Private key")
        parser.add_argument("-a", "--amount", help="Amount to send")
        parser.add_argument("-d", "--destination", help="Destination address")
        parser.add_argument("-n", "--walletname", help="Wallet name")

        args = parser.parse_args()

        private_key = args.privatekey
        amount = args.amount
        destination_address = args.destination
        wallet_name = args.walletname

        if private_key is None:
            private_key = input("Enter private key: ")
        
        if amount is None:
            amount = float(input("Amount to send: "))

        if destination_address is None:
            destination_address = input("Destination address: ")

        if wallet_name is None:
            wallet_name = input("Wallet name: ")

        wallet = OpenOrCreateWalletWithPrivKey(private_key=private_key, wallet_name=wallet_name)
        spendLockFunds(wallet=wallet, amount=amount, destination_address=destination_address)
    
if __name__ == "__main__":
    main()

    