class int:
    def __init__(self,value):
        self.__value = value
    def __add__(self, other):
        return self.__value + other.__value
    def __repr__(self):
        return self.__value
    def __str__(self):
        return str(self.__value)
    def __sub__(self, other):
        return self.__value - other.__value
    def __mul__(self, other):
        print("MUL")
        if type(other) == int:
            return self.__value*other
(10+(11))