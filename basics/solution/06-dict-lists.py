# 06 Seznamy slovníků
# ------------------------------- TASK 06-01 -----------------------------------
# Mějme menu v nejmenované kavárně uložené jako seznam slovníků:
menu = [
    { "name": "Double Chocolate Brownie", "price": 3.25, "allergens": ["Egg", "Milk", "Soy", "Wheat"], "vegan": False },
    { "name": "Plain Bagel", "price": 1.10, "allergens": ["Wheat"], "vegan": True },
    { "name": "Grilled Cheese", "price": 6.00, "allergens": ["Milk", "Wheat"], "vegan": False },
    { "name": "Orange", "price": 0.50, "allergens": [], "vegan": True },
    { "name": "Cinnamon Bun", "price": 3.20, "allergens": ["Wheat"], "vegan": True },
    { "name": "Churros", "price": 5.00, "allergens": ["Wheat"], "vegan": False },
]

# Kolik zaplatíme, pokud si dáme churros a dva pomeranče?
result = 0
for item in menu:
    if item["name"] == "Churros":
        result += item["price"]
    elif item["name"] == "Orange":
        result += 2 * item["price"]

# Vypiš všechny vegan položky.
for item in menu:
    if item["vegan"]:
        print(item["name"])

# Který alergen je nejvíce zastoupený?
allergen_counts = dict()
for item in menu:
    for allergen in item["allergens"]:
        if allergen not in allergen_counts.keys():
            allergen_counts[allergen] = 1
        else:
            allergen_counts[allergen] += 1

max_count = 0
max_allergen = ""
for allergen, count in allergen_counts.items():
    if count > max_count:
        max_count = count
        max_allergen = allergen

print(max_allergen)

# ------------------------------- TASK 06-02 -----------------------------------
# Mějme piva na skladu nejmenované pivotéky uložené jako seznam slovníků:
beers = [
    { "name": "Brněnská 11", "brewery": "Parní pivovar Hauskrecht", "type": "Pale Lager", "IBU": 38, "ABV": 4.5, "count": 25 },
    { "name": "Šlágr", "brewery": "Falkon", "type": "Pale Lager", "IBU": 35, "ABV": 4.0, "count": 13 },
    { "name": "Hofburg", "brewery": "Topolský pivovar", "type": "Dark Lager", "IBU": 30, "ABV": 4.9, "count": 0 },
    { "name": "Drakobití", "brewery": "Mazák", "type": "APA", "IBU": None, "ABV": None, "count": 8 },
    { "name": "Single Hop Ale Eclipse", "brewery": "MadCat", "type": "APA", "IBU": None, "ABV": 5.0, "count": 0 },
    { "name": "West Is The Best", "brewery": "MadCat", "type": "IPA", "IBU": None, "ABV": 6.3, "count": 17 },
    { "name": "Philadelphia Sour Višeň", "brewery": "Obora", "type": "Sour Ale", "IBU": 15, "ABV": 4.7, "count": 19 },
    { "name": "Franklin", "brewery": "Ládví Cobolis", "type": "NEIPA", "IBU": None, "ABV": 6.0, "count": 2 },
]

# Které pivo má nejvíc alkoholu (tj. má nejvyšší ABV)?
max_abv = 0
max_beer = ""
for beer in beers:
    if beer["ABV"] != None and beer["ABV"] > max_abv:
        max_abv = beer["ABV"]
        max_beer = beer["name"]
print(f"Nejvíc alkoholu má {max_beer}.")

# Která piva jsou vyprodaná (tj. count se rovná nule)?
sold_out_beers = []
for beer in beers:
    if beer["count"] == 0:
        sold_out_beers.append(beer["name"])

print(f"Vyprodána jsou: {sold_out_beers}")

# Zákazník si koupil 2x West Is The Best, zaznamenej tuto informaci do tabulky.
for beer in beers:
    if beer["name"] == "West Is The Best":
        beer["count"] -= 2

# Některým pivům chybí některé hodnoty (tj. rovnají se None). Vytvoř nový seznam,
# který bude obsahovat jen piva, které mají všechny hodnoty vyplněny.
non_none_beers = []
for beer in beers:
    if None not in beer.values():
        non_none_beers.append(beer)

# Vytvoř slovník, který bude mít jako klíče typy piv obsažené ve vstupním seznamu
# a jako hodnoty seznamy názvů piv, které jsou na skladu.
beers_by_type = dict()
for beer in beers:
    if beer["type"] not in beers_by_type.keys():
        beers_by_type[beer["type"]] = [ beer["name"] ]
    else:
        beers_by_type[beer["type"]].append(beer["name"])
print(beers_by_type)

