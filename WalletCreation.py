# Importing necessary modules
from bitcoinlib.keys import *
from bitcoinlib.wallets import *

# Function to print the menu for creating Bitcoin addresses
def PrintMenuAddress():
    print("-------Menu-Tao-Dia-Chi-BTC------")
    print("1.Create New Wallet With random private key")
    print("2.Recover a wallet from private key")
    print("3.Test functionality with a predefined private key")
    print("3.Exit program")

# Function to generate a random key and create a wallet
def CreateWalletWithRandomPrivKey():
    k = Key(network='testnet')
    private_key = k.private_hex
    wallet_name = input("Enter wallet name: ")

    w = wallet_create_or_open(wallet_name, private_key, network='testnet')
    print("Infomation of Wallet")
    w.utxos_update()
    w.info()
    
    print("-----Infomation of Private key, Public key, Address------")
    print("Private_key", private_key)
    public_key = w.public_master().wif
    print("Public_key", public_key)
    print("Address", w.addresslist()[0])
    print("-------------Please save above information!--------------")
    
    return w

# Function to create a wallet using user-input private key
def OpenOrCreateWalletWithPrivKey(private_key=None, wallet_name=None):
    if private_key is None:
        private_key = input("Enter your private key: ")

    if wallet_name is None:
        wallet_name = input("Enter your wallet name: ")

    w = wallet_create_or_open(wallet_name, private_key, network='testnet')
    print("Infomation of Wallet")
    w.utxos_update()
    w.info()

    print("-----Infomation of Private key, Public key, Address------")
    print("Private_key", private_key)
    public_key = w.public_master().wif
    print("Public_key", public_key)
    print("Address", w.addresslist()[0])
    print("-------------Please save above information!--------------")
    
    return w

# Function to create a wallet with a predefined private key just for testing
def PredefiendWalletTest():
    # this is a dump private key in BTC testnet
    private_key = '1c0c0e74e9ee4509bbf47a9769d28de853d63659669a147c0fa2ca474c9a06e3'
    w = wallet_create_or_open('Wallet_test', private_key, network='testnet')
    w.utxos_update()
    w.info()
    
    print("-----Infomation of Private key, Public key, Address------")
    print("Private_key", private_key)
    print("Public_key", public_key)
    public_key = w.public_master().wif
    print("Address", w.addresslist()[0])
    
    return w

# Function to handle the creation of Bitcoin addresses based on user input
def WalletCreation():
    PrintMenuAddress()
    x = input("Select your choice: ")
    
    switcher = {
        '1': CreateWalletWithRandomPrivKey,
        '2': OpenOrCreateWalletWithPrivKey,
        '3': PredefiendWalletTest
    }
    
    # Call the function based on user input
    switcher.get(x, lambda: print("Try again!"))()
