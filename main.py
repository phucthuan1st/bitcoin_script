from WalletCreation import *
from SpendLockFunds import *
import sys

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['help', '--help', None]:
        print("Usage:")
        print("    python main.py wallet")
        print("    python main.py spend --privatekey <privatekey> --amount <amount> --destination <destination> --walletname <walletname>")
        print("    python your_script.py spend -p <privatekey> -a <amount> -d <destination> -n <walletname>")
        return
    
    mode = sys.argv[1]
    print(f'Mode: %s' % mode)

    if mode == 'wallet':
        WalletCreation()
        return
    elif mode == 'spend':
        import argparse
        parser = argparse.ArgumentParser(
            usage="""
                python main.py spend --privatekey <privatekey> --amount <amount>
                                     --destination <destination> --walletname <walletname>
                python your_script.py spend -p <privatekey> -a <amount> -d <destination> -n <walletname>
            """,
            description="Send an amount of tBTC to destination address using your wallet"
        )

        parser.add_argument("-p", "--privatekey", help="Private key", required=True)
        parser.add_argument("-a", "--amount", help="Amount to send", required=True)
        parser.add_argument("-d", "--destination", help="Destination address", required=True)
        parser.add_argument("-n", "--walletname", help="Wallet name", required=True)

        args = parser.parse_args()

        private_key = args.privatekey
        amount = args.amount
        destination_address = args.destination
        wallet_name = args.walletname

        wallet = OpenOrCreateWalletWithPrivKey(private_key=private_key, wallet_name=wallet_name)
        spendLockFunds(wallet=wallet, amount=amount, destination_address=destination_address)
    
if __name__ == "__main__":
    main()
