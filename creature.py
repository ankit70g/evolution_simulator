# creature.py
import pygame
import numpy as np
import random
from config import *
from neural_network import NeuralNetwork

class Creature:
    def __init__(self, x=None, y=None, brain=None):
        self.x = x if x is not None else random.randint(0, SCREEN_WIDTH)
        self.y = y if y is not None else random.randint(0, SCREEN_HEIGHT)
        
        # Physics
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.ax = 0
        self.ay = 0
        
        # Stats
        self.energy = CREATURE_STARTING_ENERGY
        self.size = CREATURE_SIZE
        self.vision_range = CREATURE_VISION_RANGE
        self.age = 0
        self.food_eaten = 0
        
        # Neural network brain
        if brain is None:
            self.brain = NeuralNetwork()
        else:
            self.brain = brain.copy()
            self.brain.mutate()
        
        # Visual representation
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    
    def think(self, foods, poisons):
        """Use neural network to decide movement"""
        # Find nearest food
        nearest_food = self.find_nearest(foods)
        food_dx, food_dy, food_dist = nearest_food if nearest_food else (0, 0, self.vision_range)
        
        # Find nearest poison
        nearest_poison = self.find_nearest(poisons)
        poison_dx, poison_dy, poison_dist = nearest_poison if nearest_poison else (0, 0, self.vision_range)
        
        # Prepare inputs for neural network (normalize to 0-1 range)
        inputs = np.array([
            food_dx / self.vision_range,      # Food direction x
            food_dy / self.vision_range,      # Food direction y
            1 - (food_dist / self.vision_range),  # Food proximity
            poison_dx / self.vision_range,    # Poison direction x
            poison_dy / self.vision_range,    # Poison direction y
            1 - (poison_dist / self.vision_range),  # Poison proximity
            self.vx / CREATURE_MAX_SPEED,     # Current velocity x
            self.vy / CREATURE_MAX_SPEED,     # Current velocity y
        ])
        
        # Get output from neural network
        output = self.brain.predict(inputs)
        
        # Apply steering force
        self.ax = output[0] * 0.5
        self.ay = output[1] * 0.5
    
    def find_nearest(self, targets):
        """Find nearest target within vision range"""
        nearest = None
        min_dist = self.vision_range
        
        for target in targets:
            dx = target.x - self.x
            dy = target.y - self.y
            dist = np.sqrt(dx**2 + dy**2)
            
            if dist < min_dist:
                min_dist = dist
                nearest = (dx / (dist + 0.001), dy / (dist + 0.001), dist)  # Normalized direction + distance
        
        return nearest
    
    def update(self):
        """Update physics and energy"""
        # Apply acceleration
        self.vx += self.ax
        self.vy += self.ay
        
        # Limit speed
        speed = np.sqrt(self.vx**2 + self.vy**2)
        if speed > CREATURE_MAX_SPEED:
            self.vx = (self.vx / speed) * CREATURE_MAX_SPEED
            self.vy = (self.vy / speed) * CREATURE_MAX_SPEED
        
        # Update position
        self.x += self.vx
        self.y += self.vy
        
        # Wrap around screen edges
        self.x = self.x % SCREEN_WIDTH
        self.y = self.y % SCREEN_HEIGHT
        
        # Energy consumption
        self.energy -= CREATURE_ENERGY_DECAY
        self.energy -= speed * 0.01  # More energy for faster movement
        
        self.age += 1
    
    def eat(self, target):
        """Consume food or poison"""
        dx = target.x - self.x
        dy = target.y - self.y
        dist = np.sqrt(dx**2 + dy**2)
        
        if dist < self.size + target.size:
            self.energy += target.energy
            if target.energy > 0:
                self.food_eaten += 1
            return True
        return False
    
    def is_alive(self):
        """Check if creature is still alive"""
        return self.energy > 0
    
    def draw(self, screen):
        """Draw creature"""
        # Body
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        
        # Direction indicator
        end_x = int(self.x + self.vx * 3)
        end_y = int(self.y + self.vy * 3)
        pygame.draw.line(screen, (255, 255, 255), (int(self.x), int(self.y)), (end_x, end_y), 2)
        
        # Energy bar
        bar_width = 20
        bar_height = 3
        energy_ratio = max(0, min(1, self.energy / CREATURE_STARTING_ENERGY))
        pygame.draw.rect(screen, (255, 0, 0), 
                        (self.x - bar_width/2, self.y - self.size - 5, bar_width, bar_height))
        pygame.draw.rect(screen, (0, 255, 0), 
                        (self.x - bar_width/2, self.y - self.size - 5, bar_width * energy_ratio, bar_height))