class Protected:
    def __init__(self):
        self.__privateVar = 'Public'

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private


obj = Protected()
obj.getPrivate()
obj.setPrivate('Secret')
obj.getPrivate()



class Protected:
    def __init__(self):
        self._protectedVar = 0


obj = Protected()
obj._protectedVar = 'Inbetween'
print(obj._protectedVar)
