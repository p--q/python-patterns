#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-
import types
def flyNoWayWithName(self):
    print(self.name + " can't fly") 
def flyRocketPoweredWithName(self):
    print(self.name + " is flying with a rocket")    
class Duck:    
    def swim(self):
        print("All ducks float, even decoys!") 
class ModelDuck2(Duck):
    def __init__(self,name):
        self.performFly = types.MethodType(flyNoWayWithName,self) 
        self.name = name  
carue2 = ModelDuck2("Carue2")
carue2.performFly()  
ModelDuck2.performFly = flyRocketPoweredWithName
carue2.performFly()  