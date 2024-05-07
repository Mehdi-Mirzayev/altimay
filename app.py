class Kitab:
    def __init__(self, basliq, muellif, nesriyyat, seyfe_sayi):
        self.basliq = basliq
        self.muellif = muellif
        self.nesriyyat = nesriyyat
        self.seyfe_sayi = seyfe_sayi

    def melumatlari_goster(self):
        return f"{self.basliq} - {self.muellif} ({self.nesriyyat}, {self.seyfe_sayi} seyfe)"

    def oxu(self):
        return f"{self.basliq} Kitab oxunur."


kitab1 = Kitab("Suç  ve Ceza", "Fyodor Dostoyevski", "Petersburg Roman Gazetesi", 551)
kitab2 = Kitab("1984", "George Orwell", "Secker & Warburg", 328)


print(kitab1.melumatlari_goster())
print(kitab2.oxu())
