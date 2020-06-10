
class Animal ():
    
    numAnimals = 0

    def __init__ (self, name = 'NoName', numLegs = 0):
        self.name = name
        self.numLegs = numLegs
        self.id = Animal.numAnimals
        Animal.numAnimals = Animal.numAnimals + 1
        
    def getName(self):
        return self.name
    
    def getNumLegs(self):
        return self.numLegs
   
    def speak(self):
        print("...")

    def __repr__(self):
        return ('Animal(name={}, numlegs={})'.format(self.name, self.numLegs))
    
    def __str__(self):
        return ('<{} the animal(ID#{}))>'.format(self.name, self.id))

class Dog(Animal):
    
    def __init__(self, name = 'rover'):
        Animal.__init__(self, name, 4)
    
    def speak(self):
        print('woof')
        
    def fetch(self):
        print("I'm fetching")

    def __repr__(self):
        return "Dog(name='{}')".format(self.name)
    
    def __str__(self):
        return '<{} the dog(ID#{}))>'.format(self.name, self.id)

        
class Cat(Animal):
    def __init__(self, name = 'noname', furColor = 'unknown'):
        Animal.__init__(self, name, 4)
        self.color = furColor
    
    def speak(self):
        print('meow')

    def getFurColor(self):
        return self.color

    def __repr__(self):
        return ("Cat(name='{}', furColor='{}')".format(self.name, self.color))
    
    def __str__(self):
        return ('<{} the {} cat(ID#{}))>'.format(self.name, self.color, self.id))

