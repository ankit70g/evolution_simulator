# food.py
import pygame
import random
from config import *

class Food:
    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(0, SCREEN_WIDTH)
        self.y = y if y is not None else random.randint(0, SCREEN_HEIGHT)
        self.size = FOOD_SIZE
        self.color = (0, 255, 0)  # Green
        self.energy = FOOD_ENERGY
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
    
    def respawn(self):
        """Respawn at random location"""
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)

class Poison:
    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(0, SCREEN_WIDTH)
        self.y = y if y is not None else random.randint(0, SCREEN_HEIGHT)
        self.size = FOOD_SIZE
        self.color = (255, 0, 0)  # Red
        self.energy = POISON_DAMAGE
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
    
    def respawn(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)