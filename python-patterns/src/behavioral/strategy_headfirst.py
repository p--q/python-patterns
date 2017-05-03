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
    def muteQuack(self):
        print("<< Silence >>")
    def quack(self):
        print("Quack")
    def squeak(self):
        print("Squeak")
    def fakeQuack(self):
        print("Qwak")
class Duck(FlyBehavior,QuackBehavior): 
    def swim(self):
        print("All ducks float, even decoys!") 
class DecoyDuck(Duck):
    def __init__(self,name):
        self.name = name
        self.performFly = self.flyNoWay 
        self.performQuack = self.muteQuack
    def display(self):
        print(self.name + " is a duck Decoy")
class MallardDuck(Duck):
    def __init__(self,name):
        self.name = name
        self.performFly = self.flyWithWings
        self.performQuack = self.quack
    def display(self):
        print(self.name + " is a real Mallard duck")
class ModelDuck(Duck):
    def __init__(self,name):
        self.name = name
        self.performFly = self.flyNoWay 
        self.performQuack = self.quack
    def display(self):
        print(self.name + " is a model duck")
class RedHeadDuck(Duck):
    def __init__(self,name):
        self.name = name
        self.performFly = self.flyWithWings
        self.performQuack = self.quack
    def display(self):
        print(self.name + " is a real Red Headed duck")     
class RubberDuck(Duck):
    def __init__(self,name):
        self.name = name
        self.performFly = self.flyNoWay 
        self.performQuack = self.squeak
    def display(self):
        print(self.name + " is a rubber duckie")   
if __name__ == '__main__':
    mallard = MallardDuck("mallard")
    rubberDuckie = RubberDuck("rubberDukie")
    decoy = DecoyDuck("decoy")
    model = ModelDuck("model")
    
    mallard.performQuack()
    rubberDuckie.performQuack()
    decoy.performQuack()
   
    model.performFly()  
    model.performFly = model.flyRocketPowered  # インスタンスのメソッドを置換。
    model.performFly()
    
    model2 = ModelDuck("model2")
    model2.performFly()  # 他のインスタンスのメソッドは置換されない。
    

    