
class Human:
    def power(self):
        print("Human power")

    def human(self):
        print("I'm human")

    def special_one(self):
        print("Special One")


class Woman:
    def power(self):
        print("Woman power")

    def woman(self):
        print("I'm a woman")


class Superwoman(Human, Woman):
    def power(self):
        print("I'm a woman, a bit more powerfull than a human")


if __name__ == "__main__":
    s = Superwoman()
    s.power()
    s.human()

    s.special_one()

    s.woman()