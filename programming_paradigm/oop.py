"""class item:
    def __init__(self, name):
        print(f"Item created: {name}")
    def calculate_total_price(self, x, y):
        return x * y

#assigning attributes to the class
item1 = item("phone")
item1.name = "phone"
item1.price = 1000
item1.quantity = 5

item2 = item("laptop")
item2.name = "laptop"  
item2.price = 1500
item2.quantity = 3
"""
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print(f"Person {self.name} is being deleted")
        
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
    
    def __del__(self):
        print(f"Book '{self.title}' by {self.author} is being deleted")
        """
class Animal:
        def eat(self):
            print("the animal is eating")
        
        def sleep(self):
            print("the animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("the dog is barking")
    
    def eat(self):
        print("the dog is eating")
    
    def sleep(self):
        print("the dog is sleeping")
        
def demonstrate_inheritance():
    generic_animal = Animal()
    print("Generic Animal:")
    generic_animal.eat()
    generic_animal.sleep()
    print()
    
    my_dog = Dog()
    print("My Dog:")
    my_dog.eat()
    my_dog.sleep()  
    my_dog.bark()
    
    demonstrate_inheritance()           
        