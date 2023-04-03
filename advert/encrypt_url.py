import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

def urlEncryption(url):
    encryption_key = os.getenv('THE_KEY')

    encrypted_url = Fernet(encryption_key).encrypt(url.encode('utf-8'))
    short_encrypted_url = encrypted_url.decode('utf-8')[6:10]

    return short_encrypted_url

def urlEncoding(url):
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    encodedMsg = ''
    
    for letter in url:
        letter_unicode_code = ord(letter)

        letter_unicode_code += 5
        integer_unicode_code = chr(letter_unicode_code)

        encodedMsg += str(integer_unicode_code)


    return encodedMsg

# print(urlEncoding('Before encoding'))
# print(urlEncryption('Before been encrypted blablabla'))
# print(urlEncryption('Before been encrypted'))