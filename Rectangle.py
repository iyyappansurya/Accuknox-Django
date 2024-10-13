import json

class Rectangle:
    def __init__(self,length:int,width:int):
        self.length = length
        self.width = width
    def getValues(self):
        yield({'length':self.length})
        yield({'width':self.width})  

rec = Rectangle(4,5)
for i in rec.getValues():
    print(i)
