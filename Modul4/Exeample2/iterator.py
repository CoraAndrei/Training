class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        print("I got called with {}".format(self.current))
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


if __name__ == "__main__":
    counter = Counter(2, 10)
    print(counter)
    for elem in counter:
        print(elem)