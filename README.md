# OOP Coursework: Gyvatėlės žaidimas (Snake Game)

## 1. Įvadas (Introduction)
[cite_start]**Kas yra ši programa?** 
Tai klasikinis „Gyvatėlės“ (Snake) žaidimas, sukurtas naudojant Python kalbą ir `turtle` grafinę biblioteką. Programos tikslas – pritaikyti objektinio programavimo (OOP) principus, dizaino šablonus ir pademonstruoti kodo testavimo bei failų valdymo įgūdžius.

[cite_start]**Kaip paleisti programą?** 
1. Įsitikinkite, kad jūsų kompiuteryje įdiegtas Python 3.
2. Atsisiųskite projekto failus į vieną direktoriją.
3. Terminale arba komandinėje eilutėje atidarykite projekto aplanką.
4. Paleiskite pagrindinį failą: `python main.py`
*(Pastaba: Unit testus galite paleisti su komanda `python -m unittest test_game.py`)*

[cite_start]**Kaip naudotis programa?** 
Žaidimas valdomas klaviatūra:
* **W** - judėti į viršų
* **S** - judėti į apačią
* **A** - judėti į kairę
* **D** - judėti į dešinę
Tikslas – valgyti raudonus maisto blokus, auginti gyvatėlę ir rinkti taškus. Atsitrenkus į sieną arba į savo uodegą, žaidimas atstatomas į pradinę padėtį, o taškai nunulinami, tačiau išsaugomas visų laikų geriausias rezultatas (rekordas).

---

## 2. Analizė (Body/Analysis)
[cite_start]Programa pilnai realizuoja funkcinius reikalavimus, įtraukiant visus keturis OOP pilarus, Singleton dizaino šabloną ir kompoziciją[cite: 76, 77].

### [cite_start]4 OOP pilarai 

**1. Abstrakcija (Abstraction)**
Naudojama abstrakčioji bazinė klasė `GameObject`, apibrėžianti bendrą žaidimo objektų logiką. Klasė turi abstraktų metodą `reset_position()`, kurį privalo įgyvendinti visos iš jos paveldimos klasės.
```python
class GameObject(ABC):
    def __init__(self, shape, color):
        self.obj = turtle.Turtle()
        # ... kiti nustatymai ...

    @abstractmethod
    def reset_position(self):
        """Abstraktus metodas, kurį privalo implementuoti vaikinės klasės."""
        pass
