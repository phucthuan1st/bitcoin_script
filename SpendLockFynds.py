import os
from pprint import pprint
from bitcoinlib.wallets import Wallet, BCL_DATABASE_DIR

test_databasefile = os.path.join(BCL_DATABASE_DIR, 'bitcoinlib.test.sqlite')
test_database = 'sqlite:///' + test_databasefile
if os.path.isfile(test_databasefile):
    os.remove(test_databasefile)

print("\n=== Create a wallet and a simple transaction ===")
wlt = Wallet.create('wlttest1', network='bitcoinlib_test', db_uri=test_database)
wlt.get_key()
wlt.utxos_update()  # Create some test UTXOs
wlt.info()
to_key = wlt.get_key()
print("\n- Create transaction (send to own wallet)")
t = wlt.send_to(to_key.address, 2)
t.info()

print("\n- Successfully send, updated wallet info:")
wlt.info()


print("\n Wallet Address")
print(wlt.addresslist())

