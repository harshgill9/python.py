# class Animal:
#     def speak(self):
#         return "I make a sound"

# class Dog(Animal):
#     def speak(self):
#         return "Bark!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# dog = Dog()
# cat = Cat()
# print(dog.speak()) 
# print(cat.speak())

class A:
    def method_A(self):
        return "Method from A 789"
    def method_B(self):
        return "Method from B 456"

class B:
    def method_B(self):
        return "Method from  123"

class C(A, B):
    def method_B(self):
        return "Method from B 000"

obj = C()