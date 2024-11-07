import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

frequency_characteristics = {
    "а": 0.0801,
    "б": 0.0159,
    "в": 0.0454,
    "г": 0.017,
    "д": 0.0298,
    "е": 0.0845,
    "ё": 0.0004,
    "ж": 0.0094,
    "з": 0.0165,
    "и": 0.0735,
    "й": 0.0121,
    "к": 0.0349,
    "л": 0.044,
    "м": 0.0321,
    "н": 0.067,
    "о": 0.1097,
    "п": 0.0281,
    "р": 0.0473,
    "с": 0.0547,
    "т": 0.0626,
    "у": 0.0262,
    "ф": 0.0026,
    "х": 0.0097,
    "ц": 0.0048,
    "ч": 0.0144,
    "ш": 0.0073,
    "щ": 0.0046,
    "ъ": 0.0004,
    "ы": 0.0190,
    "ь": 0.0174,
    "э": 0.0032,
    "ю": 0.0064,
    "я": 0.0201
}
alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def indices_to_text(indices,alphabet=alphabet_ru):
    text = ''.join(alphabet[i] for i in indices if 0 <= i < len(alphabet))
    return text

def get_letter_index(letter,alphabet=alphabet_ru):
    return alphabet.find(letter)

def decode(cipher_text, key,alphabet=alphabet_ru):
    result = ''
    key_indices= []
    cipher_indices = []
    for letter in key:
        key_indices.append(get_letter_index(letter,alphabet))
    for letter in cipher_text:
        cipher_indices.append(get_letter_index(letter,alphabet))
    for i in range(len(cipher_indices)):
        if key_indices[i%len(key_indices)]==0:
            result += alphabet[(cipher_indices[i] - key_indices[i % len(key_indices)]) % len(alphabet)]
        else:
           result += alphabet[(cipher_indices[i]-key_indices[i%len(key_indices)])%len(alphabet)].upper()
    return result

def get_key(cipher_word,word,alphabet=alphabet_ru):
    key=[]
    cipher_indices =[]
    word_indices=[]
    for letter in cipher_word:
        cipher_indices.append(get_letter_index(letter, alphabet))
    for letter in word:
        word_indices.append(get_letter_index(letter, alphabet))
    for i in range(len(cipher_indices)):
        key += alphabet[(cipher_indices[i] - word_indices[i]) % len(alphabet)]
    return key


text = (
    "боояпаспюыылтщёытыуфэоьпатршовэеьпкйцёиаэишоыоцёиьаесыфечмхзбтнрычцшовулмьпхфйчъюгьэчаихвщыеычофшкбыятцщгяиагар"
    "лцщпучцпефвяутбщкеюьааяшфипёъфкюобткуйаълтэятыыжююзъуфьиожешттъласбжрфттшьтщууъэуящгуфубюъул")

key_len = 5
print("Key len:", key_len)
word = 'сто'
key=[]

prohibited_bigrams={'ЁЁ','ЩЩ','ЧЁ','ЭЫС','ТЪЖ','ХНЮ','АЗЙ','АЗЙ','АЗЙ','АЗЙ','АЗЙ','АЗЙ','НЙР'}
def check_prohibited_bigrams(text):
    upper_text = ''.join([char for char in text if char.isupper()])
    substrings = [upper_text[i:i + 3] for i in range(0, len(upper_text), 3)]
    for substring in substrings:
        # Проверяем на наличие невозможных биграмм
        for i in range(len(substring) - 1):
            for prohibited in prohibited_bigrams:
                if prohibited in substring:
                    return True
    return False


for i in range(len(text)//5-1):
    key+=alphabet_ru[0]*2
    key+=get_key(cipher_word=text[i*5+2:(i+1)*5],word=word,alphabet=alphabet_ru)
    if not check_prohibited_bigrams(decode(text, key, alphabet=alphabet_ru)):
        print(i, text[i*5+2:(i+1)*5],key)
        print(decode(text,key,alphabet=alphabet_ru))
    key=[]
for i in range(len(text)//5-1):
    key+=alphabet_ru[0]
    key+=get_key(cipher_word=text[i*5+1:i*5+4],word=word,alphabet=alphabet_ru)
    key += alphabet_ru[0]
    if not check_prohibited_bigrams(decode(text,key,alphabet=alphabet_ru)):
        print(i, text[i*5+1:i*5+4],key)
        print(decode(text,key,alphabet=alphabet_ru))
    key=[]
for i in range(len(text)//5-1):
    key+=get_key(cipher_word=text[i*5:i*5+3],word=word,alphabet=alphabet_ru)
    key += alphabet_ru[0]*2
    if not check_prohibited_bigrams(decode(text, key, alphabet=alphabet_ru)):
        print(i, text[i*5:i*5+3],key)
        print(decode(text,key,alphabet=alphabet_ru))
    key=[]
# print("Correlation:", correlation)
