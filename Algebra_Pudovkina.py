import re
import pickle
with open("russian.utf-8", encoding="utf-8") as f:
    word_list = [line.strip() for line in f if line.strip()]


# Создаем список слов нужной длины
word_length = 4
filtered_word_list4 = [word for word in word_list if len(word) == word_length]
filtered_word_list5 = [word for word in word_list if len(word) == 5]
filtered_word_list2 = [word for word in word_list if len(word) == 2]

def find_words(word_length, letter_positions,word_list):
    # Генерируем маску для слова и компилируем паттерн один раз
    mask = ['_'] * word_length
    for position, letter in letter_positions.items():
        mask[position] = letter
    pattern = re.compile(''.join(mask).replace('_', '[а-яёА-ЯЁ]'))

    # Ищем слова, соответствующие маске
    return [word for word in word_list if pattern.fullmatch(word)]


# letters_to_try = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфё'
letters_to_try = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфё'
matches = []
matches1 = []
# Проход по комбинациям букв
for nul in letters_to_try:
    for four in letters_to_try:
        for one in letters_to_try:
            if nul == four or nul == one or one == four:
                continue

            # Первый поиск
            letter_positions1 = {0: nul, 3: four, 1: one}
            matching_words1 = find_words(word_length, letter_positions1, filtered_word_list4)

            # Второй поиск
            letter_positions2 = {1: nul, 3: four, 0: one}
            matching_words2 = find_words(word_length, letter_positions2, filtered_word_list4)

            for matching_word_one in matching_words1:
                for matching_word_two in matching_words2:
                    if matching_word_one[0]== matching_word_two[1] and matching_word_one[1] == matching_word_two[0] and matching_word_one[3] == matching_word_two[3]:
                        matches1.append([matching_word_one, matching_word_two])
for three in letters_to_try:
    for five in letters_to_try:
        if three == five:
            continue
        # Первый поиск
        letter_positions1 = {3: three, 1: five}
        matching_words1 = find_words(word_length, letter_positions1, filtered_word_list4)

        # Второй поиск
        letter_positions2 = {2: three, 4: five}
        matching_words2 = find_words(5, letter_positions2, filtered_word_list5)
        for matching_word_one in matching_words1:
            for matching_word_two in matching_words2:
                if matching_word_one[3]== matching_word_two[2] and matching_word_one[1] == matching_word_two[4]:
                    matches.append([matching_word_one, matching_word_two])
result=[]
for matching_word_one, matching_word_two in matches:
    for matc in matches1:
        if matching_word_one == matc[1]:
            word_two = matching_word_two[0]+matching_word_two[1]
            if matc[0][2] in matching_word_two or matc[0][2] in matc[1]:
                continue
            if matc[1][2] in matching_word_two or matching_word_two[0]==matching_word_two[1]:
                continue
            if matching_word_two[0] ==  matching_word_two[2] or matching_word_two[0] == matching_word_two[4] or matching_word_two[0] == matching_word_two[3]:
                continue
            if matching_word_two[1] ==  matching_word_two[2] or matching_word_two[1] == matching_word_two[4] or matching_word_two[1] == matching_word_two[3]:
                continue
            if matching_word_two[3] ==  matching_word_two[0] or matching_word_two[3] == matching_word_two[1] or matching_word_two[3] == matching_word_two[2]\
                    or matching_word_two[3] == matching_word_two[4] or matching_word_two[3] in matc[1] or matching_word_two[3] in matc[0]:
                continue
            if matching_word_two[0] in matc[1] or matching_word_two[1] in matc[1]:
                continue
            if word_two in filtered_word_list2:
                result += [[f"{matc[0]} {matching_word_two[0]}{matching_word_two[1]} {matching_word_two} {matc[1]}"]]
unique_matches = []
for match in result:
    if match not in unique_matches:
        unique_matches.append(match)

for match in unique_matches:
    print(match)
print("Уникальные совпадения:", len(unique_matches))

# Сохранение массива в файл
with open("unique_matches.pkl", "wb") as f:
    pickle.dump(unique_matches, f)

