class Allat:
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_):
        self.nev = nev_
        self.faj = faj_
        self.eletkor = eletkor_
        self.elohely = elohely_
        self.meret = meret_

    def __str__(self):
        return f"{self.nev} {self.faj} {self.eletkor} éves, élőhelye{self.elohely}, mérete {self.meret}"


class Madar(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "madár", eletkor_, "erdő", "kicsi")

    def csiripel(self):
        print(f"{self.nev} éppen csiripel")

class Keteltu(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "keteltu", eletkor_, "tópart", "kicsi")

    def brekeg(self):
        print(f"{self.nev} éppen brekeg")

class Hullo(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "hullo", eletkor_, "szikla", "kicsi")

    def napozik(self):
        print(f"{self.nev} napozik a kövön")

