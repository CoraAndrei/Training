#### calls papagal class pinguin with ineritnace


class Parrot:
    def fly(self):
        print("Parrot can Fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:
    def fly(self):
        print("Penguin can't Fly")

    def swim(self):
        print("Penguin can swim")


# comm inteface
def flying_test(bird):
    bird.fly()


# inst obj
Reggy = Parrot()
Sasha = Penguin()

# passing obj
flying_test(Reggy)
flying_test(Sasha)


def swim_test(bird):
    bird.swim()


swim_test(Reggy)
swim_test(Sasha)






class Austria():
    def capital(self):
        print("Viennna is the capital of Aus")

    def language(self):
        print("Austrian is the most spoken L")

    def status(self):
        print("Austria is always in a continu development phase")


class Germany():
    def capital(self):
        print("Berlin is the capital of GER")

    def language(self):
        print("German is the most spoken G")

    def status(self):
        print("German is not always so pleased to see me.")


obj_Austria = Austria()
obj_Germany = Germany()

for country in (obj_Germany, obj_Austria):
    country.capital()
    country.language()
    country.status()


##

# Len
print(len("a a a "))

print(len([10, 30]))


def add(x, y, z=1):
    return x + y + z


print(add(2, 3))
print(add(2, 3, 4))
