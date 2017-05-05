#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def scale(self, n):
        self.x = n * self.x
        self.y = n * self.y
def notify(f):
    def g(self, n):
        print(n)
        return f(self, n)
    return g
Point.scale = notify(Point.scale)

p = Point(2.0, 3.0)

p.scale(2.5)





# import types
# def flyNoWayWithName(self):
#     print(self.name + " can't fly") 
# def flyRocketPoweredWithName(self):
#     print(self.name + " is flying with a rocket")    
# class Duck:    
#     def swim(self):
#         print("All ducks float, even decoys!") 
# class ModelDuck2(Duck):
#     def __init__(self,name):
#         self.performFly = types.MethodType(flyNoWayWithName,self) 
#         self.name = name  
# carue2 = ModelDuck2("Carue2")
# carue2.performFly()  
# ModelDuck2.performFly = flyRocketPoweredWithName
# carue2.performFly()  