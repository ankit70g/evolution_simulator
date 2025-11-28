# neural_network.py
import numpy as np
from config import *

class NeuralNetwork:
    def __init__(self, weights_ih=None, weights_ho=None):
        """
        Simple feedforward neural network with one hidden layer
        """
        if weights_ih is None:
            # Initialize with random weights
            self.weights_ih = np.random.randn(HIDDEN_NEURONS, INPUT_NEURONS) * 0.5
        else:
            self.weights_ih = weights_ih.copy()
            
        if weights_ho is None:
            self.weights_ho = np.random.randn(OUTPUT_NEURONS, HIDDEN_NEURONS) * 0.5
        else:
            self.weights_ho = weights_ho.copy()
    
    def sigmoid(self, x):
        """Activation function"""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def tanh(self, x):
        """Alternative activation for output layer"""
        return np.tanh(x)
    
    def predict(self, inputs):
        """Forward propagation"""
        # Input to hidden
        hidden = self.sigmoid(np.dot(self.weights_ih, inputs))
        
        # Hidden to output
        output = self.tanh(np.dot(self.weights_ho, hidden))
        
        return output
    
    def mutate(self):
        """Mutate weights for evolution"""
        if np.random.random() < MUTATION_RATE:
            # Mutate input-hidden weights
            mutation_mask = np.random.random(self.weights_ih.shape) < MUTATION_RATE
            self.weights_ih += mutation_mask * np.random.randn(*self.weights_ih.shape) * MUTATION_STRENGTH
        
        if np.random.random() < MUTATION_RATE:
            # Mutate hidden-output weights
            mutation_mask = np.random.random(self.weights_ho.shape) < MUTATION_RATE
            self.weights_ho += mutation_mask * np.random.randn(*self.weights_ho.shape) * MUTATION_STRENGTH
    
    def copy(self):
        """Create a copy of this network"""
        return NeuralNetwork(self.weights_ih, self.weights_ho)