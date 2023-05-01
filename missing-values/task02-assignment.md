# Task 02: Modus

1. **Predict:** \
   Bez spuštění! Přečti si kód v souboru `task02.py` a pokus se odhadnout, co dělá. Až budeš mít rozmyšleno, prober to se svou dvojičkou/skupinkou.

2. **Run:** \
   Nyní kód spusťte. Byl váš odhad správný?

3. **Investigate:** \
   Opět si celý kód důkladně projděte a tentokrát se zaměřte na odsazení jednotlivých řádků. Řekněte si u každého řádku, v jaké funkci se nachází, jestli je v cyklu, případně za jaké podmínky se vykoná. Zkuste najít řádky (nebo bloky kódu), u kterých bychom mohli odsazení změnit aniž bychom porušili pravidla Pythonu (např. samotný řádek 10 odsadit vlevo nemůžeme, ale blok řádků 10-13 ano) a zamyslete se, jak by se změnilo chování programu.

4. **Modify:** \
   Aktuálně kód v případě, že seznam obsahuje vícero nejčastějších hodnot, vybere tu, která se v seznamu vyskytuje jako první. Uprav kód tak, aby vybrala tu poslední.

5. **Make:** \
   Napiš funkci `fill_columns_nan(df, filling_map)`, která vezme jako parametr DataFrame a slovník, který bude mít jako klíče název sloupců dataframu a jako hodnoty způsob, jak vyplnit v daném sloupci NaN hodnoty. Bude rozpoznávat `"modus"` a `"mean"`, pokud dostane jinou hodnotu, vyplní s ní sloupec pomocí `fill_missing_values_with` z tasku 01. Například po takovémto volání funkce:
   ```python
   fill_columns_nan(data, { "height": "modus", "weight": "mean", "age": 30 })
   ```
   se hodnoty ve sloupci height NaN vyplní pomocí modusu funkce z tohoto tasku, sloupec weight pomocí funkce na průměr z tasku 01 a NaN hodnoty ve sloupci věk se nahradí za hodnotu 30.
