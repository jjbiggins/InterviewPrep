import random

class NimGame():

    def __init__(self, numberOfBalls):
        self.numberOfBallsRemaining = numberOfBalls
        print("Nim game initialized with {} balls.".format(self.numberOfBallsRemaining))

    def take(self, numberOfBalls):
        if (numberOfBalls < 1) or (numberOfBalls > 3) or (numberOfBalls > self.numberOfBallsRemaining):
            print("You can't take that number of balls. Try again.")
        else:
            self.numberOfBallsRemaining = self.numberOfBallsRemaining - numberOfBalls
            print("You took {} balls. {} remain.".format(numberOfBalls, self.numberOfBallsRemaining))
            if self.numberOfBallsRemaining == 0:
                print("You win!")
            else: 
                computerMaxBalls = min(3, self.numberOfBallsRemaining)
                compBallsTaken = random.randint(1,computerMaxBalls)
                self.numberOfBallsRemaining = self.numberOfBallsRemaining - compBallsTaken
                print("Computer took {} balls. {} remain.".format(compBallsTaken, self.numberOfBallsRemaining))
                if self.numberOfBallsRemaining == 0:
                    print("Computer wins!")

   
    
    
