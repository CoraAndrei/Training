import random

from Modul4.Exeample2.carte import Carte


class Pachet:
    carti = []

    def __init__(self):
        culori = ["rosu", "negru", "romb", "trefla"]
        valori = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.carti = [Carte(val, cul) for val in valori for cul in culori]
        # for cul in culori:
        #     for val in valori:
        #         carti_fianl = Carte(val, cul)
        #         self.carti.apend(carti_fianl)
        # self.carti = carti

    def deal(self):
        # carte[0] = carte[1]
        # pop la carti
        print(self.carti[0] == self.carti[1])
        return self.carti.pop()

    def shuffle(self):
        random.shuffle(self.carti)

    def __eq__(self, other):
        return len(self.carti) == len(other.carti)
