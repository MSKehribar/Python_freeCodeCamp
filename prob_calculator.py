
# This project written for determine the approjimate probability of drawing certain balls randomly from a hat.

import random
from copy import deepcopy
import time

class Hat:
    def __init__(self,**kwargs) :
        self.icerik = []
        for i,j in kwargs.items():
            for k in range(j):
                self.icerik.append(i)

    def draw(self, cek_top_say):
        sapka_ic_kopyası = deepcopy(hat.icerik)
        if cek_top_say <= len(sapka_ic_kopyası):
            cekilen_top = []
            for i in range(cek_top_say):
                rasgele_Deger = random.randrange(len(sapka_ic_kopyası))
                cekilen_top.append(sapka_ic_kopyası[rasgele_Deger])
                sapka_ic_kopyası.pop(rasgele_Deger)  
            return cekilen_top
        else:
            return sapka_ic_kopyası



def experiment(hat, beklenen_toplar, cek_top_say, deney_say):

    M = 0
    for i in range(deney_say):
        cekilenler=deepcopy(hat.draw(cek_top_say))
        E = 0
        for i in beklenen_toplar:
            if (cekilenler.count(i)>=beklenen_toplar[i]):
                E = E +1
        if len(beklenen_toplar)==E:
            M = M + 1
            
    return M/deney_say



#Test Part
baslangic_zamani = time.time()

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat,{"red":2,"green":1},5,2000)
print(probability)

print("--- %s saniye ---" % (time.time() - baslangic_zamani)) 