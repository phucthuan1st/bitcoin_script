from bitcoinlib.transactions import Transaction
from bitcoinlib.wallets import wallet_create_or_open
from bitcoinlib.keys import HDKey

def create_and_send_transaction(key1, key2, amount, network='testnet'):
    k1 = HDKey(key1, network=network)
    k2 = HDKey(key2, network=network)

    w1 = wallet_create_or_open('multisigcosigner1', sigs_required=2, keys=[k1, k2.public_master(multisig=True)], network=network)
    w2 = wallet_create_or_open('multisigcosigner2', sigs_required=2, keys=[k1.public_master(multisig=True), k2], network=network)

    # Create a new transaction
    tx = Transaction()

    # Add the input (the multisig address)
    tx.add_input(w1.get_key().address, amount)

    # Ask the user for the destination address
    destination_address = input("Enter the destination address: ")

    # Add the output (the address to send the bitcoins to)
    tx.add_output(destination_address, amount)

    # Sign the transaction with the necessary keys
    tx.sign([k1, k2])

    # Send the transaction
    tx.send()

key1 = 'tprv8ZgxMBicQKsPd1Q44tfDiZC98iYouKRC2CzjT3HGt1yYw2zuX2awTotzGAZQEAU9bi2M5MCj8iedP9MREPjUgpDEBwBgGi2C8eK5zNYeiX8'
key2 = 'tprv8ZgxMBicQKsPeUbMS6kswJc11zgVEXUnUZuGo3bF6bBrAg1ieFfUdPc9UHqbD5HcXizThrcKike1c4z6xHrz6MWGwy8L6YKVbgJMeQHdWDp'
amount = 10000
create_and_send_transaction(key1, key2, amount)