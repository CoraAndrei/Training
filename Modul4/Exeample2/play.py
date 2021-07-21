from Modul4.Exeample2.pachet import Pachet

pachet_1 = Pachet()
pachet_2 = Pachet()

print(pachet_1 != pachet_2)  ## Au aceleasi liste as in Culori si vlaori

pachet_1.shuffle()
pachet_2.shuffle()

Andreea = print(f"Andreea - {pachet_1.deal()}")
Andreea_1 = print(f"Andreea_1 - {pachet_1.deal()}")
Lidia = print(f"Lidia - {pachet_1.deal()}")
Lidia_2 = print(f"Lidia_2 - {pachet_1.deal()}")
Oana = print(f"Oana - {pachet_1.deal()}")
Oana_2 = print(f"Oana_2 - {pachet_1.deal()}")
Daniel = print(f"Daniel - {pachet_1.deal()}")
Daniel_2 = print(f"Daniel_2 - {pachet_1.deal()}")
Sergiu = print(f"Sergiu - {pachet_1.deal()}")
Sergiu_2 = print(f"Sergiu_2 - {pachet_1.deal()}")

Deaalerz_1 = print(f"Deaalerz_1 - {pachet_1.deal()}")
Deaalerz_2 = print(f"Deaalerz_2 - {pachet_1.deal()}")
Deaalerz_3 = print(f"Deaalerz_3 - {pachet_1.deal()}")
Deaalerz_4 = print(f"Deaalerz_4 - {pachet_1.deal()}")
Deaalerz_5 = print(f"Deaalerz_5 - {pachet_1.deal()}")

# Andreea - Q Negru -9 Negru
# Lidia - 5 Romb-5 Negru
# Oana - 9 Rosu -3 Negru
# Daniel - 3 Trefla - 9 Romb
# Segiul - 8 Trefla - 6 Romb

# 6 - romb  |  4 - trefla | 8 - negru | 5 rosu | 10 - rosu
