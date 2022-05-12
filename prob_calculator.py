import random
from copy import deepcopy


class Hat:
    def __init__(self,**kwargs) :
        self.icerik = []
        for i,j in kwargs.items():
            for k in range(j):
                self.icerik.append(i)

    def draw(self, cekilen_top_say):
        if cekilen_top_say <= len(self.icerik):
            cekilen_top = []
            for i in range(cekilen_top_say):
                rasgele_Deger = random.randrange(len(self.icerik))
                cekilen_top.append(self.icerik[rasgele_Deger])
                self.icerik.pop(rasgele_Deger)  
            return cekilen_top
        else:
            return self.icerik



def experiment(hat, beklenen_toplar, cekilen_top_say, deney_say):
    beklenen = []
    for i, j in beklenen_toplar.items():
        for k in range(j):
            beklenen.append(i)
    M = 0
    content_copy = deepcopy(hat.icerik)
    for i in range(deney_say):
        if all(item in hat.draw(cekilen_top_say) for item in beklenen):
            M = M + 1
        hat.icerik = deepcopy(content_copy)
    return M/deney_say


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat,{"red":2,"green":1},5,5000)
print(probability)
