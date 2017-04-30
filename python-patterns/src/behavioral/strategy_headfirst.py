#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-
import types

class Duck:
    def __init__(self):
        self.flyBehavior
        self.quackBehavior

        
        

    def setFlyBehavior(self,func=None):
        if func is not None:
            self.performFly = types.MethodType(func, self)        
    def setQuackBehavior(self,func=None):
        if func is not None:
            self.performQuack = types.MethodType(func, self)    
    def display(self):
        pass
    def performFly(self):
        pass
    def performQuack(self):
        pass
    def swim(self):
        print("All ducks float, even decoys!")
class FlayBehavior:
    def __init__(self,func=None):
        if func is not None:
            self.fly = types.MethodType(func, self)
    def fly(self):
        pass     
class FlyWithWings:
    def fly(self):
        print("I'm flying!!")        
class FlyRocketPowered:
    def fly(self):
        print("I'm flying with a rocket")   
class FlyNoWay:
    def fly(self):
        print("I can't fly")           


class DecoyDuck(Duck):
    def __init__(self):
        self.flyBehavior = None 
        self.quackBehavior = None
    def display(self):
        print("I'm a duck Decoy")
class MallardDuck(Duck):
    def __init__(self):
        self.flyBehavior = None 
        self.quackBehavior = None
    def display(self):
        print("I'm a real Mallard duck")
class ModelDuck(Duck):
    def __init__(self):
        self.flyBehavior = None 
        self.quackBehavior = None
    def display(self):
        print("I'm a model duck")
class RubberDuck(Duck):
    def __init__(self):
        self.flyBehavior = None 
        self.quackBehavior = None
    def display(self):
        print("I'm a rubber duckie")
class RedHeadDuck(Duck):
    def __init__(self):
        self.flyBehavior = None 
        self.quackBehavior = None
    def display(self):
        print("I'm a real Red Headed duck")
        
        
        
        
        
        
if __name__ == '__main__':
    pass