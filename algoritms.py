class AlgoError(BaseException):
    def __init__(self,text):
        pass
class const:
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return str(self.__value)
    def __repr__(self):
        return str(self.__value)
def num_len(num):
    if type(num) == int:
        return len(str(num))
    elif type(num) == float:
        return len(str(num))-1
    else:
        raise ValueError("Num not int or float")