from bitcoinlib.keys import *
from bitcoinlib.wallets import *
#priv_key = 1c0c0e74e9ee4509bbf47a9769d28de853d63659669a147c0fa2ca474c9a06e3
# Generate a random key
#k = Key()
private_key = '1c0c0e74e9ee4509bbf47a9769d28de853d63659669a147c0fa2ca474c9a06e3'

w = wallet_create_or_open('Wallet_test', private_key, network='testnet', encoding=base58encode)

print("--------------------------------------------------------------------")
#w= Wallet('Wallet_test')
w.utxos_update()
w.info()
public_key = w.public_master().wif
print("Private_key", private_key)
print("Public_key", public_key)
print("Address", w.addresslist())

