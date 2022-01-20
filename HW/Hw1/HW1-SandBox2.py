# HW1-SandBox.py
import numpy as np
import ast 
import matplotlib.pyplot as pyplot
import sys 

VISTITED_MARK = 0.8
MARK = 0.5
LEFT = 0
UP = 1
RIGHT =2
DOWN = 3

actions = {
    LEFT: 'Left',
    RIGHT: 'Right',
    UP: 'up',
    DOWN: 'down',
}

num_actions = len(actions)

# Exploration factor
epsilon = 0.1


print(sys.path[0])




# Object to represnt the actual maze that we will be building 5 X 5 maze 
class Maze:
    def __init__(self):

        self.size = int
        self.matrix = [] 
        self.barriers = []

    def set_maze_size(self):
        # while True:
        #     print("What is the size of the maze?\t >>>")
        #     try: 
        #         x = int(input())
        #         break     
        #     except:
        #         print("Please enter size in a numerical value representation (i.e. 1, 2, 3, ect.).")
        with open("C:/Users/Admin/OneDrive/Documents/School/CS-4080 Reinforcment Learning/HW/Hw1/MazeTestFile1.txt") as file:
            data = file.readlines()
            self.size = int(data[0][0:3])
        # Building string numpy.matrix() i.e. 2x2; numpy.matrix("1 2; 3 4") = [[1, 2][3, 4]] tuple type. 
        set_iter = 1 
        array_str = ""
        for i in range(0, self.size):
            if set_iter % int((self.size ** 0.5)) == 0:
                array_str += " " + str(1) + ";"
                set_iter = 1
            else:
                array_str += " " + str(1)
                set_iter += 1
        # Clean up string to pass to numpy for building a matrix
        string_to_matrix = array_str.rstrip(";").lstrip()
        self.matrix = np.matrix(string_to_matrix)
    
    def set_maze_barriers(self):
        #Add barrier option not needed but satarted if that changes
        # user_choice = " "
        # while user_choice != "exit":
        #     while True:
        #         print("Where is the barrier in the x direction on the maze?\n x-value >>>")
        #         try: 
        #             x = int(input())
        #             break     
        #         except:
        #             print("Please enter size in a numerical value representation (i.e. 1, 2, 3, ect.).")
        #     while True:
        #         print("Where is the barrier in the y direction on the maze?\n y-value >>>")
        #         try: 
        #             y = int(input())
        #             break     
        #         except:
        #             print("Please enter size in a numerical value representation (i.e. 1, 2, 3, ect.).")
        #
        #     user_added_barriers = []
        #     user_added_barriers += [[x, y]]
        #     print("Would you like to add another barrier? (Enter anything to contiue, enter exit to quit")
        #     user_choice = input()
        #
        # Delete this line below inuncommenting out addbarrier choise for users
        user_added_barriers = []

        with open("C:/Users/Admin/OneDrive/Documents/School/CS-4080 Reinforcment Learning/HW/Hw1/MazeTestFile1.txt") as file:
            data = file.readlines()
            self.barriers = ast.literal_eval(data[1])
        
        self.barriers += user_added_barriers
        print(self.barriers)

        for i, j in self.barriers:
            print(i, j)
            self.matrix.itemset((i-1, j-1), float(0))   

    def build_maze(self):
        #pyplot.plot(self.matrix)
        pyplot.matshow(self.matrix, cmap='hot')
        pyplot.show()
        

maze = Maze()
maze.set_maze_size()
print(maze.size)
print(maze.matrix)
print(maze.set_maze_barriers())
print(maze.matrix)
maze.build_maze()



