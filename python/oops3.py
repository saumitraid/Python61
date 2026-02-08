# Parent class
class Animal:
    def eat(self):
        print("Eating")

#Child Class
class Dog(Animal): 
    def bark(self):
        print("barking");

obj=Dog()
obj.eat()
obj.bark()