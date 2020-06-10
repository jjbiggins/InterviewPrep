class Cat ():
    numCats = 0
    
    def __init__(self, name = "fluffy"):
        self.myName = name
        Cat.numCats = Cat.numCats + 1
        self.myID = Cat.numCats

    def speak(self):
        print("meow")

    def getName(self):
        return self.myName

    def __repr__(self):
       return ('<Cat named {} (ID#: {})>'.format(self.myName, self.myID))

    def  __eq__ (self, anotherCat):
        return self.myName == anotherCat.getName()

class Dog ():
    
    def speak(self):
        print("woof")

    def fetch(self):
        print("I am fetching")

