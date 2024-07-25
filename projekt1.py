"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Macicek

email: jakub.macicek@gnj.cz

discord: kmzm TheKmzm#9073

"""

import time 
TEXTS = ['''
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
garpike and stingray are also present, asdtpfurpgiusd g d d d d d d d '''
]

registr = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
oddelovac = 40 * "-"
prihlasovaci_jmeno = input("Zadejte prihlasovaci jmeno: \n")
heslo = input("Zadejte heslo:\n")
print(oddelovac)

if prihlasovaci_jmeno in registr.keys() and (heslo == registr.get(prihlasovaci_jmeno)):
    print("Welcome to the app,",prihlasovaci_jmeno)
    print("We have 3 texts to be analyzed.")
    print(oddelovac)
    cislo = input("Enter a number btw. 1 and 3 to select: ")
    print(oddelovac)
    if cislo in ("1","2","3"):
        words = TEXTS[int(cislo)-1].split()
        sum = 0 #pocet slov
        titlecase = 0 
        uppercase = 0
        lowercase = 0
        numeric = 0
        sum_num = 0
        lenght = 0
        max_lenght = 0
        for word in words: #pocitani vlastnost
            sum = sum + 1
            if word.isnumeric():
                numeric = numeric + 1
                sum_num = sum_num + int(word)
            if (word.isupper() and word.isalpha()):
                uppercase = uppercase +1
                #print(word)
            if word.islower():
                lowercase = lowercase +1
            if word.istitle():
                titlecase = titlecase +1
            if max_lenght < len(word): #zjisteni max velikosti slova
                max_lenght = len(word)
        
        delky = {}
        for x in range(1, max_lenght + 1): #tvoreni dynamickeho slovniku slovniku
            delky["delka{0}".format(x)] = 0
            
        for word in words: # pricitani do slovniku
            word = word.strip(",.?:!@#$%^&*()_")
            delky["delka{0}".format(len(word))] = delky["delka{0}".format(len(word))] +  1
            lenght = len(word)
        
        print( #vypis hodnot
            "There are",sum, "words in the selected text.\nThere are",
            titlecase, "titlecase words.\nThere are",
            uppercase, "uppercase words.\nThere are",
            lowercase, "lowercase words.\nThere are",
            numeric, "numeric strings.\nThe sum of all the numbers",
            sum_num
            )
        print(oddelovac)
        print(f"{'''LEN|''' : >7}",
              f"{'''OCCURENCES''' : ^15}",
              f'{"|": >10}',
              "NR."
              )
        for x in range(1, max_lenght + 1): #tvorba tabulky
            if delky["delka{0}".format(x)] == 0:
                continue
            print(f'{x : > 5}',
                "|",
                f'{(delky["delka{0}".format(x)]) * "*" : <15}',
                f'{"|": >10}',
                delky["delka{0}".format(x)]
                )
        
    else:
        print("Vybrali jse neplatný vstup, program se ukončí.") #konec
        time.sleep(5)
        exit()
else:
    print("unregistered user, terminating the program..") #šPATNÝ KONEC
    time.sleep(5)
    exit()

print("\nKonec programu.")
input("Pro ukončení zmáčněte klávesu.")