# ------------------------------- TASK 06-03 -----------------------------------
# Mějme lidi, co byli vybráni jako Person of the Year podle Times, uložené jako seznam slovníků:
person_of_the_year = [
    { "year": 2000, "name": "George W. Bush", "country": "United States", "title": "President of the United States", "category": "Politics", "context": "Presidential Election" },
    { "year": 2001, "name": "Rudy Giuliani", "country": "United States", "title": "Mayor of New York City", "category": "War", "context": "9/11 Terrorist Attacks" },
    { "year": 2002, "name": "The Whistleblowers (Coleen Rowley)", "country": "United States", "title": "FBI Special Agent", "category": "Politics", "context": "9/11 Terrorist Attacks" },
    { "year": 2002, "name": "The Whistleblowers (Sherron Watkins)", "country": "United States", "title": "Vice President of Corporate Development at Enron", "category": "Economics", "context": "Corporate Fraud" },
    { "year": 2002, "name": "The Whistleblowers (Cynthia Cooper)", "country": "United States", "title": "Vice President of Internal Audit at WorldCom", "category": "Economics", "context": "Corporate Fraud" },
    { "year": 2003, "name": "The American Soldier", "country": "United States", "title": None, "category": "War", "context": "Iraq War" },
    { "year": 2004, "name": "George W. Bush", "country": "United States", "title": "President of the United States", "category": "Politics", "context": "Presidential Election" },
    { "year": 2005, "name": "The Good Samaritans (Bill Gates)", "country": "United States", "title": "Founder of Bill & Melinda Gates Foundation", "category": "Philanthropy", "context": None },
    { "year": 2005, "name": "The Good Samaritans (Melinda Gates)", "country": "United States", "title": "Founder of Bill & Melinda Gates Foundation", "category": "Philanthropy", "context": None },
    { "year": 2005, "name": "The Good Samaritans (Bono)", "country": "Ireland", "title": "Lead Singer of U2", "category": "Philanthropy", "context": "Charity Concerts" },
    { "year": 2006, "name": "You", "country": None, "title": None, "category": "Technology", "context": "World Wide Web" },
    { "year": 2007, "name": "Vladimir Putin", "country": "Russia", "title": "President of the Russian Federation", "category": "Politics", "context": None },
    { "year": 2008, "name": "Barack Obama", "country": "United States", "title": "President of the United States", "category": "Politics", "context": "Presidential Election" },
    { "year": 2009, "name": "Ben Bernanke", "country": "United States", "title": "Chairman of the Federal Reserve", "category": "Economics", "context": "Financial Crisis" },
    { "year": 2010, "name": "Mark Zuckerberg", "country": "United States", "title": "Founder and CEO of Facebook", "category": "Technology", "context": None },
    { "year": 2011, "name": "The Protester", "country": None, "title": None, "category": "Revolution", "context": "Arab Spring" },
    { "year": 2012, "name": "Barack Obama", "country": "United States", "title": "President of the United States", "category": "Politics", "context": "Presidential Election" },
    { "year": 2013, "name": "Pope Francis", "country": "Vatican City", "title": "Pope of the Roman Catholic Church", "category": "Religion", "context": "Papal Conclave" },
    { "year": 2014, "name": "The Ebola Fighters", "country": None, "title": None, "category": "Science", "context": "Ebola Epidemic" },
    { "year": 2015, "name": "Angela Merkel", "country": "Germany", "title": "Chancellor of Germany", "category": "Politics", "context": "Debt Crisis, Refugee Crisis, Paris Terrorist Attacks" },
    { "year": 2016, "name": "Donald Trump", "country": "United States", "title": "President of the United States", "category": "Politics", "context": "Presidential Election" },
    { "year": 2017, "name": "The Silence Breakers", "country": None, "title": None, "category": "Society", "context": "MeToo movement" },
    { "year": 2018, "name": "The Guardians and the War on Truth", "country": None, "title": None, "category": "Society", "context": "Fake news" },
    { "year": 2019, "name": "Greta Thunberg", "country": "Sweden", "title": None, "category": "Society", "context": "Climate change, ecology, environmental movements" },
    { "year": 2020, "name": "Joe Biden", "country": "United States", "title": "President of the United States", "category": "Politics", "context": "Presidential Election" },
    { "year": 2020, "name": "Kamala Harris", "country": "United States", "title": "Vice President of the United States", "category": "Politics", "context": "First woman, first African American, and first Asian American vice president" },
    { "year": 2021, "name": "Elon Musk", "country": "United States", "title": "CEO of Tesla & SpaceX", "category": "Technology", "context": "Richest person in the world in 2021" },
    { "year": 2022, "name": "Volodymyr Zelensky", "country": "Ukraine", "title": "President of Ukraine", "category": "War", "context": "Supreme commander-in-chief during the 2022 Russian invasion of Ukraine" },
    { "year": 2022, "name": "The Spirit of Ukraine", "country": "Ukraine", "title": None, "category": "War", "context": "'The Spirit of Ukraine' represents the 'resilience of the Ukrainian people and the Ukrainian resistance, as well as foreign aid to Ukraine'" },
]
# Které státy mají jen jednoho zástupce?
country_counts = dict()
for person in person_of_the_year:
    if person["country"] not in country_counts.keys():
        country_counts[person["country"]] = 1
    else:
        country_counts[person["country"]] += 1

for country, count in country_counts.items():
    if count == 1:
        print(country)

# Která kategorie má nejvíc zástupců?
category_counts = dict()
for person in person_of_the_year:
    if person["category"] not in category_counts.keys():
        category_counts[person["category"]] = 1
    else:
        category_counts[person["category"]] += 1

max_count = 0
max_category = ""
for category, count in category_counts.items():
    if count > max_count:
        max_count = count
        max_category = category
print(f"Nejvíc je zastoupena kategorie {max_category}")

# Ve kterých letech bylo vybráno více osob?
year_counts = dict()
for person in person_of_the_year:
    if person["year"] not in year_counts.keys():
        year_counts[person["year"]] = 1
    else:
        year_counts[person["year"]] += 1

for year, count in year_counts.items():
    if count > 1:
        print(year)

# Nahraď všechny hodnoty None za prázdný řetězec (tj. "").
for person in person_of_the_year:
    for key, value in person.items():
        if value == None:
            person[key] = ""

# Kolik je v seznamu prezidentů? Pozor, nachází se cem i vice presidents, ty nepočítej.
president_count = 0
for person in person_of_the_year:
    if "President" in person["title"] and "Vice President" not in person["title"]:
        president_count += 1
print(f"V seznamu se nachází {president_count} prezidentů.")
