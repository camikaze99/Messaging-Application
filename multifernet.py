# sudo apt-get install build-essential libssl-dev libffi-dev python-dev
# sudo apt install python3-pip
# If necessary, give permission to make changes in /usr/lib/python3/dist-packages
# sudo chmod 777 dist-packages
# pip3 install cryptography

from cryptography.fernet import Fernet
from cryptography.fernet import MultiFernet

def encrypt(message):
    key1 = Fernet.generate_key()
    key2 = Fernet.generate_key()
    k1 = Fernet(key1)
    k2 = Fernet(key2)
    cryptoKey = MultiFernet([k1, k2])
    encryptedMessage = cryptoKey.encrypt(message.encode('ascii'))
    return [key1, key2, encryptedMessage]

def decrypt(key1, key2, encryptedMessage):
    k1 = Fernet(key1)
    k2 = Fernet(key2)
    decryptoKey = MultiFernet([k1, k2])
    message = decryptoKey.decrypt(encryptedMessage)
    return message

cryptoKey = encrypt("This is supposed to be a secret")
#print(cryptoKey[0])
#print(cryptoKey[1])
#print(cryptoKey[2])
print(decrypt(cryptoKey[0], cryptoKey[1], cryptoKey[2]))
