"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Dominik Hvězda
email: domik.hvezduj@gmail.com
discord: domino#0624
"""
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
line = 40 * "-"

username = input("username: ")
password = input("password: ")
print(line)

# kontrola zda je uzivatel registrovany
if username in registered_users and registered_users[username] == password:
    print("Welcome to the app", username)
    print("We have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    quit()
print(line)

# nechat uzivatele vybrat mezi 3 texty
txt_choice = input("Enter a number btw. 1 and 3 to select: ")
if txt_choice.isdigit() and 1 <= int(txt_choice) <= 3:
    print(line)
else:
    print("Wrong input!")
    exit()

# preindexovat text
index_text = texts[int(txt_choice) - 1]

cleaned_words = list()
individual_words = index_text.split()

# ocisteni slov
for word in individual_words:
    cleaned_words.append(word.strip(",.:;?!"))

# spocitani slov
num_words = len(cleaned_words)

# spocitani slov zacinajici velkymi pismeny
title_words = 0
for title in individual_words:
    if title.istitle():
        title_words = title_words + 1

# spocitani slov psanych velkymi pismeny
upper_words = 0
for upper in individual_words:
    if upper.isupper():
        upper_words = upper_words + 1

# spocitani slov s malymi pismeny
lower_words = 0
for lower in individual_words:
    if lower.islower():
        lower_words = lower_words + 1

# pocet cisel (ne cifer)
numbers = 0
for number in individual_words:
    if number.isdigit():
        numbers = numbers + 1

# suma všech cisel
total = 0
for sum_up in individual_words:
    if sum_up.isnumeric():
        total += int(sum_up)

# vypsani hodnot
bar_chart = "LEN|  OCCURENCES  |NR."

print("There are", num_words, "words in the selected text.")
print("There are", title_words, "titlecase words.")
print("There are", upper_words, "uppercase words.")
print("There are", lower_words, "lowercase words.")
print("There are", numbers, "numeric strings.")
print("The sum off all the numbers", total)
print(
    line,
    bar_chart,
    line,
    sep="\n"
    )

# spocitani delky ruznych slov
word_len = dict()
for word in individual_words:
    if word not in word_len:
        word_len[word] = len(word)

lenght = sorted(list(word_len.values()))
len_number = dict()
for amount in set(lenght):
    len_number[amount] = lenght.count(amount)

# sloupcový graf
for word_len, pocetslov in len_number.items():
    graf = pocetslov * "*"
    print(f"{word_len:<3}|{graf:<14}|{pocetslov:>2}")