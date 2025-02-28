import pygame
import random

# Initialize Pygame
pygame.init()

# Config
dis_width, dis_height = 800, 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Game params
snake_block = 20
snake_speed = 15
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Initial state
x1 = dis_width // 2
y1 = dis_height // 2
x1_change = 0
y1_change = 0
snake_list = []
length_of_snake = 1
foodx = round(random.randrange(0, dis_width - snake_block) /
              snake_block) * snake_block
foody = round(random.randrange(0, dis_height - snake_block) /
              snake_block) * snake_block

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change == 0:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change == 0:
                y1_change = snake_block
                x1_change = 0

    # Update position
    x1 += x1_change
    y1 += y1_change

    # Boundary check
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        break

    # Render
    dis.fill(white)
    pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

    # Update snake body
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
        del snake_list[0]

    # Self-collision check
    for segment in snake_list[:-1]:
        if segment == snake_head:
            running = False

    # Draw snake
    for segment in snake_list:
        pygame.draw.rect(
            dis, black, [segment[0], segment[1], snake_block, snake_block])

    # Score display
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {length_of_snake - 1}", True, black)
    dis.blit(score_text, [10, 10])

    pygame.display.update()

    # Food collision
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(
            0, dis_width - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, dis_height -
                      snake_block) / snake_block) * snake_block
        length_of_snake += 1

    clock.tick(snake_speed)

pygame.quit()
