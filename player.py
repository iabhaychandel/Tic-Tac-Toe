import math
import random


class player:
    def __init__(self, letter) -> None:
        #Letter maybe x or O
        self.letter = letter


    def get_move(self, game):
            pass

class randomComputerPlayer(player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    
    def get_move(self, game):
        pass
class HumanPlayer(player):
     def __init__(self, letter) -> None:
          super().__init__(letter)

     def get_move(self, game):
            
         pass

