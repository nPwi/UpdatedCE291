# import library
from tkinter import Y
from random import sample
import pygame
from menu import *
from generatelevel import *

class Game():
    # Initialize
    def __init__(self):
        pygame.init()
        self.int_difficultyLevel = 2
        self.NumberofGamesSolved = 0
        self.TotalNumberofMoves = 0
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.S_KEY  = False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 750, 750
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W,self.DISPLAY_H),0,32)
        self.font_name = pygame.font.get_default_font()
        self.caption_name = pygame.display.set_caption('The Self Solving Sudoku')
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.analysis = AnalysisMenu(self)
        self.generatelevel = GenerateLevel(self)
        self.curr_menu = self.main_menu
        self.defaultgrid = self.generatelevel.defaultgrid()
        self.completeFlag = False

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
                self.defaultgrid = self.generatelevel.defaultgrid()
                self.completeFlag = False
            elif self.S_KEY:
                self.generatelevel.solvegame(self.defaultgrid,0,0)
                self.completeFlag = True
            self.display.fill(self.BLACK)
            self.display.fill(self.WHITE)
            if self.completeFlag == True:
                self.generatelevel.drawlines(self.defaultgrid, True)
            elif self.completeFlag == False:
                self.generatelevel.drawlines(self.defaultgrid, False)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
    
    # Function to check for possible inputs by user
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.generatelevel = GenerateLevel(self)
                    self.defaultgrid = self.generatelevel.defaultgrid()
                    self.UP_KEY = True
                if event.key == pygame.K_s:
                    self.S_KEY = True

    # Function to reset keys
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.S_KEY = False, False, False, False, False  

    def draw_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def load_image(self, sprite, position):
        self.display.blit(sprite, position)

    def draw_rect(self, w, x, y, z, color):
        pygame.draw.rect(self.display, color, pygame.Rect(w, x, y, z))



    