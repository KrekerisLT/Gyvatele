# 🐍 Gyvatėlės žaidimas (OOP Coursework)

## 1. Įvadas (Introduction)
**Darbo tikslas:** Sukurti objektiniu programavimu (OOP) pagrįstą taikomąją programą, demonstruojančią pagrindinius programinės įrangos projektavimo principus ir švaraus kodo praktikas[cite: 4, 75].

**Apie programą:** Tai klasikinio „Gyvatėlės“ žaidimo interpretacija, sukurta naudojant Python `turtle` biblioteką[cite: 36]. Žaidimo tikslas – valdyti gyvatėlę, rinkti maistą ir siekti aukščiausio rezultato, nesusiduriant su rėmeliu ar pačia gyvatėle.

**Kaip paleisti programą:**
1. Įsitikinkite, kad turite įdiegtą **Python 3**.
2. Atsisiųskite projekto failus į vieną aplanką.
3. Terminale paleiskite komandą: `python pagrindinis_failas.py` (pakeiskite į savo failo pavadinimą).

**Kaip naudotis programa:**
* Naudokite klavišus **W, A, S, D** gyvatėlės krypčiai keisti.
* Kiekvienas suvalgytas maistas prideda tašką ir pailgina gyvatėlę.
* Žaidimas baigiasi atsitrenkus į sieną arba į savo uodegą.

---

## 2. Analizė (Body/Analysis)

### 4 OOP pyplys (4 OOP Pillars)Programa įgyvendina visus keturis pagrindinius objektinio programavimo principus:

1.  **Abstrakcija (Abstraction):** Naudojama `GameObject` klasė (paveldinti iš `ABC`), kuri apibrėžia bendrą struktūrą ir privalomą `reset_position` metodą visiems žaidimo objektams.
2.  **Paveldėjimas (Inheritance):** Klasės `Food` ir `SnakeSegment` paveldi savybes iš bazinės `GameObject` klasės, taip išvengiant kodo dubliavimo.
3.  **Enkapsuliacija (Encapsulation):** Jautrūs duomenys, tokie kaip gyvatėlės kryptis (`__direction`) ar taškų skaičius (`__score`), yra paslėpti naudojant privačius atributus, pasiekiamus tik per tam skirtus metodus.
4. **Polimorfizmas (Polymorphism):** Metodas `reset_position()` skirtingose klasėse veikia skirtingai: maistas perkeliamas į atsitiktinę vietą, o segmentai – už ekrano ribų.

### Dizaino modelis (Design Pattern)
Projekte pritaikytas **Singleton** (Vieneto) modelis `ScoreManager` klasėje. Tai užtikrina, kad žaidime egzistuotų tik vienas centralizuotas taškų valdymo taškas, atsakingas už rezultatų saugojimą ir failų valdymą.

### Kompozicija ir Agregacija
* **Kompozicija:** `Snake` klasė tiesiogiai valdo `SnakeSegment` objektų sąrašą.
* **Agregacija:** Pagrindinėje `main()` funkcijoje skirtingi objektai (`Snake`, `Food`, `ScoreManager`) sujungiami į bendrą sistemą.

### Darbas su failais (File I/O)
Programa naudoja `highscore.txt` failą duomenų importui ir eksportui:
* **Skaitymas:** Pradedant žaidimą, įkeliamas geriausias rezultatas.
* **Rašymas:** Pasiekus naują rekordą, jis automatiškai įrašomas į failą, užtikrinant duomenų išlikimą.

---

## 3. Rezultatai ir išvados (Results and Summary)

### Rezultatai
* Sukurta veikianti programa, atitinkanti visus funkcinius reikalavimus.
* Įgyvendinta automatinė rekordų sistema su failų saugojimu.
* Kodas parašytas laikantis **PEP8** stiliaus gairių.
* **Iššūkiai:** Didžiausias iššūkis buvo tinkamas gyvatėlės segmentų pozicionavimo algoritmas, užtikrinantis sklandų sekimą paskui galvą.

### Išvados
* [cite_start]Darbas pasiekė užsibrėžtą tikslą – pademonstruoti OOP principų praktinį pritaikymą žaidimų kūrime[cite: 78].
* [cite_start]Sukurta modulinė struktūra leidžia lengvai papildyti žaidimą naujomis funkcijomis[cite: 78].
* [cite_start]**Perspektyvos:** Ateityje būtų galima pridėti sudėtingumo lygius, kliūtis arba spalvų temas[cite: 78].
