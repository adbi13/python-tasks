# 05 Funkce se slovníky
# ------------------------------- TASK 05-01 -----------------------------------
# Napiš funkci pretty_print, která vezme jako parametr slovník a vypíše jej hezky
# naformátovaný. Např. tak, že každá dvojice klíč:hodnota bude na samostatném řádku.
def pretty_print(dictionary):
    print("{")
    for key, value in dictionary.items():
        print(f"{key}: {value}")
    print("}")

# ------------------------------- TASK 05-02 -----------------------------------
# Napiš funkci items_to_dict, která vezme jako parametr seznam dvojic (tuples)
# (klíč, hodnota) a vytvoří z nich slovník.
def items_to_dict(dvojice):
    novy_slovnik = dict() # Lze použít i {}
    for klic, hodnota in dvojice:
        novy_slovnik[klic] = hodnota
    return novy_slovnik


# ------------------------------- TASK 05-03 -----------------------------------
# Napiš funkci upper_dict, která vezme jako parametr slovník a vytvoří z něj nový
# slovník, který bude mít všechny klíče převedené na velká písmena.
def upper_dict(dictionary):
    new_dict = dict()
    for key, value in dictionary.items():
        upper_key = key.upper()
        new_dict[upper_key] = value
    return new_dict

# ------------------------------- TASK 05-04 -----------------------------------
# Napiš funkci concat_dicts, která vezme jako parametr seznam slovníků a spojí
# je do jednoho.
def concat_dicts(dict_list):
    new_dict = dict()
    for dictionary in dict_list:
        for key, value in dictionary.items():
            new_dict[key] = value
    return new_dict

# ------------------------------- TASK 05-05 -----------------------------------
# Napiš funkci translator, která vezme jako parametry slovník a seznam slov a
# nahradí slova v seznamu dle slovníku (klíč vyskytující se v seznamu nahradí
# za jemu příslušnou hodnotu ze slovníku).
def translator(dictionary, strings):
    translated_strings = []
    for string in strings:
        if string in dictionary.keys():
            translated_strings.append(dictionary[string])
        else:
            translated_strings.append(string)
    return translated_strings
