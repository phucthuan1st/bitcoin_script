from bitcoinlib.wallets import *
from bitcoinlib.values import *
#coinomi address mzUX8X5uV1gft7NGbLAacBR2GYALKsovp9
def transactionBtc():
    print(print("\n=== Create a wallet and a simple transaction ==="))
    ## Cho nay a thuan goi ham ho em voi e bi qua
    ## a goi sao gan wlt = creteAddress no tra ve chung
    ## kieu du lieu la duoc
    ## em test cung nhu trong de cho khoe
    wlt = wallet_create_or_open('Wallet_test')
    wlt2 = wallet_create_or_open('Wallet_test_2')
    wlt.info()
    wlt2_key = wlt2.get_key()
    destination_address = wlt2_key.address
    #Create a transaction.
    print("\n - Create Transaction")
    ## offline = True la no chua chuyen that bo ra la di that
    ## anh xem code r noi lai em nhe
    t = wlt.send_to(destination_address,10, offline= True)
    t.info()
    print("\n- Successfully send, updated wallet info:")
    wlt.utxos_update()
    wlt.info()

    print("\n -Infomation of Wallet recv")
    wlt2.utxos_update()
    wlt2.info()
   

transactionBtc()