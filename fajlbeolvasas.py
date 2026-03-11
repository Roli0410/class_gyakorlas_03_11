from allat import Allat, Madar, Keteltu, Hullo
from emlos import Emlos, Macska, Kutya

allatok = []
with open('adatok/allatok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
            nev, faj, eletkor, szorzet_szine = sor.strip().split(',')
            
            
            if faj ==  "kutya":
                allatok.append(Kutya(nev, int(eletkor), "udvar", szorzet_szine))
            elif faj == "macska":
                allatok.append(Macska(nev, int(eletkor), "ház", szorzet_szine ))
            elif faj == "madar":
                allatok.append(Madar(nev, int(eletkor)))
            elif faj == "keteltu":
                allatok.append(Keteltu(nev, int(eletkor)))
            elif faj == "hullo":
                allatok.append(Hullo(nev, int(eletkor)))



for allat in allatok:
    print(allat)

for allat in allatok:
    if isinstance(allat, Kutya):
        allat.ugat()
    if isinstance(allat, Macska):
        allat.dorombol()
    if isinstance(allat, Madar):
        allat.csiripel()
    if isinstance(allat, Keteltu):
        allat.brekeg()
    if isinstance(allat, Hullo):
        allat.napozik()


# for allat in allatok:
#     if allat.faj == "kutya":
#         allat.ugat()
#         allat.
#     elif allat.faj == "macska":
#         allat.dorombol
#     elif allat.faj == "madar":
#         allat.csiripel
#     elif allat.faj == "keteltu":
#         allat.brekeg
#     elif allat.faj == "hullo":
#         allat.napozik


