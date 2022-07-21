class A:
    def __init__(self):
        self.field = 2
        self.__qwe = 5

    @classmethod
    def fn(cls):
        return cls.__qwe

    def fn2(self):
        return self.__qwe

a = A()
