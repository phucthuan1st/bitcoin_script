from bitcoinlib.keys import *
from bitcoinlib.wallets import *
#priv_key = 1c0c0e74e9ee4509bbf47a9769d28de853d63659669a147c0fa2ca474c9a06e3
#priv_key2 = c8e929bf5fa8d4d3dcded8a873564081fb019572e7c61df348cdeb57ac5faee0
# Generate a random key
#k = Key()
private_key = '1c0c0e74e9ee4509bbf47a9769d28de853d63659669a147c0fa2ca474c9a06e3'

w1 = wallet_create_or_open('Wallet_test', private_key, network='testnet')

print("--------------------------------------------------------------------")
#w= Wallet('Wallet_test')
w1.utxos_update()
w1.info()
public_key = w1.public_master().wif
print("Private_key", private_key)
print("Public_key", public_key)
print("Address", w1.addresslist()[0])

print("Tao them mot wallet test nua de lam yeu cau 2 giao dich voi nhau")


private_key2 = 'c8e929bf5fa8d4d3dcded8a873564081fb019572e7c61df348cdeb57ac5faee0'

w2 = wallet_create_or_open('Wallet_test_2', private_key2, network='testnet')

print("--------------------------------------------------------------------")
#w= Wallet('Wallet_test')
w2.utxos_update()
w2.info()
public_key2 = w2.public_master().wif
print("Private_key2", private_key2)
print("Public_key2", public_key2)
print("Address2", w2.addresslist()[0]) #n1tSwA7YecwmrJCdTW5TxqS1AAKvhfbPdj
