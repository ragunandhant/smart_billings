from cryptography.fernet import Fernet

def create_key():
    
    key = Fernet.generate_key()

    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)
def load_key():
    
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
        return key
def encrpyt_message(s):
    s= s.encode()
    f = Fernet(load_key())
    encrypted = f.encrypt(s)
    return encrypted
def decrypt_message(s):
    f = Fernet(load_key())
    decrypt = f.decrypt(s)
    return decrypt.decode()


