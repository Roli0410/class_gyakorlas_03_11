from allat import Allat, Madar, Keteltu, Hullo
from emlos import Emlos, Macska, Kutya



allat1 = Allat("Bodri", "kutya", 5, "kert", "közepes")
allat2 = Allat("Cirmi", "macska", 2, "ház", "közepes")

print(allat1)
print(allat2)

print("\nEMLŐSÖK\n")

emlos1 = Emlos("Morzsi", "kutya", 5, "kert", "barna")
emlos2 = Emlos("Cicó", "macska", 3, "huzz", "cirmos")

print(emlos1)
print(emlos2)


macska1 = Macska("Hubert", 4, "ház", "fehér")
print(macska1)
macska1.dorombol()

kutya1 = Kutya("Cézár", 7, "udvar", "fekete")
print(kutya1)
kutya1.ugat()

print("\nMADARAK\n")

madar1 = Madar("veréb", 1)
print(madar1)
madar1.csiripel()

print("\nKÉTÉLTŰEK\n")

keteltu1 = Keteltu("Johhny", 5)
print(keteltu1)
keteltu1.brekeg()

print("\nHÜLLŐK\n")

hullo1 = Hullo("Larry", 4)
print(hullo1)
hullo1.napozik()


