#
# Reflex Test on a 3x3 board
#

import pygame
import math
import game_mouse
import random
import datetime

BACKGROUND_COLOR        = (200, 200, 200)
BUTTON_OUTLINE_COLOR    = (  0,   0,   0)
BUTTON_FILL_COLOR       = (255, 51, 153)
BUG_COLOR       		= (86,195,86)

class GameBoard(game_mouse.Game):
    def __init__(self, width, height):
        game_mouse.Game.__init__(self, "Reflex tester", width, height, 10)
        
        self.board = [0,0,0,0,0,0,0,0,0]
        self.timeclock = 0
        self.timer = 0
        self.random_wait = random.randint(20,50)
        self.bug = False
        self.bugpos = random.randrange(9)
        self.spot = pygame.Rect(10,10,0,0)
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        pass
    
    def paint(self, surface):
        drawWindow(surface, self.width, self.height, self.board)
        if self.bug:
        	drawBug(surface, self.width, self.height, self.bugpos, self.board)
        return
        
def processClick(board, click_x, click_y, bug, bugpos, width, height,timer):
    pass

def drawBug(surface, width, height, square, board):
	pass
	
def drawTest(surface, spot):
	pass

def drawWindow(surface, width, height, board):
    clearBackground(surface, width, height)
    

def clearBackground(surface, width, height):
    pass

def main():
    game = GameBoard(600, 600)
    game.main_loop()
    
if __name__ == "__main__":
    main()















