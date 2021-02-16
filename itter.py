class TopFive:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration


value = TopFive()

for i in value:
    print(i)
    