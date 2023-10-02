# 04 Slovníky
# ------------------------------- TASK 04-01 -----------------------------------
# Do proměnné animal ulož slovník, který bude reprezentovat zvíře s alespoň 5
# nějakými jeho vlastnostmi. Pokus se, aby alespoň jedna z hodnot byla seznam.
# Pokud tě nic nenapadá, mrkni na svoje oblíbené zvíře na Wikipedii.
animal = {
    "nazev": "lenochod",
    "barva srsti": "hneda",
    "vyska": 1.20,
    "potrava": ["ovoce", "listi", "kvety", "vyhonky"]
}

# ------------------------------- TASK 04-02 -----------------------------------
# Napiš funkci in_in, která vezme jako parametr slovník a řetětec a zjistí, zda
# se daný řetězec nachází v klíčích nebo hodnotách ve slovníku.
def in_in(slovnik, retezec):
    je_v_klicich = retezec in slovnik.keys()
    je_v_hodnotach = retezec in slovnik.values()
    return je_v_klicich or je_v_hodnotach

if in_in(animal, "lenochod"):
    print("V animal najdes lenochoda")

# ------------------------------- TASK 04-03 -----------------------------------
# Proměnná medal_table obsahuje zisky medailí států na olympiádě 2020. Vypiš
# název státu, který získal nejvíc medailí.

medal_table = {
    "Kenya": 10,
    "Australia": 46,
    "Iran": 7,
    "Ecuador": 3,
    "Portugal": 4,
    "Kazakhstan": 8,
}

top_stat = ""
top_medaile = 0

for stat, medaile in medal_table.items():
    if medaile > top_medaile:
        top_medaile = medaile
        top_stat = stat

print(f"Nejvic medaili ziskali sportovci z {top_stat}")

# ------------------------------- TASK 04-04 -----------------------------------
# Proměnná medal_table tentokrát obsahuje zisky jednotlivých druhů medailí států
# na olympiádě 2020.
medal_table = {
    "Cuba": { "gold": 7, "silver": 3, "bronze": 5 },
    "Spain": { "gold": 3, "silver": 8, "bronze": 6 },
    "Uganda": { "gold": 2, "silver": 1, "bronze": 1 },
    "Bahamas": { "gold": 2, "silver": 0, "bronze": 0 },
    "Ukraine": { "gold": 1, "silver": 6, "bronze": 12 },
    "San Marino": { "gold": 0, "silver": 1, "bronze": 2 },
}

# Vypiš název státu, který získal nejvíc bronzových medailí.
top_stat = ""
top_bronzove_medaile = 0

for stat, medaile in medal_table.items():
    if medaile["bronze"] > top_bronzove_medaile:
        top_bronzove_medaile = medaile["bronze"]
        top_stat = stat

print(f"Nejvíc bronzových medailí získali sportovci z {top_stat}")

# Vypiš název státu, který získal nejvíc medailí celkově.
top_stat = ""
top_medaile = 0

for stat, medaile in medal_table.items():
    soucet_medaili = sum(medaile.values())
    if soucet_medaili > top_medaile:
        top_medaile = soucet_medaili
        top_stat = stat

print(f"Nejvíc medailí získali sportovci z {top_stat}")

# ------------------------------- TASK 04-05 -----------------------------------
# Proměnná medal_table tentokrát obsahuje zisky jednotlivých druhů medailí států
# na posledních 3 letních olympiádách.
medal_table = {
    2012: {
        "Brazil": { "gold": 3, "silver": 5, "bronze": 9 },
        "Norway": { "gold": 2, "silver": 1, "bronze": 1 },
        "Czech Republic": { "gold": 4, "silver": 4, "bronze": 3 },
        "New Zealand": { "gold": 6, "silver": 2, "bronze": 5 },
        "South Korea": { "gold": 13, "silver": 9, "bronze": 8 },
    },
    2016: {
        "Brazil": { "gold": 7, "silver": 6, "bronze": 6 },
        "Norway": { "gold": 0, "silver": 0, "bronze": 4 },
        "Czech Republic": { "gold": 1, "silver": 2, "bronze": 7 },
        "New Zealand": { "gold": 4, "silver": 9, "bronze": 5 },
        "South Korea": { "gold": 9, "silver": 3, "bronze": 9 },
    },
    2020: {
        "Brazil": { "gold": 7, "silver": 6, "bronze": 8 },
        "Norway": { "gold": 4, "silver": 2, "bronze": 2 },
        "Czech Republic": { "gold": 4, "silver": 4, "bronze": 4 },
        "New Zealand": { "gold": 7, "silver": 6, "bronze": 7 },
        "South Korea": { "gold": 6, "silver": 4, "bronze": 10 },
    },
}

# Pro každý rok vypiš stát s nejvíce medailemi.
for year, table in medal_table.items():
    top_stat = ""
    top_medaile = 0

    for stat, medaile in table.items():
        soucet_medaili = sum(medaile.values())
        if soucet_medaili > top_medaile:
            top_medaile = soucet_medaili
            top_stat = stat
    
    print(f"V roce {year} nejvíc medailí získali sportovci z {top_stat}.")

# Pro každý stát vypiš rok s nejmíň medailemi.
import math # modul math se nám bude hodit pro získání nekonečna jako iniciální hodnotu minima

countries = medal_table[2012].keys()
for country in countries:
    medal_minimum = math.inf # Chceme mít jistotu, že se v tabulce bude vyskytovat nižší hodnota, proto nekonečno
    minimum_year = 0
    for year, table in medal_table.items():
        medal_count = sum(table[country].values())
        if medal_count < medal_minimum:
            medal_minimum = medal_count
            minimum_year = year
    print(f"Pro {country} byl nejslabší rok {minimum_year}.")

# Kolik zlatých medailí získal Nový Zéland za všechny 3 roky?
count = 0
for year, table in medal_table.items():
    count += table["New Zealand"]["gold"]

print(f"Nový Zéland získal dohromady {count} zlatých medailí.")
