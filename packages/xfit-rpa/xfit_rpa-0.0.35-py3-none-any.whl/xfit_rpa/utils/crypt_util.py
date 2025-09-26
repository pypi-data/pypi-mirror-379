import base64
import binascii
import os
import random
import string
from typing import Union

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def base64_encode(data) -> str:
    return base64.b64encode(data).decode('utf-8')


def base64_decode(data) -> bytes:
    return base64.b64decode(data)


def base64_key(length=32) -> str:
    key = os.urandom(length)  # AES-256密钥
    # os.environ['AES_GCM_KEY'] =
    return base64_encode(key)


def encrypt_gcm(key: str, plaintext: str) -> str:
    cipher = AES.new(base64.b64decode(key), AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    ciphertext = cipher.nonce + tag + ciphertext
    return base64_encode(ciphertext)


def decrypt_gcm(key: str, ciphertext: Union[str, bytes]) -> str:
    if isinstance(ciphertext, str):
        ciphertext = base64_decode(ciphertext)
    nonce = ciphertext[:16]
    tag = ciphertext[16:32]
    actual_ciphertext = ciphertext[32:]
    cipher = AES.new(base64.b64decode(key), AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(actual_ciphertext, tag).decode('utf-8')


def encrypt_aes(key: Union[str, bytes], plaintext: str, iv: Union[str, bytes] = None) -> str:
    """
     AES加密函数（支持可选IV）

    :param key: 16/24/32字节的二进制密钥
    :param plaintext: 要加密的文本
    :param iv: None-随机生成, b''-使用ECB模式, 或16字节IV
    :return: base64编码的密文(IV已包含在结果中，ECB模式除外)
    """
    if isinstance(key, str):
        # key = key.encode('utf-8')
        key = base64.b64decode(key)
    # 处理IV为空字符串的情况
    if iv is not None and len(iv) == 0:
        # ECB模式不需要IV
        cipher = AES.new(key, AES.MODE_ECB)
        padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
        ciphertext = cipher.encrypt(padded_data)

    else:
        # 处理None或有效IV的情况
        if iv is None:
            iv = get_random_bytes(16)
        elif len(iv) != 16:
            raise ValueError("IV必须是16字节长度或空(使用ECB模式)")

        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
        ciphertext = iv + cipher.encrypt(padded_data)
    return base64_encode(ciphertext)


def decrypt_aes(key: Union[str, bytes], ciphertext: str, iv=None) -> str:
    if isinstance(key, str):
        # key = key.encode('utf-8')
        key = base64.b64decode(key)
    # Base64解码
    try:
        ciphertext = base64.b64decode(ciphertext)
    except Exception as e:
        raise ValueError("无效的Base64编码数据") from e
    # 处理不同IV情况
    if iv is None:
        # 从密文头部提取IV(CBC模式)
        if len(ciphertext) < 16:
            raise ValueError("密文太短，无法提取IV")
        iv = ciphertext[:16]
        actual_ciphertext = ciphertext[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif len(iv) == 0:
        # ECB模式
        actual_ciphertext = ciphertext
        cipher = AES.new(key, AES.MODE_ECB)
    elif len(iv) == 16:
        # 使用提供的IV(CBC模式)
        actual_ciphertext = ciphertext
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        raise ValueError("IV必须是16字节长度或空字节串(ECB模式)")

    # 解密并去除填充
    try:
        decrypted = cipher.decrypt(actual_ciphertext)
        unpadded = unpad(decrypted, AES.block_size)
        return unpadded.decode('utf-8')
    except ValueError as e:
        raise ValueError("解密失败: 可能是无效的密钥、IV或填充") from e
    except UnicodeDecodeError:
        raise ValueError("解密结果不是有效的UTF-8文本")


def encrypt(key: str, plaintext: str, mode: str = 'gcm') -> str:
    if mode == 'gcm':
        return encrypt_gcm(key, plaintext)
    elif mode == 'ecb':
        return encrypt_aes(key, plaintext, '')
    elif mode == 'cbc':
        return encrypt_aes(key, plaintext, None)
    else:
        raise ValueError("无效的加密模式")


def decrypt(key: str, ciphertext: str, mode: str = 'gcm') -> str:
    if mode == 'gcm' or mode is None:
        return decrypt_gcm(key, ciphertext)
    elif mode == 'ecb':
        return decrypt_aes(key, ciphertext, '')
    elif mode == 'cbc':
        return decrypt_aes(key, ciphertext, None)
    else:
        raise ValueError("无效的解密模式")


class CryptUtil:
    _random_str_idx = 8
    _random_str_len = 8

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def encrypt(self, data: str):
        data = self._random_str() + data
        if isinstance(data, str):
            data = data.encode('ascii')
        return base64.b64encode(binascii.hexlify(data)).decode('ascii')

    def decrypt(self, data: str):
        if isinstance(data, str):
            data = data.encode('ascii')
        return binascii.unhexlify(base64.b64decode(data)).decode('ascii')[self._random_str_len:]

    @classmethod
    def _random_str(cls, length=_random_str_len):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


if __name__ == '__main__':
    key = base64_key()
    print(key)
    encrypted = encrypt_aes(key, 'hello world')
    decrypted = decrypt_aes(key, encrypted)
    print(encrypted, decrypted)