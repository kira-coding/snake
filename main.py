import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CS-snake")
clock = pygame.time.Clock()

snake_block = 20
snake_speed = 10
white = (255, 255, 255)
brown = (100, 0, 0)
red = (255, 0, 0)

# Initial state
x1 = WIDTH // 2
y1 = HEIGHT // 2
x1_change = 0
y1_change = 0
snake_parts = []
length_of_snake = 1
foodx = round(random.randrange(0, WIDTH - snake_block) /
              snake_block) * snake_block
foody = round(random.randrange(0, HEIGHT - snake_block) /
              snake_block) * snake_block

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


    x1 += x1_change
    y1 += y1_change






    # Update snake body
    snake_head = [x1, y1]
    snake_parts.append(snake_head)
    if len(snake_parts) > length_of_snake:
        del snake_parts[0]

    #collision boundary
    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
        break
    for segment in snake_parts[:-1]:
        if segment == snake_head:
            running = False

    #snake draw call
    for segment in snake_parts:
        pygame.draw.rect(
            window, brown, [segment[0], segment[1], snake_block, snake_block])

    #score
    font = pygame.font.SysFont("sans-serif", 35)
    score_text = font.render(f"Score: {length_of_snake - 1}", True, brown)
    window.blit(score_text, [10, 10])

    pygame.display.update()

    #food
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(
            0, WIDTH - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, HEIGHT -
                      snake_block) / snake_block) * snake_block
        length_of_snake += 1

    clock.tick(snake_speed)

pygame.quit()
