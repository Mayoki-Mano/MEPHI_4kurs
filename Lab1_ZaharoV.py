import matplotlib.pyplot as plt
import pandas as pd
from itertools import combinations
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


def decode(cipher_text, key):
    result = ''
    for i in range(len(cipher_text)):
        result += alphabet[(alphabet.index(cipher_text[i])+key[i%len(key)])%len(alphabet)]
    return result

def plot_histograms(freq_text1, freq_text2, alphabet):
    # Извлекаем значения для каждого текста
    values1 = [freq_text1[char] for char in alphabet]
    values2 = [freq_text2[char] for char in alphabet]

    # Создаем фигуру и оси
    plt.figure(figsize=(10, 5))

    # Ширина столбиков
    width = 0.4

    # Позиции для первого набора данных
    x = range(len(alphabet))

    # Строим гистограммы
    plt.bar(x, values1, width=width, label='Частотные характеристики текста', color='b', align='center')
    plt.bar([p + width for p in x], values2, width=width, label='Частотные характеристики русского языка', color='r',
            align='center')

    # Настройка меток и заголовков
    plt.xlabel('Символы')
    plt.ylabel('Частота')
    plt.title('Сравнение частот символов в двух текстах')
    plt.xticks([p + width / 2 for p in x], alphabet)
    plt.legend()

    # Отображаем гистограмму
    plt.tight_layout()
    plt.show()


def count_char_frequency(text, alphabet):
    # Инициализируем словарь с ключами из алфавита и нулевыми значениями частоты
    frequency = {char: 0 for char in alphabet}

    # Проходим по каждому символу в тексте
    for char in text:
        # Если символ присутствует в алфавите, увеличиваем его частоту
        if char in alphabet:
            frequency[char] += 1

    # Получаем длину текста
    text_length = len(text)

    # Делим частоты на длину текста для получения относительной частоты
    if text_length > 0:  # Проверяем, что длина текста больше 0, чтобы избежать деления на 0
        for char in frequency:
            frequency[char] /= text_length

    return frequency


def find_text_with_best_statistic(text, key_len, alphabet):
    # Создаем пустой массив для хранения результатных строк
    texts = ['' for _ in range(key_len)]
    correlation = 0
    # Итерируем по тексту и добавляем символы в соответствующую строку
    for i, char in enumerate(text):
        texts[i % key_len] += char

    result_text = ''
    multiplier = 1
    for found_text in texts:
        statistic = count_char_frequency(found_text, alphabet)
        values1 = sorted([statistic[char] * multiplier for char in alphabet], reverse=True)
        values2 = sorted([statistic[char] * multiplier for char in alphabet], reverse=True)
        # values1 = [x for x in values1 if x != 0]
        # values2 = [y for y in values2 if y != 0]
        series1 = pd.Series(values1)
        series2 = pd.Series(values2)
        new_correlation = abs(series1.corr(series2))
        # new_correlation = abs(np.corrcoef(values1, values2)[0, 1])
        if correlation <= new_correlation:
            result_text = found_text
            correlation = new_correlation
    return result_text, correlation


def find_key_len(text, max_key_len, alphabet):
    correlation = 0
    key_len = -1
    for i in range(1, max_key_len + 1):
        found_text, new_correlation = find_text_with_best_statistic(text, i, alphabet)
        if correlation <= new_correlation:
            correlation = new_correlation
            key_len = i
        print("Претендент на победу с корреляцией", new_correlation, "и длиной ключа", i)
        plot_histograms(count_char_frequency(found_text, alphabet), frequency_characteristics, alphabet)
    return key_len, correlation
def get_texts_with_same_key(text, key_len):
    texts = {i: "" for i in range(key_len)}
    for i in range(len(text)):
        texts[i%key_len] += text[i]
    return texts

text = (
    "боояпаспюыылтщёытыуфэоьпатршовэеьпкйцёиаэишоыоцёиьаесыфечмхзбтнрычцшовулмьпхфйчъюгьэчаихвщыеычофшкбыятцщгяиагар"
    "лцщпучцпефвяутбщкеюьааяшфипёъфкюобткуйаълтэятыыжююзъуфьиожешттъласбжрфттшьтщууъэуящгуфубюъул")
# max_key_len = 20
# print("Alphabet len", len(alphabet))
# print("Text:\n", text, sep="")
# print("Text length:", len(text))
# key_len,correlation = find_key_len(text, max_key_len, alphabet)
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
sorted_freqs= "оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфёъ"

key_len = 10
print("Key len:", key_len)
key=[]
texts=get_texts_with_same_key(text, key_len)
mean_freq=0
for letter in alphabet:
    mean_freq+=alphabet.index(letter)*frequency_characteristics[letter]
print(mean_freq)
for i in range(key_len):
    mean = 0
    frequency_stat=count_char_frequency(texts[i], alphabet)
    for letter in alphabet:
        mean+=alphabet.index(letter)*frequency_stat[letter]
    key.append(int((mean-mean_freq+len(alphabet)-3)%len(alphabet)))
print(key)

result=decode(text, key)
print(result)
for i in range(len(result)//len(key)):
    for j in range(len(key)):
        print(result[i*len(key)+j],sep='', end='')
    print()
    if i==34:
        break