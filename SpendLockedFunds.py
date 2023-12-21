from bitcoinlib.transactions import Transaction
from bitcoinlib.wallets import Wallet
from bitcoinlib.keys import HDKey
# Define the amount of satoshis to send
amount = 10000
NETWORK = 'testnet'
k1 = HDKey('tprv8ZgxMBicQKsPd1Q44tfDiZC98iYouKRC2CzjT3HGt1yYw2zuX2awTotzGAZQEAU9bi2M5MCj8iedP9MREPjUgpDEBwBgGi2C8eK5zNYeiX8', network=NETWORK)
k2 = HDKey('tprv8ZgxMBicQKsPeUbMS6kswJc11zgVEXUnUZuGo3bF6bBrAg1ieFfUdPc9UHqbD5HcXizThrcKike1c4z6xHrz6MWGwy8L6YKVbgJMeQHdWDp', network=NETWORK)

w1 = Wallet.create('multisigcosigner1', sigs_required=2, keys=[k1, k2.public_master(multisig=True)], network=NETWORK)
w2 = Wallet.create('multisigcosigner2', sigs_required=2, keys=[k1.public_master(multisig=True), k2], network=NETWORK)

# Create a new transaction
tx = Transaction()

# Add the input (the multisig address)
tx.add_input(w1.get_key().address, amount)

# Add the output (the address to send the bitcoins to)
tx.add_output('destination_address', amount)

# Sign the transaction with the necessary keys
tx.sign([k1, k2])

# Send the transaction
tx.send()