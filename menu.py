# Import pygame library
import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        self.difficulty = 'Easy'
    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y, self.game.WHITE)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.titlex, self.titley = self.mid_w, self.mid_h - 300
        self.mainmenux, self.mainmenuy = self.mid_w, self.mid_h + 110
        self.difficultyx, self.difficultyy = self.mid_w, self.mid_h + 145
        self.startx, self.starty = self.mid_w, self.mid_h + 175
        self.increasex, self.increasey = self.mid_w, self.mid_h + 195
        self.decreasex, self.decreasey = self.mid_w, self.mid_h + 215
        self.analysisx, self.analysisy = self.mid_w, self.mid_h + 235
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 255
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        splashmenu = pygame.image.load('./images/sudokulogo4.png')

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("The Self-Solving Sudoku", 55, self.titlex, self.titley, self.game.WHITE)
            self.game.load_image(splashmenu,(self.game.DISPLAY_W / 3, self.game.DISPLAY_H / 5))
            self.game.draw_text("Main Menu", 50, self.mainmenux, self.mainmenuy, self.game.WHITE)
            self.game.draw_text("Difficulty: " + self.difficulty, 25, self.difficultyx, self.difficultyy, self.game.WHITE)
            self.game.draw_text("Start Game", 20, self.startx, self.starty, self.game.WHITE)
            self.game.draw_text("Increase Difficulty", 20, self.increasex, self.increasey, self.game.WHITE)
            self.game.draw_text("Decrease Difficulty", 20, self.decreasex, self.decreasey, self.game.WHITE)
            self.game.draw_text("Analysis", 20, self.analysisx, self.analysisy, self.game.WHITE)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy, self.game.WHITE)
            self.draw_cursor()
            self.blit_screen()
            

    def move_cursor(self):
        # For all down keys, set state to next menu item
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.increasex + self.offset, self.increasey)
                self.state = 'Increase Difficulty'
            elif self.state == 'Increase Difficulty':
                self.cursor_rect.midtop = (self.decreasex + self.offset, self.decreasey)
                self.state = 'Decrease Difficulty'
            elif self.state == 'Decrease Difficulty':
                self.cursor_rect.midtop = (self.analysisx + self.offset, self.analysisy)
                self.state = 'Analysis'
            elif self.state == 'Analysis':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        # For all up keys, set state to one menu item before
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Increase Difficulty':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Decrease Difficulty':
                self.cursor_rect.midtop = (self.increasex + self.offset, self.increasey)
                self.state = 'Increase Difficulty'
            elif self.state == 'Analysis':
                self.cursor_rect.midtop = (self.decreasex + self.offset, self.decreasey)
                self.state = 'Decrease Difficulty'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.analysisx + self.offset, self.analysisy)
                self.state = 'Analysis'

            
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            # Start Button on press
            if self.state == 'Start':
                self.game.playing = True
            
            # Increase Difficult button on press
            elif self.state == 'Increase Difficulty':
                # Keeping max difficulty to 5
                if self.game.int_difficultyLevel == 5:
                    self.game.int_difficultyLevel = 5
                elif self.game.int_difficultyLevel != 5:
                    self.game.int_difficultyLevel = self.game.int_difficultyLevel + 1
                # If else to assign Difficulty Keyword based on level
                if self.game.int_difficultyLevel == 5:
                    self.difficulty = 'Expert'
                elif self.game.int_difficultyLevel == 4:
                    self.difficulty = 'Hard'
                elif self.game.int_difficultyLevel == 3:
                    self.difficulty = 'Medium'
                elif self.game.int_difficultyLevel == 2:
                    self.difficulty = 'Easy'    

            elif self.state == 'Decrease Difficulty':
                # Keeping min difficulty to 2
                if self.game.int_difficultyLevel == 2:
                    self.game.int_difficultyLevel = 2
                elif self.game.int_difficultyLevel != 2:
                    self.game.int_difficultyLevel = self.game.int_difficultyLevel - 1
                # If else to assign Difficulty Keyword based on level
                if self.game.int_difficultyLevel == 5:
                    self.difficulty = 'Expert'
                elif self.game.int_difficultyLevel == 4:
                    self.difficulty = 'Hard'
                elif self.game.int_difficultyLevel == 3:
                    self.difficulty = 'Medium'
                elif self.game.int_difficultyLevel == 2:
                    self.difficulty = 'Easy'  
            elif self.state == 'Analysis':
                self.game.curr_menu = self.game.analysis
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30, self.game.WHITE)
            self.game.draw_text("Volume", 15, self.volx, self.voly, self.game.WHITE)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy, self.game.WHITE)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class AnalysisMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        # Get total games played from txt
        with open('totalgamesplayed.txt', 'r') as file:
            data = file.read().rstrip()
        self.NumberofGamesSolved = int(data)

        # Get total moves played from txt
        with open('totalmoves.txt', 'r') as file:
            data = file.read().rstrip()
        self.NumberofTotalMoves = int(data)

        # Get total easy played from txt
        with open('totaleasy.txt', 'r') as file:
            data = file.read().rstrip()
        self.NumberofTotalEasy = int(data)

        # Get total medium played from txt
        with open('totalmedium.txt', 'r') as file:
            data = file.read().rstrip()
        self.NumberofTotalMedium = int(data)

        # Get total hard played from txt
        with open('totalhard.txt', 'r') as file:
            data = file.read().rstrip()
        self.NumberofTotalHard = int(data)

        # Get total hard played from txt
        with open('totalexpert.txt', 'r') as file:
            data = file.read().rstrip()
        self.NumberofTotalExpert = int(data)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            #Analysis Header
            self.game.draw_text("Game Analysis", 50, self.mid_w, self.mid_h - 300 , self.game.WHITE)
            #Easy
            self.game.draw_rect((self.mid_w-150),((self.mid_h+100)-(self.NumberofTotalEasy*100/2)),50,(self.NumberofTotalEasy*100/2), (100,150,200))
            self.game.draw_text("Easy", 20, (self.mid_w-125), (self.mid_h+125) ,(100,150,200))
            self.game.draw_text(str(self.NumberofTotalEasy), 20, (self.mid_w-125), (self.mid_h+145) ,(100,150,200))
            #Medium
            self.game.draw_rect((self.mid_w-50),((self.mid_h+100)-(self.NumberofTotalMedium*100/2)),50,(self.NumberofTotalMedium*100/2), (45,150,33))
            self.game.draw_text("Medium", 20, (self.mid_w-25), (self.mid_h+125) ,(45,150,33))
            self.game.draw_text(str(self.NumberofTotalMedium), 20, (self.mid_w-25), (self.mid_h+145) ,(45,150,33))
            #Hard
            self.game.draw_rect((self.mid_w+50),((self.mid_h+100)-(self.NumberofTotalHard*100/2)),50,(self.NumberofTotalHard*100/2), (222,33,122))
            self.game.draw_text("Hard", 20, (self.mid_w+75), (self.mid_h+125) ,(222,33,122))
            self.game.draw_text(str(self.NumberofTotalHard), 20, (self.mid_w+75), (self.mid_h+145) ,(222,33,122))
            #Expert
            self.game.draw_rect((self.mid_w+150),((self.mid_h+100)-(self.NumberofTotalExpert*100/2)),50,(self.NumberofTotalExpert*100/2), (100,150,22))
            self.game.draw_text("Expert", 20, (self.mid_w+175), (self.mid_h+125) ,(100,150,22))
            self.game.draw_text(str(self.NumberofTotalExpert), 20, (self.mid_w+175), (self.mid_h+145) ,(100,150,22))

            #Total Games
            self.game.draw_text("Total Games: "+str(self.NumberofGamesSolved), 20, self.mid_w, self.mid_h +250 , self.game.WHITE)
            #Total Moves
            self.game.draw_text("Total Moves: "+str(self.NumberofTotalMoves), 20, self.mid_w, self.mid_h +275 , self.game.WHITE)
            #Average Moves / Per
            self.game.draw_text("Average Moves Per Game: "+str(round(self.NumberofTotalMoves/self.NumberofGamesSolved,2)), 20, self.mid_w, self.mid_h +300 , self.game.WHITE)
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

