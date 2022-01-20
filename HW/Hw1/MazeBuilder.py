# HW1-SandBox.py
import numpy as np
import ast 
import matplotlib.pyplot as pyplot
import sys 
import math

# Class to build the maze
class BuildMaze:
    def __init__(self, _start={}, _end={}, _size=int):

        self.size = _size
        self.start = _start
        self.end = _end
        self.matrix = [] 
        self.barriers = []

    def change_maze_size(self, N):

        # Allows user to input own size of maze
        while True:
            try: 
                x = int(N)
                break     
            except:
                print("Please enter size in a numerical value representdation (i.e. 1, 2, 3, ect.).", end="")
                N= input()
                if N == "no":
                    x = int(math.sqrt(self.size)) 
                    break
        self.size = x * x
        pass

    def add_barrier(self):

        #Add barrier option not needed but satarted if that changes
        added_in_barriers=[]
        print("\tWould you like to add another barrier?")
        print("\tIf not enter \'no\' >>>", end="")
        user_choice = input()
        while user_choice != "no":
            user_added_barriers = []
            while True:
                print("\tWhere is the barrier in the x direction on the maze?\n\t\tx-value >>>", end="")
                try: 
                    x = int(input())
                    break     
                except:
                    print("\tPlease enter size in a numerical value representation (i.e. 1, 2, 3, ect.).")
            while True:
                print("\tWhere is the barrier in the y direction on the maze?\n\t\ty-value >>>", end="")
                try: 
                    y = int(input())
                    break     
                except:
                    print("\tPlease enter size in a numerical value representation (i.e. 1, 2, 3, ect.).")
        
            user_added_barriers = [x, y]
            added_in_barriers += [user_added_barriers]
            print("\tWould you like to add another barrier?\n\tEnter anything to contiue,\n\tor no to quit >>>", end="")
            user_choice = input()
        return added_in_barriers       

    def set_maze_size(self):

        # # Reads in size from test file first line
        with open("C:/Users/Admin/OneDrive/Documents/School/CS-4080 Reinforcment Learning/HW/Hw1/MazeTestFile1.txt") as file:
            data = file.readlines()

            # Build string of first number entered in test file
            size_str = ""
            for digit in data[0]:
                if digit == " ":
                    break
                else:
                    size_str += digit

            # # Change maze size?
            # print("Want to change maze size?")
            # print("If so enter the size for a N by N maze,")
            # print("if not enter in \'no\' >>> ", end="")
            # chng_sze = input()
            # if chng_sze.lower() != "no":
            #     self.change_maze_size(chng_sze)
            # else:    
            #     # Setting maze size
            #     self.size = int(size_str) * int(size_str)

            # UNCOMMENT BELOW V V With out change_maze_size
            self.size = int(size_str) * int(size_str)

    def set_maze_barriers(self):
        with open("C:/Users/Admin/OneDrive/Documents/School/CS-4080 Reinforcment Learning/HW/Hw1/MazeTestFile1.txt") as file:
            data = file.readlines()
        barrier_str = ""
        for character in data[1]:
            if character == ";":
                break
            else:
                barrier_str += character

        self.barriers = ast.literal_eval(barrier_str)
        
        # Uncomment for acces to user to add barrier
        # self.barriers += self.add_barrier()

        try:
            for i, j in self.barriers:
                self.matrix.itemset((i-1, j-1), float(0)) 
        except:
            print("Make sure barriers are contained within the maze" )  

    def build_Maze(self):
        # Get (from file user option not avliable) and set maze size
        self.set_maze_size()

        # Building string numpy.matrix() i.e. 2x2; numpy.matrix("1 2; 3 4") = [[1, 2][3, 4]] tuple type. 
        set_iter = 1
        array_str = ""
        for i in range(0, self.size):
            if set_iter % 5 == 0:
                array_str += " " + str(1.0) + ";"
                set_iter = 1
            else:
                array_str += " " + str(1.0) + "," 
                set_iter += 1

        # Clean up string to pass to numpy for building a matrix
        string_to_matrix = array_str.rstrip(";").lstrip()
        # print(string_to_matrix)
        self.matrix = np.matrix(string_to_matrix)

        # # Print OG maze 
        # print(self.matrix)

        # Get (From file and user optional) and set barrier into maze
        self.set_maze_barriers()

        # # Print new maze with barriers
        # print(self.matrix)

    def get_maze_size(self):
        return self.size

    def get_maze_barriers(self):
        return self.barriers

        
