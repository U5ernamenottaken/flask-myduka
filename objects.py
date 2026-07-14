class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    def say_hello(self):
        print('Hello')
        print('Hello')
        print('Hello')



person1 = Person('Jerald','Male',27)
print(person1.name)
person1.say_hello()