# config.py
# World settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Creature settings
INITIAL_POPULATION = 50
CREATURE_SIZE = 8
CREATURE_MAX_SPEED = 3
CREATURE_VISION_RANGE = 100
CREATURE_STARTING_ENERGY = 100
CREATURE_ENERGY_DECAY = 0.1

# Food settings
FOOD_COUNT = 80
POISON_COUNT = 30
FOOD_SIZE = 5
FOOD_ENERGY = 30
POISON_DAMAGE = -50

# Neural network settings
INPUT_NEURONS = 8  # Distance to nearest food/poison (x4), own velocity (x2), energy, bias
HIDDEN_NEURONS = 8
OUTPUT_NEURONS = 2  # Steering force (x, y)

# Evolution settings
MUTATION_RATE = 0.1
MUTATION_STRENGTH = 0.3