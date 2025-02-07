from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 8
PLAINTEXT = "Hello World"
KEY = b"poaisfun"
iv = bytes(8)


class DESSettings:
    key: str
    iv: bytes
    mode: int
    block_size: int

    def __init__(self, key: str, iv: bytes, mode: int = DES.MODE_CBC):
        self.key = key
        self.iv = iv
        self.mode = mode
        self.block_size = DES.block_size


des_settings = DESSettings(KEY, iv)


# Encryption
def encrypt_des(settings: DESSettings, plaintext: str) -> bytes:
    des = DES.new(settings.key, settings.mode, settings.iv)
    padded = pad(plaintext.encode(), settings.block_size)
    return des.encrypt(padded)


# Decryption
def decrypt_des(settings: DESSettings, ciphertext: str) -> bytes:
    des = DES.new(settings.key, settings.mode, settings.iv)
    decrypted = des.decrypt(ciphertext)
    return unpad(decrypted, settings.block_size)


def xor(a: int, b: int, c: int):
    return a ^ b ^ c


def oracle(settings: DESSettings, ciphertext: str) -> bool:
    try:
        decrypt_des(settings, ciphertext)
        return True
    except ValueError:
        return False


ciphertext = encrypt_des(des_settings, PLAINTEXT)
print(ciphertext.hex())
plaintext = decrypt_des(des_settings, ciphertext)
print(plaintext.decode())
