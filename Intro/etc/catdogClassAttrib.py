class Cat ():
    numCats = 0
    
    def __init__(self, name = "fluffy"):
        self.myName = name
        self.id = Cat.numCats
        Cat.numCats = Cat.numCats + 1
        
    def getName(self):
        return self.myName

    def __repr__(self):
       return ('<Cat named {} (id = {})>'.format(self.myName, self.id))
    
    def speak(self):
        print("meow")

class Dog ():

    def __init__(self, name = "rover"):
        self.myName = name

    def getName(self):
        return self.myName
    
    def __repr__(self):
       return ('<Dog named {}>'.format(self.myName))
    
    def speak(self):
        print("woof")

    def fetch(self):
        print("I am fetching")

