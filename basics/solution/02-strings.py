# 02 Řetězce
# ------------------------------- TASK 02-01 -----------------------------------
# Napiš program, který načte od uživatele řetězec a nahradí první tři a poslední
# tři znaky za "***"
input_string = input("Write something: ")
new_string = f"***{input_string[3:-3]}***"
print(new_string)

# ------------------------------- TASK 02-02 -----------------------------------
# Napiš funkci mask_card_number, která jako parametr dostane číslo karty
# (jako řetězec), zachová jen první 4 čísla a zbytek nahradí hvězdičkami.
# Mezery mezi čísly skrývat nebude.
def mask_card_number(card_number):
    masked_number = card_number[:4]
    for character in card_number[4:]:
        if character == " ":
            masked_number += " "
        else:
            masked_number += "*"
    return masked_number

print(mask_card_number("1234 5678 9876 5432"))

# ------------------------------- TASK 02-03 -----------------------------------
# Napiš funkci initials, která vezme jako parametr řetězec se jménem a získá z něj
# iniciály. Tuto funkci použij v programu, ve kterém se zeptáš uživatele na jméno
# a vypíšeš mu zpět jeho iniciály.
def initials(name):
    name_initials = ""
    for word in name.split():
        name_initials += word[0]
    return name_initials

my_initials = initials("Adéla Bierská")
print(my_initials)

# ------------------------------- TASK 02-04 -----------------------------------
# Napiš funkci better_capitalize, která vezme jako parametr řetězec a dosadí
# velká písmena na začátek všech slov.
"""
better_capitalize("dnes je krásný den") -> "Dnes Je Krásný Den"
better_capitalize("nemuzunajitnaklavesnicimezeru") -> "Nemuzunajitnaklavesnicimezeru"
"""
def better_capitalize(string):
    capitalized_words = []
    for word in string.split(" "):
        capitalized_words.append(word.capitalize())
    return " ".join(capitalized_words)

print(better_capitalize("dnes je krásný den"))
print(better_capitalize("nemuzunajitnaklavesnicimezeru"))

# ------------------------------- TASK 02-05 -----------------------------------
# Sdružení superhrdinek se rozhodlo založit všem členkám emailové adresy.
# Máš seznam dvojic obsahujících jméno superhrdinky a nakladatelství, ze kterého
# pochází. Emailovou adresu vytvoříš z prvních 6 písmen jména a za zavináč dej
# jméno nakladatelství následnované .com. Aby byly adresy validní, nahraď mezery
# pomlčkami a převeď vše na malá písmena.
# např. Wonder Woman z Marvel Comics bude mít email wonder@marvel-comics.com
superheroines = [
    ("Aurora", "Marvel Comics"),
    ("Poison Ivy", "DC Comics"),
    ("Domino Lady", "Pulps"),
    ("Liz Sherman", "Dark Horse"),
    ("Thor Girl", "Marvel Comics"),
    ("Catwoman", "DC Comics"),
    ("Shadowhawk", "Image Comics"),
    ("Scarlet Witch", "Marvel Comics"),
    ("Batwoman", "DC Comics")
]

emails = []
for superheroine in superheroines:
    email = f"{superheroine[0][:6]}@{superheroine[1]}.com"
    email = email.replace(" ", "-")
    email = email.lower()
    emails.append(email)
