# HW1-SandBox.py
import numpy as np

print("Hello World")
# np.array()

# Object to represnt the actual maze that we will be building 5 X 5 maze 
class Maze:
    def __init__(self):
        self.x_val= int
        self.y_val= int
        self.size = int
        self.matrix = [] 

    def set_maze_size(self):
        while True:
            print("What is the vertical size of the maze?\n\tX-values >>>")
            try: 
                x = int(input())
                break     
            except:
                print("Please enter size in a numerical value representation (i.e. 1, 2, 3, ect.).")


        while True:
            print("What is the horizontal size of the maze?\n\ty-values >>>")
            try:
                y = int(input())
                if y != x:
                    print(f"Must be same size as {x}, maze not com")
                else:
                    break
            except:
                print("Please enter size in a numerical value representation (i.e. 1, 2, 3, ect.).")


           

        self.x_val = x
        self.y_val = y
        self.size = x * y
        set_iter = 1

        array_str = ""

        # Building string numpy.matrix() i.e. 2x2; numpy.matrix("1 2; 3 4") = [[1, 2][3, 4]] tuple type. 
        for i in range(0, self.size):
            if set_iter % 5 == 0:
                array_str += " " + str(i + 1) + ";"
                set_iter = 1
            else:
                array_str += " " + str(i + 1)
                set_iter += 1
        # Clean up string to pass to numpy for building a matrix
        string_to_matrix = array_str.rstrip(";").lstrip()
        self.matrix = np.matrix(string_to_matrix)




maze = Maze()

maze.set_maze_size()

print(maze.size)

print(maze.matrix)



