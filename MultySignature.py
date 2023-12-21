from bitcoinlib.wallets import Wallet, wallet_create_or_open
from bitcoinlib.keys import HDKey

NETWORK = 'testnet'
# khóa riêng tư mở rộng (Extended Private Key) theo chuẩn BIP32
# Khóa riêng tư mở rộng này bắt đầu bằng "tprv", điều này cho thấy nó được sử dụng cho mạng thử nghiệm (Testnet) của Bitcoin.
k1 = HDKey('tprv8ZgxMBicQKsPd1Q44tfDiZC98iYouKRC2CzjT3HGt1yYw2zuX2awTotzGAZQEAU9bi2M5MCj8iedP9MREPjUgpDEBwBgGi2C8eK5zNYeiX8', network=NETWORK)
k2 = HDKey('tprv8ZgxMBicQKsPeUbMS6kswJc11zgVEXUnUZuGo3bF6bBrAg1ieFfUdPc9UHqbD5HcXizThrcKike1c4z6xHrz6MWGwy8L6YKVbgJMeQHdWDp', network=NETWORK)

w1 = wallet_create_or_open('multisig_cosigner1', sigs_required=2, keys=[k1, k2.public_master(multisig=True)], network=NETWORK)
w2 = wallet_create_or_open('multisig_cosigner2', sigs_required=2, keys=[k1.public_master(multisig=True), k2], network=NETWORK)


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


# Deposit testnet bitcoin to this address to create transaction:  2NBrLTapyFqU4Wo29xG4QeEt8kn38KVWRRr
# Public Key 1: 03fba20a7ec73d77a75ff16c3d234dc46d3a33aee91ac67a8c9e73a99723c6d826
# Public Key 2: 02ec69bf1b0003775fbc384a23648cca2dba2fef5fc88b707bce2ac58e278cbef5