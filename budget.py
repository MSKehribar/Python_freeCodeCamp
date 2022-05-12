class Category:
    def __init__(self, tanim):
        self.tanim = tanim
        self.defter = []
        self.__durum = 0.0

    def __repr__(self):
        baslik = self.tanim.center(30, "*") + "\n"
        defter = ""
        for i in self.defter:
            # format tanim and miktar
            line_tanim = "{:<23}".format(i["tanim"])
            line_miktar = "{:>7.2f}".format(i["miktar"])
            # Truncate defter tanim and miktar to 23 and 7 characters respectively
            defter += "{}{}\n".format(line_tanim[:23], line_miktar[:7])
        toplam = "Total: {:.2f}".format(self.__durum)
        return baslik + defter + toplam

    def deposit(self, miktar, tanim=""):        #yatırılan para
        self.defter.append({"miktar": miktar, "tanim": tanim})
        self.__durum += miktar

    def withdraw(self, miktar, tanim=""):       #cekilen para
        if self.__durum - miktar >= 0:
            self.defter.append({"miktar": -1 * miktar, "tanim": tanim})
            self.__durum -= miktar
            return True
        else:
            return False

    def get_durum(self):
        return self.__durum

    def transfer(self, miktar, ornek_kategori):
        if self.withdraw(miktar, "Transfer to {}".format(ornek_kategori.tanim)):
            ornek_kategori.deposit(miktar, "Transfer from {}".format(self.tanim))
            return True
        else:
            return False

    def check_funds(self, miktar):
        if self.__durum >= miktar:
            return True
        else:
            return False

def create_spend_chart(kategoriler):
    harcama_miktari = []
    # Get toplam harcama in each kategori
    for kategori in kategoriler:
        harcama = 0
        for i in kategori.defter:
            if i["miktar"] < 0:
                harcama += abs(i["miktar"])
        harcama_miktari.append(round(harcama, 2))

    # Calculate percentage rounded down to the nearest 10
    toplam = round(sum(harcama_miktari), 2)
    harcama_yuzdesi = list(map(lambda miktar: int((((miktar / toplam) * 10) // 1) * 10), harcama_miktari))

    # Create the bar cizelge substrings
    baslik = "Percentage harcama by kategori\n"

    cizelge = ""
    for value in reversed(range(0, 101, 10)):
        cizelge += str(value).rjust(3) + '|'
        for yuzde in harcama_yuzdesi:
            if yuzde >= value:
                cizelge += " o "
            else:
                cizelge += "   "
        cizelge += " \n"

    altbilgi = "    " + "-" * ((3 * len(kategoriler)) + 1) + "\n"
    tanimlar = list(map(lambda kategori: kategori.tanim, kategoriler))
    max_uzunluk = max(map(lambda tanim: len(tanim), tanimlar))
    tanimlar = list(map(lambda tanim: tanim.ljust(max_uzunluk), tanimlar))
    for x in zip(*tanimlar):
        altbilgi += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (baslik + cizelge + altbilgi).rstrip("\n")




cuzdan_Y=Category("Yemek")
cuzdan_A=Category("Arac")
cuzdan_Y.deposit(1000,"yatirim")
cuzdan_Y.deposit(1200,"yatirim")
cuzdan_Y.deposit(3200,"yatirim")
cuzdan_Y.withdraw(15,"yemek")
cuzdan_Y.withdraw(25,"giysi")
cuzdan_Y.transfer(99,cuzdan_A)
cuzdan_Y.check_funds(250)

print(cuzdan_Y)
print(cuzdan_Y.get_durum())
print(create_spend_chart([cuzdan_Y,cuzdan_A]))