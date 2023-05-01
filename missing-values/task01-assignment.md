# Task 01: Průměr
1. **Predict:** \
   Bez spuštění! Přečti si kód v souboru `task01.py` a pokus se odhadnout, co dělá. Až budeš mít rozmyšleno, prober to se svou dvojičkou/skupinkou.

2. **Run:** \
   Nyní kód spusťte. Byl váš odhad správný?

3. **Investigate:** \
   Teď si celý kód důkladně projděte a ve dvojici/skupince si řekněte nahlas u každého slova a operátoru, co znamená. Doporučuji začít na řádku 26 (`test_values = ...`), jeho popis by mohl vypadat např. vypadat takto: *`test_values` je název proměnné, `=` zde značí, že chceme do této proměnné uložit nějaký obsah a poté následuje v hranatých závorkách seznam celých čísel, který obsahuje 2 NaN hodnoty z modulu `numpy`.* Když narazíte na námi definovanou funkci, přesuňte se k jejímu kódu stejně, jak by to dělal Python při zpracování skriptu.

4. **Modify:** \
   Vstupní seznam obsahuje pouze celá čísla (`int`), naše funkce ale doplňuje hodnoty s desetinným rozvojem. Uprav kód tak, aby doplňovanou hodnotu zaokrouhlil.
   
5. **Make:** \
   Napiš vlastní funkci `fill_missing_values_with(values, default_value)` na dosazování chybějících hodnot, která nahradí všechny NaN hodnoty ve `values` za `default_value`. Příklady použití:
   ```python
   fill_missing_values_with([30, np.nan, 8], 9) -> [30, 9, 8]
   fill_missing_values_with([np.nan, 3, np.nan, 2], 3) -> [3, 3, 3, 2]
   ```
