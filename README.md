#  Gyvatėlės žaidimas (OOP Coursework 2026)

## 1. Įvadas (Introduction)

**Darbo tikslas:**  
Sukurti objektiniu programavimu (OOP) pagrįstą taikomąją programą, demonstruojančią pagrindinius programinės įrangos projektavimo principus ir švaraus kodo praktikas.

**Apie programą:**  
Tai klasikinio „Gyvatėlės“ žaidimo interpretacija, sukurta naudojant Python `turtle` biblioteką. Žaidimo tikslas – valdyti gyvatėlę, rinkti maistą ir siekti aukščiausio rezultato, nesusiduriant su rėmeliu ar pačia gyvatėle.

**Kaip paleisti programą:**  
1. Įsitikinkite, kad turite įdiegtą **Python 3**.  
2. Atsisiųskite projekto failus į vieną aplanką.  
3. Terminale paleiskite komandą nurodant failo aplanko vieta:
   ```bash
   cd kelias/iki/jūsų/aplanko
   ```
   ```bash
   py main.py
   ```
**Arba** 
1. Atsiusti projekto failus į vieną aplanką.
2. Per VisualStudio atidaryti ``main.py``
3. Paleisti koda per VisualStudio

**Kaip naudotis programa:**  
- Naudokite klavišus **W, A, S, D** gyvatėlės krypčiai keisti.  
- Kiekvienas suvalgytas maistas prideda tašką ir pailgina gyvatėlę.  
- Žaidimas baigiasi atsitrenkus į sieną arba į savo uodegą.

---

## 2. Analizė (Body / Analysis)

Šioje dalyje detaliai aprašoma, kaip programa įgyvendina funkcinius reikalavimus, naudojant objektinio programavimo principus.

### 2.1. 4 OOP principai (4 OOP Pillars)

Programa sėkmingai integruoja visus keturis pagrindinius OOP principus:

#### 1. Abstrakcija (Abstraction)
Naudojama `GameObject` klasė (paveldinti iš `ABC`), kuri apibrėžia bendrą struktūrą ir privalomą metodą vaikinėms klasėms.

```python
from abc import ABC, abstractmethod

class GameObject(ABC):
    @abstractmethod
    def reset_position(self):
        """Abstraktus metodas, kurį privalo implementuoti vaikinės klasės."""
        pass
```

#### 2. Paveldėjimas (Inheritance)
Klasės `Food` ir `SnakeSegment` paveldi savybes iš bazinės `GameObject` klasės, taip išvengiant kodo dubliavimo.

```python
class Food(GameObject):
    def __init__(self):
        super().__init__("circle", "#E74C3C")
```

#### 3. Enkapsuliacija (Encapsulation)
Jautrūs duomenys, pvz., gyvatėlės kryptis ar taškai, yra apsaugoti naudojant privačius atributus.

```python
self.__score = 0
self.__direction = "stop"
```

#### 4. Polimorfizmas (Polymorphism)
Metodas `reset_position()` realizuotas skirtingai `Food` ir `SnakeSegment` klasėse.

---

### 2.2. Dizaino modelis (Design Pattern)

Projekte pritaikytas **Singleton** modelis `ScoreManager` klasėje.

**Kodėl pasirinkta:**  
Tai užtikrina, kad visoje programoje egzistuotų tik vienas taškų valdytojas.

```python
def __new__(cls):
    if cls._instance is None:
        cls._instance = super(ScoreManager, cls).__new__(cls)
    return cls._instance
```

---

### 2.3. Kompozicija

- **Kompozicija:** `Snake` klasė valdo `SnakeSegment` objektų sąrašą.  

---

### 2.4. Darbas su failais (File I/O)

Programa naudoja `.txt` failą:

- **Skaitymas:** nuskaitomas geriausias rezultatas (`__load_high_score`)  
- **Rašymas:** naujas rekordas įrašomas (`__save_high_score`)

---

### 2.5. Testavimas

Pagrindinės funkcijos tikrinamos naudojant `unittest` karkasą, užtikrinant stabilumą.

---

## 3. Rezultatai ir išvados (Results and Summary)

### Rezultatai
- Sukurta veikianti programa, atitinkanti funkcinius reikalavimus  
- Įgyvendinta rekordų sistema su failų saugojimu  
- Kodas atitinka **PEP8** standartus  

### Iššūkiai
Didžiausias iššūkis buvo užtikrinti sklandų gyvatėlės segmentų judėjimą.

### Išvados
- Darbas pasiekė tikslą – pademonstruoti OOP principus praktikoje  
- Modulinė struktūra leidžia lengvai plėsti projektą  

### Ateities perspektyvos
- Sudėtingumo lygiai  
- Kliūtys žemėlapyje  
- Daugiau unit testų  
