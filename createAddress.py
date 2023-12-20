from bitcoinlib.keys import *
from bitcoinlib.wallets import *
import os


def PrintMenuAddress():
    print("-------Menu-Tao-Dia-Chi-BTC------")
    print("1.Random Key")
    print("2.Input Key")
    print("3.Wallet - Test")
    print("3.Exit")


def randomKeyToAdd():
    k = Key()
    private_key = k.private_hex
    w = wallet_create_or_open('My_Wallet_random_key', private_key,network='testnet')
    print("Infomation of Wallet")
    w.utxos_update()
    w.info()
    public_key = w.public_master().wif
    print("-----Infomation of Private key, Public key, Address------")
    print("Private_key", private_key)
    print("Public_key", public_key)
    print("Address", w.addresslist()[0])
    return w


def InputKeyToAdd():
    print("Enter your pivate key: ")
    private_key = input()
    w = wallet_create_or_open('My_Wallet_Input_key', private_key,network='testnet')
    print("Infomation of Wallet")
    w.utxos_update()
    w.info()
    public_key = w.public_master().wif
    print("-----Infomation of Private key, Public key, Address------")
    print("Private_key", private_key)
    print("Public_key", public_key)
    print("Address", w.addresslist()[0])
    return w

def WalletTest():
    private_key = '1c0c0e74e9ee4509bbf47a9769d28de853d63659669a147c0fa2ca474c9a06e3'
    w = wallet_create_or_open('Wallet_test', private_key, network='testnet')
    w.utxos_update()
    w.info()
    public_key = w.public_master().wif
    print("-----Infomation of Private key, Public key, Address------")
    print("Private_key", private_key)
    print("Public_key", public_key)
    print("Address", w.addresslist()[0])
    return w

def CreateAddress():
    PrintMenuAddress()
    print("Select your choice: ")
    x = input()
    switcher ={
        1: randomKeyToAdd() ,
        2: InputKeyToAdd() ,
        3: WalletTest()
    }
    return switcher.get(x,"Nothing")

CreateAddress()