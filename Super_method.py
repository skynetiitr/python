class A:
    def __init__(self):
        print("In init A")

    def function1(self):
        print('This is function1-A')

    def function2(self):
        print('This is function2')

class B():
    def __init__(self):
        #super().__init__()
        print("In init B")

    def function1(self):
        print('This is function1-B')

    def function4(self):
        print('This is function4')

class C(B,A):
    def __init__(self):
        super().__init__()
        print("In init C")
        super().function1()
c1 = C()






