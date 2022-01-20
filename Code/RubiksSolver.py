from rubik.cube import Cube
from rubik.solve import Solver

class Game:

    def __init__(self, cube_str="OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"):
        self.cube = Cube(cube_str)
        self.moves = {  'R': self.cube.R(),
                        'L': self.cube.L(),
                        'U': self.cube.U(),
                        'D': self.cube.D(),
                        'B' : self.cube.B(),
                        'F' : self.cube.F(),
                        'Q': None}


    def make_action(self):   
        user_move="" 
        while user_move != 'Q':
            try:                  
                print("Enter in next move or Q to quit.")
                print("Enter in move:", end="")
                user_move = input().upper()
                if user_move not in self.moves:
                    raise
                elif user_move == 'Q':
                    break                    
                else:
                    print("move:", self.moves.get(user_move.items()))
            except:
                print(f"!!! Enter in a valid move !!!\n{self.moves}")
            finally:
                print(self.cube)
            


        

game = Game(cube_str="OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")
game.make_action()
print(game.moves)

Solver(game.cube)