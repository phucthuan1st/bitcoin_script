from bitcoinlib.wallets import *
from bitcoinlib.values import *

def spendLockFunds(wallet: Wallet, amount: float, destination_address: String):
    wallet.info()

    prepared_Tx = wallet.send_to(destination_address, amount, network='testnet', offline=True)
    prepared_Tx.info()
    confirm = input("Do you want to send above transaction? (Y/n): ")
    no = ['no', 'NO', 'No', 'n', 'N']

    if confirm in no:
        return
    
    Tx = wallet.send_to(destination_address, amount, network='testnet', offline=False)
    Tx.info()
    print('Transaction finished! See your wallet status below:')
    wallet.utxos_update()
    wallet.info()