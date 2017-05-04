#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-
class FlyBehavior:
    def flyNoWay(self):
        print(self.name + " can't fly")
    def flyWithWings(self):
        print(self.name + " is flying!!")    
    def flyRocketPowered(self):
        print(self.name + " is flying with a rocket")      
class QuackBehavior: 
    @staticmethod
    def muteQuack():
        print("<< Silence >>")
    @staticmethod
    def quack():
        print("Quack")
    @staticmethod
    def squeak():
        print("Squeak")
    @staticmethod
    def fakeQuack():
        print("Qwak")
class Duck: 
    def swim(self):
        print("All ducks float, even decoys!") 
class DecoyDuck(Duck):
    def __init__(self,name,fb):
        self.name = name
        fb.name = name
        self.performFly = fb.flyWithWings
        self.performQuack = QuackBehavior.quack        
    def display(self):
        print(self.name + " is a duck Decoy")
class MallardDuck(Duck):
    def __init__(self,name,fb):
        self.name = name
        fb.name = name
        self.performFly = fb.flyWithWings
        self.performQuack = QuackBehavior.quack
    def display(self):
        print(self.name + " is a real Mallard duck")
class ModelDuck(Duck):
    def __init__(self,name,fb):
        self.name = name
        fb.name = name
        self.performFly = fb.flyNoWay 
        self.performQuack = QuackBehavior.quack
    def display(self):
        print(self.name + " is a model duck")
class RedHeadDuck(Duck):
    def __init__(self,name,fb):
        self.name = name
        fb.name = name
        self.performFly = fb.flyWithWings
        self.performQuack = QuackBehavior.quack
    def display(self):
        print(self.name + " is a real Red Headed duck")     
class RubberDuck(Duck):
    def __init__(self,name,fb):
        self.name = name
        fb.name = name
        self.performFly = fb.flyNoWay 
        self.performQuack = QuackBehavior.squeak
    def display(self):
        print(self.name + " is a rubber duckie")   
if __name__ == '__main__':
    fb = FlyBehavior()
    mallard = MallardDuck("mallard",fb)
    rubberDuckie = RubberDuck("rubberDukie",fb)
    decoy = DecoyDuck("decoy",fb)
    model = ModelDuck("model",fb)
    
    mallard.performQuack()
    rubberDuckie.performQuack()
    decoy.performQuack()
   
    model.performFly()  
    model.performFly = fb.flyRocketPowered  # インスタンスのメソッドを置換。
    model.performFly()
    
    model2 = ModelDuck("model2",fb)
    model2.performFly()  # 他のインスタンスのメソッドは置換されない。
    

    