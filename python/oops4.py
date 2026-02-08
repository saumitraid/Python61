# Parent class
class Animal:
    def eat(self):
        print("Eating")

#Child Class
class Dog(Animal): 
    def bark(self):
        print("barking");

class Puppies(Dog):
    def weap(self):
        print('weaping.............')


x=Puppies()
x.eat()
x.bark()
x.weap()