class Carte():
    valoare = None
    culoare = None
    def __init__(self,valoare,culoare):
        """"
        ":param valoare: 1,-2,-3,K,Q
        :param culoare: Romb, Trefla,Spada
        """
        self.valoare= valoare
        self.culoare= culoare
    def __str__(self):
        return "{culoare}"-"{valoare}".format(culoare=self.culoare,valoare=self.valoare)
    def __eq__(self, other) -> bool:

      print("EQ an object carte")
      return self.valoare == other.valoare and self.culoare == other.culoare
    def __add__(self, other):
        return self.valoare + other.valoare