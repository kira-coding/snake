import random
import pygame
pygame.init()

isRunning = True
clock = pygame.time.Clock()
fps=15

WIDTH,HEIGHT= 800,400
display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("snake Game")

snake_x =WIDTH//2
snake_y =HEIGHT//2
snake_body=[]
snake_length=1
Move_X=0
Move_Y=0
BLOCK=20
food_x= round(random.randrange(0,WIDTH-BLOCK)/BLOCK)*BLOCK
food_y= round(random.randrange(0,HEIGHT-BLOCK)/BLOCK)*BLOCK
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and Move_Y==0:
                Move_X=0
                Move_Y=BLOCK
            if event.key == pygame.K_UP and Move_Y==0:
                Move_X=0
                Move_Y=-BLOCK
            if event.key == pygame.K_LEFT and Move_X==0:
                Move_X=-BLOCK
                Move_Y=0
            if event.key == pygame.K_RIGHT and Move_X==0:
                Move_X=BLOCK
                Move_Y=0
    snake_x+=Move_X
    snake_y+=Move_Y
    snake_head=[snake_x,snake_y]
    snake_body.append(snake_head)
    if len(snake_body)>snake_length:
        print("deleted")
        del snake_body[0]
        display.fill("white")
    pygame.draw.rect(display,"blue",[food_x,food_y,BLOCK,BLOCK])
    for segment in snake_body[:-1]:
        if segment == snake_head:
            isRunning = False
            break
    if snake_x<=0 or snake_y<=0 or  snake_x >= WIDTH or snake_y>=HEIGHT:
        isRunning=False
    for segment in snake_body:
        pygame.draw.rect(display,"black",[segment[0],segment[1],BLOCK,BLOCK])
    
    if food_x == snake_x and food_y==snake_y:
        food_x= round(random.randrange(0,WIDTH-BLOCK)/BLOCK)*BLOCK
        food_y= round(random.randrange(0,HEIGHT-BLOCK)/BLOCK)*BLOCK
        snake_length+=1
    font = pygame.font.SysFont(None,50)
    score_text =font.render("Score: "+ str(snake_length),True,"brown")
    display.blit(score_text,[5,5])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()