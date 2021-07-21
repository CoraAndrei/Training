## o Class Computer , met init max price = 1000, seel price , met set price

class Computer:
    def __init__(self):
        self.__maxprice = 1000

    def sell(self):
        print(f"Selling Price:{self.__maxprice}")
        # print("Selling Price:{}".format(self.__max_price))

    def setMaxPrice(self, price):
        self.__maxprice = price


# Show Sell Price

c = Computer()
c.sell()

# Change the price
c.setMaxPrice(9999)
c.sell()



# Class Masina, viteza_maxima,

class Masina():
    def __init__(self, viteza_maxima):
        self.viteza_maxima = viteza_maxima


    def __add__(self, other):
        return self.viteza_maxima + other.viteza_maxima


audi = Masina(51)
bmw = Masina(49)

total_viteza = audi + bmw
print(f"Viteza combinata este : {total_viteza}")


    def __lt__(self, other):
        return self.viteza_maxima < other.viteza_maxima


audi = Masina(51)
bmw = Masina(49)

total_viteza = audi < bmw

print(total_viteza)


class Area:
    def find_area(self, a=None, b=None):
        if a != None and b != None:
            print("Rectangle:", (a * b))
        elif a != None:
            print("square:", (a * a))
        else:
            print("No input / figure was assigned")


obje1 = Area()

obje1.find_area()  #    o input / figure was assigned
obje1.find_area(10)  #     100
obje1.find_area(10, 20)  #   200
