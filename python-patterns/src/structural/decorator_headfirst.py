#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-

class Beverage:
    def setSize(self,size):
        self.size = size
    def getSize(self):
        return self.size
        

class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
        self.cost = 1.99
class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"
        self.cost = .99
class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf Coffee"
        self.cost = 1.05      
class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"
        self.cost = .89  
       



if __name__ == '__main__':
    beverage = Espresso()
    print("{} ${:.2f}".format(beverage.description, beverage.cost))
    beverage2 = DarkRoast()
#     beverage2 = Mocha(beverage2)
#     beverage2 = Mocha(beverage2)
#     beverage2 = Whip(beverage2)
    print("{} ${:.2f}".format(beverage2.description , beverage2.cost))
    beverage3 = HouseBlend()
#     beverage3.setSize(Size.VENTI)
#     beverage3 = Soy(beverage3)
#     beverage3 = Mocha(beverage3)
#     beverage3 = Whip(beverage3)
    print("{} ${:.2f}".format(beverage3.description, beverage3.cost))

    
    
    