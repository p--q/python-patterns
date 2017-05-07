#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-




class Event(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


class Observable(object):  # Subject
    def __init__(self):
        self.callbacks = set()

    def subscribe(self, callback):
        self.callbacks.add(callback)
        
    def unsubscribe(self, callback):
        self.callbacks.discard(callback)

    def fire(self, **attrs):
        e = Event(source=self, **attrs)
        for fn in self.callbacks:
            fn(e)












# class Point(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def scale(self, n):
#         self.x = n * self.x
#         self.y = n * self.y
# def notify(f):
#     def g(self, n):
#         print(n)
#         return f(self, n)
#     return g
# # Point.scale = notify(Point.scale)
#  
# p = Point(2.0, 3.0)
#  
# # p.scale(2.5)
# 
# 
# class Wrapper(object):
#     def __init__(self,wrapped,*callbacks):
#         self.wrapped = wrapped
#         self.callbacks = callbacks
# 
#     def __getattr__(self,name):
#         res = self.wrapped.__getattribute__(name)
#         if not callable(res):
#             return res
#         def wrap(*args,**kwargs):
#             for c in self.callbacks:
#                 c(self.wrapped,*args,**kwargs)
#             return res(*args,**kwargs)
#         return wrap
# 
#     def __str__(self):
#         return self.wrapped.__str__()
# 
# #in this example I will keep a record of each call performed on a list
# called = []
# #this is the list
# a = []
# 
# # f = notify
# 
# #and this is the wrapped list
# w = Wrapper(a,lambda f,v: called.append((f,v)) )
# #I append an element to the wrapper
# w.append(1)
# 
# w.append(2)
# w.append(3)
# w.append(4)
# 
# 
# #and I can see that it modify the original list
# print(a)
# #the print of the wrapped is well behaved, having defined the __str__ function
# print(w)
# #and we can see which function we called and which were the parameters
# print(called)






# class User:
#     _persist_methods = ['get', 'save', 'delete']
# 
#     def __init__(self, persister):
#         self._persister = persister
# 
#     def __getattr__(self, attribute):
#         if attribute in self._persist_methods:
#             return getattr(self._persister, attribute)
# 
# 
# duck = User("get")
# 
# duck.get

# def hello():
#     return "hello world"
# 
# 
# class Wrapper:
#     def __init__(self,wrapped,*callbacks):
#         self.wrapped = wrapped
#         self.callbacks = callbacks
# 
#     def __getattr__(self,name):
#         res = self.wrapped.__getattribute__(name)
#         if not callable(res):
#             return res
#         def wrap(*args,**kwargs):
#             for c in self.callbacks:
#                 c(self.wrapped,*args,**kwargs)
#             return res(*args,**kwargs)
#         return wrap
# 
#     def __str__(self):
#         return self.wrapped.__str__()
# 
# #in this example I will keep a record of each call performed on a list
# called = []
# #this is the list
# a = []
# #and this is the wrapped list
# w = Wrapper(a,lambda f,v: called.append((f,v)) )
# #I append an element to the wrapper
# w.append(1)
# #and I can see that it modify the original list
# print(a)
# #the print of the wrapped is well behaved, having defined the __str__ function
# print(w)
# #and we can see which function we called and which were the parameters
# print(called)


# w.append(hello)
# #and I can see that it modify the original list
# print(a)
# #the print of the wrapped is well behaved, having defined the __str__ function
# print(w)
# #and we can see which function we called and which were the parameters
# print(called)



# def makebold(fn):
#     def wrapped():
#         bold = "<b>" + fn() + "</b>"
#         print(bold)
#         return fn()
# #         return "<b>" + fn() + "</b>"
#     return wrapped
# 
# def makeitalic(fn):
#     def wrapped():
#         italic = "<i>" + fn() + "</i>"
#         print(italic)
#         return wrapped
# #         return "<i>" + fn() + "</i>"
#     return wrapped
# 
# 
# 
# # @makebold
# # @makeitalic
# def hello():
#     return "hello world"
# 
# 
# # hello = makeitalic(hello)
# # hello = makebold(hello)
# 
# hello = makebold(makeitalic(hello))
# 
# # print(hello()) ## returns "<b><i>hello world</i></b>"
# hello()





# class Point(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def scale(self, n):
#         self.x = n * self.x
#         self.y = n * self.y
# def notify(f):
#     def g(self, n):
#         print(n)
#         return f(self, n)
#     return g
# Point.scale = notify(Point.scale)
# 
# p = Point(2.0, 3.0)
# 
# p.scale(2.5)





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