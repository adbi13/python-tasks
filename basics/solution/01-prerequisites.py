# 01 Prerekvizity
# ------------------------------- TASK 01-01 -----------------------------------
# Vytvoř proměnnou a ulož do ní celé číslo. Pomocí vhodné funkce jej převeď
# na desetinné číslo a to ulož od další proměnné.
cele_cislo = 19
desetinne_cislo = float(cele_cislo)

# ------------------------------- TASK 01-02 -----------------------------------
# Načti od uživatele celé číslo, zjisti, zda je dělitelné 8 a informuj
# o tom uživatele.
number = int(input("Zadej cislo: "))
if number % 8 == 0:
    print("Cislo je delitelne osmi")

# ------------------------------- TASK 01-03 -----------------------------------
# Načti od uživatele matematický operátor a 2 čísla a vypiš výsledek výpočtu.
# Program bude podporovat operátory +, -, / a *.
''' # Tři uvozovky jsou jiný způsob psaní komentářů v Pythonu, tady je budeme
    # Používat na ukázky očekávaného chování zadaného programu/funkce.
Zadej operátor: +
Zadej první číslo: 3
Zadej druhé číslo: 9
Výsledek příkladu 3 + 9 je 12.
'''

operator = input("Zadej operátor: ")
prvni_cislo = int(input("Zadej první číslo: "))
druhe_cislo = int(input("Zadej druhe číslo: "))

if operator == "+":
    result = prvni_cislo + druhe_cislo
elif operator == "-":
    result = prvni_cislo - druhe_cislo
elif operator == "/":
    result = prvni_cislo / druhe_cislo
elif operator == "*":
    result = prvni_cislo * druhe_cislo

print(f"Výsledek příkladu {prvni_cislo} {operator} {druhe_cislo} je {result}.")

# ------------------------------- TASK 01-04 -----------------------------------
# Vytvoř dvě proměnné, které budou reprezentovat informaci o tom, zda zrovna
# stojíme venku na ulici a zda venku pršelo. Napiš program, který nám řekne,
# jestli máme zrovna mokré boty – ty máme mokré jen v případě, že jsme venku
# a je po dešti.
jsem_venku = False # Založíme si dvě proměnné, se kterými pak budeme pracovat.
prselo = True # Jejich iniciální hodnoty vyberte náhodně a pak je měňte při testování.

## První varianta se zanořeným ifem:
# if jsem_venku:
#     if prselo:
#         print("Mam mokre boty!")
#     else:
#         print("Nemam mokre boty.")
# else:
#     print("Nemam mokre boty.")

# Druhá varianta s použitím logických spojek:
if jsem_venku and prselo:
    print("Mam mokre boty!")
else:
    print("Nemam mokre boty.")

# ------------------------------- TASK 01-05 -----------------------------------
# Napiš program, který od uživatele načte číslo a vypíše jeho ciferný součet.
number = input("Milý uživateli, prosím, zadej nějaké číslo: ")
# "678" ~ ["6", "7", "8"] # Zde se nám bude hodit pracovat s řetězcem jako seznamem znaků
digit_sum = 0
for digit in number:
    digit_sum += int(digit) # Nesmíme zapomenout převést znak na číslo.


# ------------------------------- TASK 01-06 -----------------------------------
# V seznamu people máme seznam lidí s jejich daty narození. Vypište jména lidí,
# kteří se narodili v sudý rok.
people = [
    ["Jeong-Hui Mun", "09/12/1984"],
    ["Cezário Torres", "31/08/1993"],
    ["Josefina Löwe", "03/11/1982"],
    ["Gavrilo Milojević", "28/03/2002"],
    ["Liidia Tamm", "10/07/1963"],
    ["Matxin Zubizarreta", "19/02/1956"],
    ["Mykhail Klymenko", "01/10/1988"],
    ["Bibek Joshi", "05/03/2007"],
    ["Jan Vlk", "26/09/1995"],
    ["Xuân Hoàng", "29/08/1974"]
]

for person in people:
    if int(person[1][-1]) % 2 == 0: # Pro ověření, zda je číslo sudé, stačí ověřit, zda je sudá jeho poslední číslice.
        print(person[0])
