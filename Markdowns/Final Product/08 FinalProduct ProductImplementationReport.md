# Product Implementation Report

## Technical Diagrams

<img src="Backtracking Diagram.png" alt="solver">

The above shows the visualisation of the for loops of the solver, by going through each iterations for each cells to determine the possible solution, once the possible solutions fail to continue any further the program it self will go back to previous iterations to solve for the previous cells to continue with other possible solutions.

## Technical Description

The code is built upon using the coding laugage known as Python and was coded in Visual Studio Code. However we did imported a library to aid in the process of coding this game. The library is known as Pygame, it is meant for game designing thus we chose this library among all the other choice.

There are 2 important functions in this code, they are known as:

1. solvegame()
2. drawlines()

In the solvegame function, the main algorithm is to use the for loop to go through the highest number in a square of the given base number, e.g. if the base number is 3, the square of 3 is 9, thus the for loop will go through 9 iterations of for loop for a base number of 3 soduku. However 9 iterations is only for one axis, since we are dealing with 2D array, there is another axis thus there will be a total of 9x9 iterations per cell for the code to try on before finding the right combination.

    def solvegame(self, defaultgrid, i, j):

        while defaultgrid[i][j] != 0:
            if i < self.int_rangeNumber-1:
                i += 1
            elif i == self.int_rangeNumber-1 and j < self.int_rangeNumber-1:
                i = 0
                j += 1
            elif i == self.int_rangeNumber-1 and j == self.int_rangeNumber-1:
                return True
        pygame.event.pump()
        for it in range(1, self.int_rangeNumber+1):
            if self.validvalue(defaultgrid, i, j, it) == True:
                defaultgrid[i][j] = it
                global int_x, int_z
                int_x = i
                int_z = j
                self.drawlines(defaultgrid, False)

In the drawlines functions, the random samples of generating numbers to be placed into the grid are found in the code too. First, numbers are obtained through the determining the max range of the numbers to be used, then calculate the amount of rows and columns involved. At the same time the numbers will then be shuffled and mutliplied by a factor of 75% to produce empty cells for the user to solve or the program to solve.

    def pattern(self, r, c):
        return (self.int_base*(r % self.int_base)+r//self.int_base+c) % self.int_side

    def shuffle(self, s):
        return sample(s, len(s))

    def defaultgrid(self):
        rint_Base = range(self.int_base)
        int_rows = [g*self.int_base +
                    r for g in self.shuffle(rint_Base) for r in self.shuffle(rint_Base)]
        int_cols = [g*self.int_base +
                    c for g in self.shuffle(rint_Base) for c in self.shuffle(rint_Base)]
        self.nums = self.shuffle(range(1, self.int_base*self.int_base+1))
        # produce board using randomized int_baseline pattern
        defaultgrid = [[self.nums[self.pattern(r, c)] for c in int_cols] for r in int_rows]

        self.squares = self.int_side * self.int_side
        self.empties = self.squares * 3//4
        for p in sample(range(self.squares), self.empties):
            defaultgrid[p//self.int_side][p % self.int_side] = 0

        return defaultgrid

## Algorithms and Data Structures

In soduku, the most prominent form of data structures we have used is array or some might know it as 2D array as this forms the base of the soduku game.

In a 2D array, the variables in this case are numbers/integers, they are surrounded by 2 square brackets. "0" denoting the cell as empty, and anything more than 0 is considered as the number to be printed as it self.

Thus a sample of a 3x3 grid would look something like this:

     defaultgrid = [[8, 0, 3, 1, 0, 7, 0, 9, 4],
                    [7, 5, 0, 0, 0, 6, 8, 0, 2],
                    [0, 0, 9, 0, 0, 0, 0, 5, 7],
                    [6, 3, 1, 5, 0, 0, 0, 2, 0],
                    [0, 0, 0, 0, 0, 2, 0, 3, 5],
                    [0, 7, 0, 0, 3, 0, 0, 0, 0],
                    [0, 0, 7, 0, 1, 5, 2, 0, 0],
                    [4, 0, 2, 7, 0, 0, 0, 8, 1],
                    [5, 0, 0, 9, 2, 0, 4, 7, 0]]

The main algorithm that we used to solve the soduku is by using a for loop that goes through each number that exsist in a square of a give number, e.g. if the given number is 2, square of 2 is 4, thus the for loop will be going through 4 to 1 in a given cell and compare if the cell is a possible solution, else the algorithm will procceed backwards and decrease the possible number down until it fulfils the criteria and solves the puzzle.

This method is known as backtracking

Another form of algorithm we used to generate the puzzle is by calling on the random module and generating out numbers to fill up all the grids in the 2D array then by using a percentage to determine the number of cells to be of null value thus allowing the user/bot to solve the puzzle.

The complexity is definitely the hardest when formulating an algorithm to solve the soduku by using a for loop, as it requires a great extend of visualisation of numbers going through a loop.

## Imported Libraries

The imported libraries we have used is Pygame. Pygame is a set of Python language based modules used for writing video games. In Pygame a lot of the methods can be used efficiently as the objective is to create a video game and a program to solve the video game

The best thing about Pygame is that it runs on every operating system, from Mac OS to Linux to Windows.

In Pygame, multicore CPU can be used to speed up the video game, since multicore CPU are widely available nowadays.

Lastly, the most important feature about Pygame is that it its simple and easy to use as the documentation and references are all stated in their website plus examples can be found in Stackoverflow website.

In short the benefits of Pygame can be listed in these point forms.

1. Runs on multiple operating systems
2. Able to tap on multicore CPUs
3. Documentation and references readily available
4. Examples can be found easily on Stackoverflow

## Known Issues

The issues that exsists are

1. Takes few days to solve 4x4 soduku and above
