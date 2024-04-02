from bitcoinlib.keys import HDKey
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.services.services import Service
import threading
hilos = []
def HacerElRidiculo():
    explorer = Service('bitcoin')
    mnemo = Mnemonic('english')
    while True:
        mnemonic_phrase = mnemo.generate()
        master_key = HDKey.from_passphrase(mnemonic_phrase)
        private_key = master_key.wif()
        public_address = master_key.address()
        if explorer.getbalance(public_address) > 0:
            print("\x1b[1;92mDirección de la billetera:", public_address)
            print("\x1b[1;92mClave privada de la billetera:", private_key)
            print("\x1b[1;92mTiene: " + str(explorer.getbalance(public_address)))
        else:
            print("\x1b[1;31m" + mnemonic_phrase)

for i in range(1,50):
    hilos.append(threading.Thread(target=HacerElRidiculo))

for hilo in hilos:
    hilo.start()
