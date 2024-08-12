class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print("Hello, my name is {} and I am {} years old.".format(self.name, self.age))

human1 = Person("TY",36)
human1.greeting()
