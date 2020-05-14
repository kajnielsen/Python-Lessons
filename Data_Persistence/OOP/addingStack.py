from .stack import stack

class addingStack(stack):
    def __init__(self):
        stack.__init__(self)
        self.__sum = 0

    def getSum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        stack.push(self, val)

    def pop(self):
        val = stack.pop(self)
        self.__sum -= 1
        return val



