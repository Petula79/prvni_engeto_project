USER = ["bob", "ann", "mike", "liz"]
PASSWORD = ["123", "pass123", "password123", "pass123"]
oddelovac = ("=" * 55)
oddelovac_1 = ("-" * 55)
oddelovac_3 = ("_._" * 9)

uzivatele = dict(zip(USER, PASSWORD))

username = input("Enter your username: ")
password = input("Enter your password: ")

if uzivatele.get(username) == password:
    print(oddelovac, "Welcome to the APP!".center(len(oddelovac)), oddelovac, sep="\n")
    print(f"{username.title()} we have 3 texts to be analyzed.".center(len(oddelovac)), oddelovac_1, sep="\n")
else:
    print(oddelovac_1, "INCORRECT USERNAME OR PASSWORD!".center(len(oddelovac)), oddelovac_1, sep="\n")
    quit()

TEXTS = {
    "1": '''
    Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet 
    above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, 
    which traverse the valley. ''',
    "2": '''
    At the base of Fossil Butte are the bright 
    red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending 
    to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.''',
    "3": '''
    The monument contains 8198 acres and protects 
    a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits 
    are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils 
    represent several varieties of perch, as well as 
    other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present.'''
}

choice = input("Enter a number btw. 1 and 3 to select: ")

zadani = {"slova": 0, "cislo": 0, "Titul": 0, "mala": 0, "velka": 0, "pocet": 0}
zadani_2 = {"slova_2": 0, "cislo_2": 0, "Titul_2": 0, "mala_2": 0, "velka_2": 0, "pocet_2": 0}
zadani_3 = {"slova_3": 0, "cislo_3": 0, "Titul_3": 0, "mala_3": 0, "velka_3": 0, "pocet_3": 0}

text_1 = TEXTS["1"]
text_2 = TEXTS["2"]
text_3 = TEXTS["3"]

vycistena_slova_1 = []
vycistena_slova_2 = []
vycistena_slova_3 = []

for slovo in text_1.split():
    bez = slovo.strip(",.:;_-")
    vycistena_slova_1.append(bez)

for slovo in text_2.split():
    bez = slovo.strip(",.:;-_'")
    vycistena_slova_2.append(bez)

for slovo in text_3.split():
    bez = slovo.strip(",.:;- ")
    vycistena_slova_3.append(bez)

soucet_cisel_1 = int(vycistena_slova_1[2]) + int(vycistena_slova_1[19]) + int(vycistena_slova_1[31])
soucet_cisel_2 = int(vycistena_slova_2[-3])
soucet_cisel_3 = int(vycistena_slova_3[3]) + int(vycistena_slova_3[34])


for slovo in vycistena_slova_1:
    if not slovo.isspace():
        zadani["slova"] += 1

for titul in vycistena_slova_1:
    if titul.istitle():
        zadani["Titul"] += 1

for velke in vycistena_slova_1:
    if velke.isupper() and velke.isalpha():
        zadani["velka"] += 1

for male in vycistena_slova_1:
    if not male.istitle():
        if male.islower():
            zadani["mala"] += 1

for Cisla in vycistena_slova_1:
    if Cisla.isnumeric():
        zadani["cislo"] += 1


for slovo in vycistena_slova_2:
    if not slovo.isspace():
        zadani_2["slova_2"] += 1

for titul in vycistena_slova_2:
    if titul.istitle():
        zadani_2["Titul_2"] += 1

for velke in vycistena_slova_2:
    if velke.isupper() and velke.isalpha():
        zadani_2["velka_2"] += 1

for male in vycistena_slova_2:
    if not male.istitle():
        if male.islower():
            zadani_2["mala_2"] += 1

for Cisla in vycistena_slova_2:
    if Cisla.isnumeric():
        zadani_2["cislo_2"] += 1


for slovo in vycistena_slova_3:
    if not slovo.isspace():
        zadani_3["slova_3"] += 1

for titul in vycistena_slova_3:
    if titul.istitle():
        zadani_3["Titul_3"] += 1

for velke in vycistena_slova_3:
    if velke.isupper() and velke.isalpha():
        zadani_3["velka_3"] += 1

for male in vycistena_slova_3:
    if not male.istitle():
        if male.islower():
            zadani_3["mala_3"] += 1

for Cisla in vycistena_slova_3:
    if Cisla.isnumeric():
        zadani_3["cislo_3"] += 1


if choice == "1":
    print(oddelovac_1, f"Your choice is number: {choice}.", oddelovac_1, sep="\n")
    print("There are", str(zadani["slova"]), "words in the selected text.")
    print("There are", str(zadani["Titul"]), "titlecase words.")
    print("There are", str(zadani["velka"]), "uppercase words.")
    print("There are", str(zadani["mala"]), "lowercase words.")
    print("There are", str(zadani["cislo"]), "numeric strings.")
    print(f"The sum of all the numbers: {soucet_cisel_1}")
    print(oddelovac_1, oddelovac_3, sep="\n")
    print(f"|LEN|    OCCURENCES      NR|")
    print(oddelovac_3)
    for index, tabulka in enumerate(vycistena_slova_1,1):
        print(f"|{index: ^2}.| {'#' * len(tabulka): <18} {len(tabulka): >2}|")
        print(oddelovac_3)
elif choice == "2":
    print(oddelovac_1, f"Your choice is number: {choice}.", oddelovac_1, sep="\n")
    print("There are", str(zadani_2["slova_2"]), "words in the selected text.")
    print("There are", str(zadani_2["Titul_2"]), "titlecase words.")
    print("There are", str(zadani_2["velka_2"]), "uppercase words.")
    print("There are", str(zadani_2["mala_2"]), "lowercase words.")
    print("There are", str(zadani_2["cislo_2"]), "numeric strings.")
    print(f"The sum of all the numbers: {soucet_cisel_2}")
    print(oddelovac_1, oddelovac_3, sep="\n")
    print(f"|LEN|    OCCURENCES      NR|")
    print(oddelovac_3)
    for index, tabulka in enumerate(vycistena_slova_2, 1):
        print(f"|{index: ^2}.| {'#' * len(tabulka): <18} {len(tabulka): >2}|")
        print(oddelovac_3)
elif choice == "3":
    print(oddelovac_1, f"Your choice is number: {choice}.", oddelovac_1, sep="\n")
    print("There are", str(zadani_3["slova_3"]), "words in the selected text.")
    print("There are", str(zadani_3["Titul_3"]), "titlecase words.")
    print("There are", str(zadani_3["velka_3"]), "uppercase words.")
    print("There are", str(zadani_3["mala_3"]), "lowercase words.")
    print("There are", str(zadani_3["cislo_3"]), "numeric strings.")
    print(f"The sum of all the numbers: {soucet_cisel_3}")
    print(oddelovac_1, oddelovac_3, sep="\n")
    print(f"|LEN|    OCCURENCES      NR|")
    print(oddelovac_3)
    for index, tabulka in enumerate(vycistena_slova_3, 1):
        print(f"|{index: ^2}.| {'#' * len(tabulka): <18} {len(tabulka): >2}|")
        print(oddelovac_3)
else:
    print(oddelovac_1, "INCORRECT CHOICE!".center(len(oddelovac)), oddelovac_1, sep="\n")
    quit()
