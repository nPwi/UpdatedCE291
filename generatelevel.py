from email.policy import default
import pygame
from random import sample

class GenerateLevel():
    def __init__(self, game):
        self.game = game
        self.int_x = 0
        self.int_z = 0
        self.int_sizeOfGame = 650
        self.int_value = 0
        self.int_rangeNumber = 0
        self.int_lineNumber = 0
        self.int_base = 0
        self.int_side = 0
        self.int_diff = 0
        self.font = pygame.font.SysFont("comicsans", 20)
        self.int_difficultyLevel = self.game.int_difficultyLevel
        self.int_rangeNumber = self.int_difficultyLevel * self.int_difficultyLevel
        self.int_lineNumber = self.int_rangeNumber + 1
        self.int_diff = self.int_sizeOfGame / self.int_rangeNumber
        self.int_base = self.int_difficultyLevel
        self.int_side = self.int_base * self.int_base
        self.int_flag = True
        self.int_flag1 = 0
        self.int_flag2 = 0
        self.rs = 0
        self.error = 0
        # Setting clock
        self.clock = pygame.time.Clock()
        self.int_counter = 0
        self.str_countingMinutes = str((self.int_counter//60) % 60).zfill(2)
        self.str_countingSeconds = str(self.int_counter % 60).zfill(2)
        self.str_countingHours = str(self.int_counter//(60*60) % 24).zfill(2)
        self.text = "%s:%s:%s" % (self.str_countingHours, self.str_countingMinutes, self.str_countingSeconds)
        self.timerFont = pygame.font.SysFont('Consolas', 30)
        self.display_counter = 0
        self.singlerunFlag = False

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

    # Inner cord function
    def cord(self, pos):
        self.int_x = pos[0]//self.int_diff
        self.int_z = pos[1]//self.int_diff

    # Inner function for grid selection highlights
    def highlightboint_x(self):
        for k in range(2):
            pygame.draw.line(self.game.display, (255, 255, 255), (self.int_x * self.int_diff-3, (self.int_z + k)
                             * self.int_diff), (self.int_x * self.int_diff + self.int_diff + 3, (self.int_z + k)*self.int_diff), 7)
            pygame.draw.line(self.game.display, (255, 255, 255), ((self.int_x + k) * self.int_diff,
                             self.int_z * self.int_diff), ((self.int_x + k) * self.int_diff, self.int_z * self.int_diff + self.int_diff), 7)

    # Inner function for graphical lines
    def drawlines(self, defaultgrid, completeFlag):
        for i in range(self.int_rangeNumber):
            for j in range(self.int_rangeNumber):
                if defaultgrid[i][j] != 0:
                    pygame.draw.rect(self.game.display, (255, 255, 0),
                                     (i * self.int_diff, j * self.int_diff, self.int_diff + 1, self.int_diff + 1))
                    teint_xt1 = self.font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                    self.game.display.blit(
                        teint_xt1, (i * self.int_diff + 15, j * self.int_diff + 15))
        for l in range(self.int_lineNumber):
            if l % self.int_base == 0:
                thick = 7
            else:
                thick = 1
            # Drawing of lines
            # Line(surface, colour, starting point, ending point, thickness)
            # Surface refers to the display that is to be drawn on
            # colour is RGB, each to a maint_ximum of 255
            # starting point is (int_x,y) whr int_x is horizontal aint_xis, y is vertical aint_xis
            # ending point is the same as starting point (int_x,y)
            pygame.draw.line(self.game.display, (0, 0, 0), (0, l * self.int_diff),
                             (self.int_sizeOfGame, l * self.int_diff), thick)
            pygame.draw.line(self.game.display, (0, 0, 0), (l * self.int_diff, 0),
                             (l * self.int_diff, self.int_sizeOfGame), thick)

        self.game.draw_text("Press S to solve.", 20, self.game.DISPLAY_W/2-275, self.game.DISPLAY_H/2+305, self.game.BLACK)
        self.game.draw_text("Press ENTER to return to menu.", 20, self.game.DISPLAY_W/2-200, self.game.DISPLAY_H/2+330, self.game.BLACK)
        if completeFlag == True:
            self.game.draw_text("Game solved", 20, self.game.DISPLAY_W/2 + 150, self.game.DISPLAY_H/2+305, self.game.BLACK)
            self.game.draw_text("Total Moves: "+str(self.display_counter), 20, self.game.DISPLAY_W/2 + 150, self.game.DISPLAY_H/2+330, self.game.BLACK)
            
            if self.singlerunFlag == False:
                # Read and update total games played
                with open('totalgamesplayed.txt', 'r') as file:
                    data = file.read().rstrip()
                data = str(int(data)+1) 
                with open('totalgamesplayed.txt', 'w') as f:
                    f.write(data)

                # Read and update total moves played
                with open('totalmoves.txt', 'r') as file:
                    data = file.read().rstrip()
                data = str(int(data)+self.display_counter) 
                with open('totalmoves.txt', 'w') as f:
                    f.write(data)

                if self.int_difficultyLevel == 2:
                    txt_filepath = 'totaleasy.txt'
                elif self.int_difficultyLevel == 3:
                    txt_filepath = 'totalmedium.txt'
                elif self.int_difficultyLevel == 4:
                    txt_filepath = 'totalhard.txt'
                elif self.int_difficultyLevel == 5:
                    txt_filepath = 'totalexpert.txt'

                # Read and update total difficulty played
                with open(txt_filepath, 'r') as file:
                    data = file.read().rstrip()
                data = str(int(data)+1) 
                with open(txt_filepath, 'w') as f:
                    f.write(data)

                self.singlerunFlag = True

            str_countingMinutes = str((self.int_counter//60) % 60).split(".")
            str_countingSeconds = str(self.int_counter % 60).split(".")
            str_countingHours = str(self.int_counter//(60*60) % 24).split(".")
            text = "%s:%s:%s" % (str_countingHours[0].zfill(2), str_countingMinutes[0].zfill(2), str_countingSeconds[0].zfill(2))
            self.game.draw_text("Time Taken: "+text, 20, self.game.DISPLAY_W/2 + 150, self.game.DISPLAY_H/2+355, self.game.BLACK)

    def fillvalue(self, int_value):
        text1 = self.font.render(str(int_value), 1, (0, 0, 0))
        self.game.display.blit(
            text1, (self.int_x * self.int_diff + 15, self.int_z * self.int_diff + 15))


    def raiseerror(self):
        text1 = self.font.render("wrong!", 1, (0, 0, 0))
        self.game.display.blit(text1, (20, 570))


    def raiseerror1(self):
        text1 = self.font.render(
            "wrong ! enter a valid key for the game", 1, (0, 0, 0))
        self.game.display.blit(text1, (20, 570))


    def validvalue(self, m, k, l, int_value):
        for it in range(self.int_rangeNumber):
            if m[k][it] == int_value:
                return False
            if m[it][l] == int_value:
                return False
        it = k//self.int_base
        jt = l//self.int_base
        for k in range(it * self.int_base, it * self.int_base + self.int_base):
            for l in range(jt * self.int_base, jt * self.int_base + self.int_base):
                if m[k][l] == int_value:
                    return False
        return True

        # inner function
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
                ##
                pygame.draw.rect(self.game.display, ((0, 182, 0)),
                                 pygame.Rect(450, 700, 100, 50))
                pygame.draw.rect(self.game.display, ((0, 182, 0)),
                                 pygame.Rect(50, 700, 350, 50))
                pygame.time.set_timer(pygame.K_RETURN, 1000)
                #global int_counter
                self.int_counter += 1/10

                #global display_counter
                self.display_counter += 1
                str_display_counter = "No. of Moves: " + \
                    str(self.display_counter).zfill(2)
                str_countingMinutes = str((self.int_counter//60) % 60).split(".")
                str_countingSeconds = str(self.int_counter % 60).split(".")
                str_countingHours = str(
                    self.int_counter//(60*60) % 24).split(".")
                text = "%s:%s:%s" % (
                    str_countingHours[0].zfill(2), str_countingMinutes[0].zfill(2), str_countingSeconds[0].zfill(2))
                self.game.display.blit(self.font.render(
                    text, True, (0, 0, 0)), (450, 700))
                self.game.display.blit(self.font.render(
                    str_display_counter, True, (0, 0, 0)), (50, 700))
                self.clock.tick(10)
                ##
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        int_flag = False
                ##
                self.highlightboint_x()
                pygame.display.update()
                pygame.time.delay(20)
                if self.solvegame(defaultgrid, i, j) == 1:
                    return True
                else:
                    defaultgrid[i][j] = 0

                self.drawlines(defaultgrid, False)
                self.highlightboint_x()
                pygame.display.update()
                pygame.time.delay(50)
        return False

    def gameresult(self):
        self.game.draw_text("Game solved", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2+305, self.game.BLACK)

    def resetflags(self):
        self.int_flag = True
        self.int_flag1 = 0
        self.int_flag2 = 0
        self.rs = 0
        self.error = 0
