from WalletCreation import *
from SpendLockFunds import *
import sys
import argparse

def create_wallet(args):
    WalletCreation()

def spend_mode(args):
    private_key = args.privatekey or input("Enter private key: ")
    amount = float(args.amount) or float(input("Amount to send: "))
    destination_address = args.destination or input("Destination address: ")
    wallet_name = args.walletname or input("Wallet name: ")

    wallet = OpenOrCreateWalletWithPrivKey(private_key=private_key, wallet_name=wallet_name)
    spendLockFunds(wallet=wallet, amount=amount, destination_address=destination_address)

def main():
    parser = argparse.ArgumentParser(description="Manage Bitcoin wallets and perform transactions.")
    subparsers = parser.add_subparsers(dest='mode', help='Available modes: wallet, spend')

    # Wallet mode
    wallet_parser = subparsers.add_parser('wallet', help='Create a new wallet')
    wallet_parser.set_defaults(func=create_wallet)

    # Spend mode
    spend_parser = subparsers.add_parser('spend', help='Send an amount of tBTC to a destination address using your wallet')
    spend_parser.add_argument("-p", "--privatekey", help="Private key")
    spend_parser.add_argument("-a", "--amount", help="Amount to send")
    spend_parser.add_argument("-d", "--destination", help="Destination address")
    spend_parser.add_argument("-n", "--walletname", help="Wallet name")
    spend_parser.set_defaults(func=spend_mode)

    if len(sys.argv) < 2 or sys.argv[1] in ['help', '--help', None]:
        parser.print_help()
        return

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
