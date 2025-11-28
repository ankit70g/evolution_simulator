# 🧬 Neural Network Evolution Simulator
![Demo Image](https://github.com/ankit70g/evolution_simulator/blob/16b24c58421be496d150e7f4633cbef0ee13251c/public/hero.png)

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

*Watch AI creatures evolve intelligence through natural selection in real-time!*

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [How It Works](#-how-it-works) • [Controls](#-controls) • [Configuration](#-configuration)

</div>

---

## 🎯 Overview

This project demonstrates **evolutionary machine learning** where creatures with neural network "brains" learn to survive through natural selection. No training data, no supervised learning—just pure evolution!

Watch as randomly initialized creatures gradually evolve the ability to:
- 🍎 Hunt for food efficiently
- ☠️ Avoid poisonous substances
- 🧠 Develop complex survival strategies
- 🎯 Optimize movement patterns

**Perfect for:** Portfolio projects, ML demonstrations, educational purposes, research visualization

---

## ✨ Features

### Core Mechanics
- **Neural Network Brains**: Each creature has a feedforward neural network controlling its behavior
- **Genetic Algorithm**: Top performers reproduce with mutations, driving evolution
- **Real-time Visualization**: Watch evolution happen at 60 FPS
- **Brain Visualization**: Click any creature to see its neural network in action
- **Fitness-Based Selection**: Smarter creatures survive and pass on their genes

### Technical Highlights
- Clean, modular architecture with separation of concerns
- Configurable hyperparameters for experimentation
- NumPy-accelerated neural network computations
- Efficient agent-based modeling with spatial awareness
- Vision system with configurable perception range

---

## 🎬 Demo

### Generation 1 vs Generation 50+

**Force Production:**
![Demo Image](https://github.com/ankit70g/evolution_simulator/blob/16b24c58421be496d150e7f4633cbef0ee13251c/public/force_production.png)
- Random, chaotic movement
- Creatures die quickly
- No apparent strategy

**Vision System:**
![Demo Image](https://github.com/ankit70g/evolution_simulator/blob/16b24c58421be496d150e7f4633cbef0ee13251c/public/vision.png)
- Real-time visualization (press 'V' to display vision circles)
- 100-pixel perception radius around each creature
- Nearest-neighbor detection for food and poison
- Normalized directional inputs (X/Y coordinates relative to creature)
- Multi-sensory integration (vision + velocity + energy state)

### Neural Network Visualization
![Demo Image](https://github.com/ankit70g/evolution_simulator/blob/16b24c58421be496d150e7f4633cbef0ee13251c/public/neural_network.png)
Click on any creature to see:
- **Input neurons** (blue): Sensory information
- **Hidden layer** (yellow): Processing layer
- **Output neurons** (red): Movement decisions
- **Connection weights**: Green (positive) / Red (negative)

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/evolution-simulator.git
cd evolution-simulator
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the simulator**
```bash
python main.py
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| `SPACE` | Pause/Resume simulation |
| `V` | Toggle vision range circles |
| `R` | Force new generation (skip current) |
| `Mouse Click` | Select creature to view its brain |
| `ESC` | Exit simulation |

---

## 🔬 How It Works

### 1. Neural Network Architecture

Each creature has a simple feedforward neural network:

```
Input Layer (8 neurons)
    ↓
Hidden Layer (8 neurons, Sigmoid activation)
    ↓
Output Layer (2 neurons, Tanh activation)
```

**Inputs:**
- Distance & direction to nearest food (x3)
- Distance & direction to nearest poison (x3)
- Current velocity (x2)

**Outputs:**
- Steering force X
- Steering force Y

### 2. Evolution Process

```
1. Initialize → Random neural network weights
2. Simulate → Creatures interact with environment
3. Evaluate → Fitness = energy + food_eaten + age
4. Select → Top 33% survivors chosen
5. Reproduce → Create offspring with mutations
6. Repeat → Next generation begins
```

### 3. Fitness Function

```python
fitness = energy + (food_eaten × 20) + (age × 0.1)
```

- **Energy**: Remaining life force
- **Food eaten**: Primary survival metric
- **Age**: Rewards longevity

### 4. Mutation Strategy

- **Rate**: 10% chance per weight
- **Strength**: ±30% random variation
- Allows exploration of solution space while preserving good traits

---

## ⚙️ Configuration

Edit `config.py` to customize the simulation:

### World Settings
```python
SCREEN_WIDTH = 1200        # Window width
SCREEN_HEIGHT = 800        # Window height
FPS = 60                   # Simulation speed
```

### Population Parameters
```python
INITIAL_POPULATION = 50    # Starting creatures
CREATURE_VISION_RANGE = 100  # How far they see
CREATURE_STARTING_ENERGY = 100  # Initial energy
```

### Evolution Settings
```python
MUTATION_RATE = 0.1        # 10% mutation chance
MUTATION_STRENGTH = 0.3    # Mutation magnitude
```

### Neural Network
```python
INPUT_NEURONS = 8          # Sensory inputs
HIDDEN_NEURONS = 8         # Processing layer
OUTPUT_NEURONS = 2         # Motor outputs
```

### Environment
```python
FOOD_COUNT = 80           # Green food items
POISON_COUNT = 30         # Red poison items
FOOD_ENERGY = 30          # Energy gained from food
POISON_DAMAGE = -50       # Damage from poison
```

---

## 📊 Understanding the Interface

### Top-Left Stats
- **Generation**: Current evolutionary iteration
- **Population**: Living creatures count
- **Best Fitness**: Highest performing creature
- **Avg Fitness**: Population mean fitness
- **Avg Age**: Mean creature lifespan

### Creature Indicators
- **Body color**: Genetic identity
- **White line**: Movement direction
- **Energy bar**: Green = healthy, Red = dying

### Neural Network Panel (right side)
- Appears when creature is selected
- Shows live weight values
- Visualizes decision-making process

---

## 📚 Educational Value

This project demonstrates:

### Machine Learning Concepts
- Neural networks and forward propagation
- Gradient-free optimization (genetic algorithms)
- Fitness landscapes and local optima
- Exploration vs exploitation trade-offs

### Software Engineering
- Clean code architecture
- Modular design patterns
- Configuration management
- Real-time systems programming

### Computational Biology
- Natural selection simulation
- Genotype-phenotype mapping
- Evolutionary pressure dynamics
- Emergent behavior in complex systems

---

## 🎓 Learning Outcomes

After working with this project, you'll understand:

✅ How neural networks make decisions  
✅ How evolution can optimize AI without training data  
✅ The relationship between genes (weights) and behavior  
✅ Trade-offs in evolutionary algorithm design  
✅ How to visualize complex AI systems  
✅ Agent-based modeling techniques  

---

## 🛠️ Project Structure

```
evolution_simulator/
│
├── main.py              # Main game loop and visualization
├── creature.py          # Creature class with neural network
├── neural_network.py    # Neural network implementation
├── food.py              # Food and poison entities
├── world.py             # World management and evolution
├── config.py            # All configurable parameters
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- [ ] Add save/load functionality for best brains
- [ ] Implement evolutionary history graphs
- [ ] Add more sensor types (smell, hearing)
- [ ] Create different environment types
- [ ] Add competitive/cooperative behaviors
- [ ] Implement sexual reproduction (crossover)

**To contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Requirements

```txt
pygame>=2.0.0
numpy>=1.20.0
```

---

## 📖 References & Inspiration

- **NEAT Algorithm**: Evolving neural network topologies
- **Genetic Algorithms**: Goldberg, David E. (1989)
- **Neural Networks**: Goodfellow, Bengio, Courville
- **Evolutionary Computation**: Kenneth A. De Jong

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- Pygame community for excellent documentation
- NumPy team for high-performance computing tools
- Evolutionary computation research community
- Nature, for the original algorithm

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ and 🧬

</div>
