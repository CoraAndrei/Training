from Modul4.Example1.persona import Persoana


class Angajat(Persoana):
    salariu = 200

    def get_salary(self):
        return self.salariu