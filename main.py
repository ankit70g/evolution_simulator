# main.py
import pygame
import sys
from world import World
from config import *


def draw_neural_network(screen, creature, x, y, width, height):
    """Visualize a creature's neural network"""
    if not creature:
        return

    # Layer positions
    input_x = x + 20
    hidden_x = x + width // 2
    output_x = x + width - 20

    layer_heights = {
        'input': INPUT_NEURONS,
        'hidden': HIDDEN_NEURONS,
        'output': OUTPUT_NEURONS
    }

    def get_neuron_y(layer_name, index):
        count = layer_heights[layer_name]
        spacing = height / (count + 1)
        return y + spacing * (index + 1)

    # Draw connections (weights)
    brain = creature.brain

    # Input to hidden
    for i in range(INPUT_NEURONS):
        for h in range(HIDDEN_NEURONS):
            weight = brain.weights_ih[h][i]
            # Clamp and normalize weight
            weight = max(-1, min(1, weight))  # Clamp to [-1, 1]
            color_intensity = int(abs(weight) * 128) + 50  # Scale to [50, 178]
            # Ensure valid range
            color_intensity = max(0, min(255, color_intensity))

            if weight < 0:
                color = (color_intensity, 0, 0)  # Red for negative
            else:
                color = (0, color_intensity, 0)  # Green for positive

            pygame.draw.line(screen, color,
                             (input_x, int(get_neuron_y('input', i))),
                             (hidden_x, int(get_neuron_y('hidden', h))), 1)

    # Hidden to output
    for h in range(HIDDEN_NEURONS):
        for o in range(OUTPUT_NEURONS):
            weight = brain.weights_ho[o][h]
            # Clamp and normalize weight
            weight = max(-1, min(1, weight))
            color_intensity = int(abs(weight) * 128) + 50
            color_intensity = max(0, min(255, color_intensity))

            if weight < 0:
                color = (color_intensity, 0, 0)
            else:
                color = (0, color_intensity, 0)

            pygame.draw.line(screen, color,
                             (hidden_x, int(get_neuron_y('hidden', h))),
                             (output_x, int(get_neuron_y('output', o))), 1)

    # Draw neurons
    for i in range(INPUT_NEURONS):
        pygame.draw.circle(screen, (100, 100, 255),
                           (input_x, int(get_neuron_y('input', i))), 5)

    for h in range(HIDDEN_NEURONS):
        pygame.draw.circle(screen, (255, 255, 100),
                           (hidden_x, int(get_neuron_y('hidden', h))), 5)

    for o in range(OUTPUT_NEURONS):
        pygame.draw.circle(screen, (255, 100, 100),
                           (output_x, int(get_neuron_y('output', o))), 5)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(
        "Evolution Simulator - Neural Network Creatures")
    clock = pygame.time.Clock()

    world = World()
    font = pygame.font.Font(None, 24)
    small_font = pygame.font.Font(None, 18)

    paused = False
    show_vision = False
    selected_creature = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_v:
                    show_vision = not show_vision
                elif event.key == pygame.K_r:
                    world.reproduce()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Select nearest creature
                mx, my = pygame.mouse.get_pos()
                min_dist = float('inf')
                for creature in world.creatures:
                    dist = ((creature.x - mx)**2 + (creature.y - my)**2)**0.5
                    if dist < min_dist:
                        min_dist = dist
                        selected_creature = creature

        if not paused:
            world.update()

        # Drawing
        screen.fill((20, 20, 30))

        # Draw food and poison
        for food in world.foods:
            food.draw(screen)
        for poison in world.poisons:
            poison.draw(screen)

        # Draw creatures
        for creature in world.creatures:
            if show_vision:
                pygame.draw.circle(screen, (50, 50, 50), (int(creature.x), int(creature.y)),
                                   int(creature.vision_range), 1)
            creature.draw(screen)

        # Highlight selected creature
        if selected_creature and selected_creature.is_alive():
            pygame.draw.circle(screen, (255, 255, 0), (int(selected_creature.x), int(selected_creature.y)),
                               selected_creature.size + 3, 2)

        # Draw stats
        stats = world.get_stats()
        y_offset = 10
        texts = [
            f"Generation: {stats['generation']}",
            f"Population: {stats['population']}",
            f"Best Fitness: {stats['best_fitness']:.1f}",
            f"Avg Fitness: {stats['avg_fitness']:.1f}",
            f"Avg Age: {stats['avg_age']:.1f}",
            "",
            "Controls:",
            "SPACE: Pause/Resume",
            "V: Toggle Vision",
            "R: Force Reproduction",
            "Click: Select Creature"
        ]

        for text in texts:
            surface = small_font.render(text, True, (255, 255, 255))
            screen.blit(surface, (10, y_offset))
            y_offset += 20

        # Draw neural network of selected creature
        if selected_creature and selected_creature.is_alive():
            nn_panel_x = SCREEN_WIDTH - 250
            nn_panel_y = 10
            nn_panel_width = 240
            nn_panel_height = 300

            pygame.draw.rect(screen, (40, 40, 50), (nn_panel_x,
                             nn_panel_y, nn_panel_width, nn_panel_height))
            pygame.draw.rect(screen, (100, 100, 100), (nn_panel_x,
                             nn_panel_y, nn_panel_width, nn_panel_height), 2)

            title = small_font.render(
                "Selected Creature Brain", True, (255, 255, 255))
            screen.blit(title, (nn_panel_x + 10, nn_panel_y + 5))

            draw_neural_network(screen, selected_creature, nn_panel_x,
                                nn_panel_y + 25, nn_panel_width, nn_panel_height - 30)

        if paused:
            pause_text = font.render("PAUSED", True, (255, 255, 0))
            screen.blit(pause_text, (SCREEN_WIDTH // 2 - 50, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
