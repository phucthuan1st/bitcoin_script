from bitcoinlib.wallets import  wallet_create_or_open
from bitcoinlib.keys import HDKey

def create_multisig_wallets(key1, key2, network='testnet'):
    k1 = HDKey(key1, network=network)
    k2 = HDKey(key2, network=network)

    w1 = wallet_create_or_open('multisig_cosigner1', sigs_required=2, keys=[k1, k2.public_master(multisig=True)], network=network)
    w2 = wallet_create_or_open('multisig_cosigner2', sigs_required=2, keys=[k1.public_master(multisig=True), k2], network=network)

    print("Public Key 1:", k1.public_master(multisig=True))
    print("Public Key 2:", k2.public_master(multisig=True))
    print("Deposit testnet bitcoin to this address to create transaction: ", w1.get_key().address)
    print("Deposit testnet bitcoin to this address to create transaction: ", w2.get_key().address)
    print("\n--------------------------------------------------------------------")
    print("Wallet 1")
    w1.utxos_update()
    w1.info()

    print("\n--------------------------------------------------------------------")
    print("Wallet 2")
    w2.utxos_update()
    w2.info()

    return w1, w2

key1 = 'tprv8ZgxMBicQKsPd1Q44tfDiZC98iYouKRC2CzjT3HGt1yYw2zuX2awTotzGAZQEAU9bi2M5MCj8iedP9MREPjUgpDEBwBgGi2C8eK5zNYeiX8'
key2 = 'tprv8ZgxMBicQKsPeUbMS6kswJc11zgVEXUnUZuGo3bF6bBrAg1ieFfUdPc9UHqbD5HcXizThrcKike1c4z6xHrz6MWGwy8L6YKVbgJMeQHdWDp'
w1, w2 = create_multisig_wallets(key1, key2)