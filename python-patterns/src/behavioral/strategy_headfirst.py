#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-
def flyNoWay():
    print("I can't fly")
def flyWithWings():
    print("I'm flying!!")    
def flyRocketPowered():
    print("I'm flying with a rocket")       
def muteQuack():
    print("<< Silence >>")
def quack():
    print("Quack")
def squeak():
    print("Squeak")
def fakeQuack():
    print("Qwak")
class Duck:    
    def swim(self):
        print("All ducks float, even decoys!") 
class DecoyDuck(Duck):
    def __init__(self):
        self.performFly = flyNoWay 
        self.performQuack = muteQuack
    def display(self):
        print("I'm a duck Decoy")
class MallardDuck(Duck):
    def __init__(self):
        self.performFly = flyWithWings
        self.performQuack = quack
    def display(self):
        print("I'm a real Mallard duck")
class ModelDuck(Duck):
    def __init__(self):
        self.performFly = flyNoWay 
        self.performQuack = quack
    def display(self):
        print("I'm a model duck")
class RedHeadDuck(Duck):
    def __init__(self):
        self.performFly = flyWithWings
        self.performQuack = quack
    def display(self):
        print("I'm a real Red Headed duck")     
class RubberDuck(Duck):
    def __init__(self):
        self.performFly = flyNoWay 
        self.performQuack = squeak
    def display(self):
        print("I'm a rubber duckie")   
if __name__ == '__main__':
    mallard = MallardDuck()
    rubberDuckie = RubberDuck()
    decoy = DecoyDuck()
    model = ModelDuck()
    
    mallard.performQuack()
    rubberDuckie.performQuack()
    decoy.performQuack()
   
    model.performFly()  
    model.performFly = flyRocketPowered
    model.performFly()
    
    