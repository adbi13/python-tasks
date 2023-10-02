# 03 Funkce
# ------------------------------- TASK 03-01 -----------------------------------
# Vygoogli si funkci randint z modulu random a zjisti, jak funguje. Naimportuj
# si ji a napiš funkci, která se bude hovat jako hrací kostka, tj. bude vracet
# náhodné číslo od 1 do 6.
from random import randint

def kostka():
    return randint(1, 6)

# ------------------------------- TASK 03-02 -----------------------------------
# Napiš funkci map_multiply, která vezme jako parametry seznam čísel a číslo
# a vrátí seznam čísel vynásobený číslem z druhého parametru.
def map_multiply(seznam, cislo):
    novy_seznam = []
    for hodnota in seznam:
        novy_seznam.append(hodnota * cislo)
    return novy_seznam

# ------------------------------- TASK 03-03 -----------------------------------
# Napiš funkci filter_letter, která vezme jako parametry seznam řetězců a písmeno
# a vrátí seznam pouze těch řetězců, které dané písmeno neobsahují.
def filter_letter(seznam, pismeno):
    novy_seznam = []
    for retezec in seznam:
        if pismeno in retezec:
            novy_seznam.append(retezec)
    return novy_seznam

# ------------------------------- TASK 03-04 -----------------------------------
# Napiš funkci powers, která vezme dva číselné parametry. První z nich bude základ
# mocniny a druhé bude značit počet, kolik mocnin daného základu chceme vrátit.
# Mocniny vrátíme jako seznam.
def powers(base, count):
    base_powers = []
    for power in range(count):
        base_powers.append(base ** power)
    return base_powers

# ------------------------------- TASK 03-05 -----------------------------------
# Napiš funkci fibonacci, která vezme jeden číselný parametr a vrátí odpovídající
# počet členů Fibonacciho posloupnosti. Fibonacciho posloupnost začíná čísly 1 a 1
# a každé další číslo získáme tak, že sečteme poslední dvě [1, 1, 2, 3, 5, 8, ...].
def fibonacci(count):
    fibonacci_sequence = [1, 1]
    for last_index in range(1, count - 1):
        next_number = fibonacci_sequence[last_index - 1] + fibonacci_sequence[last_index]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence
