# world.py
import random
from creature import Creature
from food import Food, Poison
from config import *

class World:
    def __init__(self):
        self.creatures = [Creature() for _ in range(INITIAL_POPULATION)]
        self.foods = [Food() for _ in range(FOOD_COUNT)]
        self.poisons = [Poison() for _ in range(POISON_COUNT)]
        
        self.generation = 1
        self.best_fitness = 0
        self.avg_fitness = 0
    
    def update(self):
        """Update all entities"""
        # Creatures think and move
        for creature in self.creatures:
            creature.think(self.foods, self.poisons)
            creature.update()
            
            # Check food consumption
            for food in self.foods:
                if creature.eat(food):
                    food.respawn()
            
            # Check poison consumption
            for poison in self.poisons:
                if creature.eat(poison):
                    poison.respawn()
        
        # Remove dead creatures
        self.creatures = [c for c in self.creatures if c.is_alive()]
        
        # Reproduce if population is low
        if len(self.creatures) < INITIAL_POPULATION // 2:
            self.reproduce()
    
    def reproduce(self):
        """Create new generation through selection"""
        if len(self.creatures) == 0:
            # Restart with random population
            self.creatures = [Creature() for _ in range(INITIAL_POPULATION)]
            self.generation += 1
            return
        
        # Calculate fitness (energy + food eaten)
        for creature in self.creatures:
            creature.fitness = creature.energy + (creature.food_eaten * 20) + (creature.age * 0.1)
        
        # Sort by fitness
        self.creatures.sort(key=lambda c: c.fitness, reverse=True)
        
        # Stats
        self.best_fitness = self.creatures[0].fitness if self.creatures else 0
        self.avg_fitness = sum(c.fitness for c in self.creatures) / len(self.creatures)
        
        # Keep top performers
        survivors = self.creatures[:max(2, len(self.creatures) // 3)]
        
        # Create new generation
        new_creatures = []
        while len(new_creatures) < INITIAL_POPULATION:
            # Select parent based on fitness (roulette wheel selection)
            parent = random.choices(survivors, weights=[c.fitness for c in survivors])[0]
            child = Creature(brain=parent.brain)
            new_creatures.append(child)
        
        self.creatures = new_creatures
        self.generation += 1
    
    def get_stats(self):
        """Return current statistics"""
        return {
            'generation': self.generation,
            'population': len(self.creatures),
            'best_fitness': self.best_fitness,
            'avg_fitness': self.avg_fitness,
            'avg_age': sum(c.age for c in self.creatures) / len(self.creatures) if self.creatures else 0
        }