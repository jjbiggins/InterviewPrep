class Box:
   
    def __init__ (self, centerX = 0.0, centerY = 0.0, centerZ = 0.0, width=0, height = 0, depth = 0):
        self.centerX = centerX
        self.centerY = centerY
        self.centerZ = centerZ
        self.width = width
        self.height = height
        self.depth = depth

    def setCenter(self, x, y, z):
        self.centerX = x
        self.centerY = y
        self.centerZ = z
        
    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def setDepth(self, depth):
        self.depth = depth
        
    def volume(self):
        return (self.width * self.height * self.depth)

    def surfaceArea(self):
        return (2*self.width*self.height+ 2*self.width*self.depth+ 2*self.height*self.depth)

    #  This solution works by essentially saying:
    #      they DON'T OVERLAP IF THEIR x-centers are too far apart
    #                                                            y-centers are too far apart
    #                                                            z-centers are too far apart
    #      otherwise they DO overlap
    #
    def overlaps(self, otherBox):
        if abs(self.centerX - otherBox.centerX) > (self.width + otherBox.width)/2.0:
            return False
        if abs(self.centerY - otherBox.centerY) > (self.height + otherBox.height)/2.0:
            return False
        if abs(self.centerZ - otherBox.centerZ) > (self.depth + otherBox.depth)/2.0:
            return False
        return True
    
    def contains(self, otherBox):
        if abs(self.centerX - otherBox.centerX) > (self.width - otherBox.width)/2.0:
            return False
        if abs(self.centerY - otherBox.centerY) > (self.height - otherBox.height)/2.0:
            return False
        if abs(self.centerZ - otherBox.centerZ) > (self.depth - otherBox.depth)/2.0:
            return False
        return True
        
    def __repr__(self):
        return '< {}-by-{}-by-{} 3d box with center at ({},{},{}) >'.format(self.width, self.height, self.depth, self.centerX, self.centerY, self.centerZ)

def testQ1():
    def testOverlap(testnum, b1, b2, correctRes):
        res1 = b1.overlaps(b2)
        res2 = b2.overlaps(b1)
        print("Overlap test {} produced: {}, {}. {}".format(testnum, res1, res2, "CORRECT" if ((res1 == correctRes) and (res2 == correctRes)) else "INCORRECT"))
    box1 = Box(10.0, 5.0, 0.0, 2, 1, 1)
    print(box1)
    box2 =  Box(0, 0, 0, 3.5, 2.5, 1)
    res = box1.volume()
    print("box1.volume() produced: {}. {}".format(res, "CORRECT" if (res==2.0) else "INCORRECT"))
    res = box2.surfaceArea()
    print("box2.surfaceArea() produced: {}. {}".format(res, "CORRECT" if (res==29.5) else "INCORRECT"))
    testOverlap(1, box1, box2, False)
    box1.setCenter(2.75, 0.0, 0.0)
    testOverlap(2, box1, box2, True)
    box1.setCenter(2.76, 0.0, 0.0)
    testOverlap(3, box1, box2, False)
    box1.setCenter(2.75, 1.75, 1.0)
    testOverlap(4, box1, box2,True)
    box1.setCenter(0.0, 0.0, 0.0)
    testOverlap(5, box1, box2, True)   
    box1.setWidth(50.0)
    testOverlap(6, box1, box2, True)    
    box1.setDepth(50.0)
    testOverlap(7, box1, box2,True) 
    box3 = Box(-1.0, -1.0, -1.0, 1, 1, 1)
    box4 = Box(0, 0, 0, 1, 1, 1)
    testOverlap(8, box3, box4,True)    
    box3.setCenter(-1.0, -1.01, -1.01)
    testOverlap(8, box3, box4, False)    
    box3.setWidth(1000.0)
    box4.setDepth(5.0)
    testOverlap(9, box3, box4, False)       
    box4.setHeight(2.0)
    testOverlap(10, box3, box4, True)
    def testContains(testnum, b1, b2, correctRes1, correctRes2):
        res1 = b1.contains(b2)
        res2 = b2.contains(b1)
        print("Contains tests {} produced: {}, {}. {}".format(testnum, res1, res2, "CORRECT" if ((res1 == correctRes1) and (res2 == correctRes2)) else "INCORRECT"))
    box5 = Box(1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    testContains(1, box5, box5, True, True)
    box6 = Box(1.0, 1.0, 1.0, 1.0, 1.1, 1.0)
    testContains(2, box5, box6, False, True)   
    box7 = Box(1.0, 1.0, 1.0, 1.0, 1.0, 1.1)
    testContains(3, box5, box7, False, True)
    box5.setWidth(2.0)
    box5.setHeight(2.0)
    box5.setDepth(1.1)
    testContains(4, box5, box7, True, False)
    box5.setCenter(1.0, 0.0, 0.0)
    testContains(5, box5, box7, False, False)

