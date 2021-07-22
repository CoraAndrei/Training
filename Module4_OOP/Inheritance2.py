# Diamond problem
#		Human
#	 ^         ^
#	/			\
# Woman			Man
# 	 ^ 		    ^
#     \	      /
#	 	Child


class Human:
    def power(self):
        print("Human power")


class Woman(Human):
    def power(self):
        print("Woman power")

    def method2(self):
        print("Woman power method 2!")


class Man(Human):
    def power(self):
        print("Man power")

    def method2(self):
        print("Man power method 2! ")


class Child(Woman, Man):
    def method2(self):
        Man.method2(self)


if __name__ == "__main__":
    s = Child()
    s.power()  # what will be printed here?
    # print(Child.mro())
    # s.method2()