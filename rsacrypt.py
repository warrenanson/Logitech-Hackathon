import rsa
from binascii import b2a_hex, a2b_hex

class rsacrypt():

    pubkey, prikey = rsa.newkeys(256)

    def __init__(self):
        pass

    def encrypt(self, text):
        self.ciphertext = rsa.encrypt(text.encode(), self.pubkey)
        # 因為rsa加密時候得到的字串不一定是ascii字符集的，輸出到終端或者儲存時候可能存在問題
        # 所以這裡統一把加密後的字串轉化為16進位制字串
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        decrypt_text = rsa.decrypt(a2b_hex(text), self.prikey)
        return decrypt_text
