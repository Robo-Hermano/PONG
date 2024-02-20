#get our imports
import pygame
import random
#initialise table 
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pong")
#players, scores and initialising ball as well as rectangles
play1 = pygame.Rect((5,200,10,150))
play2 = pygame.Rect((775,200,10,150))
score1 = 0
score2 = 0
bong = pygame.Rect((385, 275, 30, 30))
xsped = random.randint(4,8)
ysped = random.randint(4,8)
glock = pygame.time.Clock()
run = True
while run:
    #making game run at 60fps
    glock.tick(60)
    screen.fill((132,132,132))
    #monitoring ball speed
    bong.x += xsped
    bong.y += ysped
    #ball movement and bouncing from walls and rectangles
    if bong.top <= 0 or bong.bottom >= 600:
        ysped *= -1
        if bong.top <= 0:
            bong.top = 0
        else:
            bong.bottom = 600
    if bong.left <=0 or bong.right>= 800:
        xsped *= -1
        if bong.left <=0:
            score2 += 1
            bong.center = (385,275)
        else:
            score1 += 1
            bong.center = (385,275)
    if bong.colliderect(play1) or bong.colliderect(play2):
        xsped *= -1
        ysped = random.randint(-8,8)
        if bong.colliderect(play1):
            bong.left = 11
        else:
            bong.right = 769
    #actually drawing the objects
    pygame.draw.rect(screen, (0, 255, 0), play1)
    pygame.draw.rect(screen, (255, 0, 0), play2)
    pygame.draw.ellipse(screen, (0, 0, 255), bong)
    pygame.draw.aaline(screen, (255,255,255), (400, 0), (400, 600))
    key = pygame.key.get_pressed()
    #player(s) movement
    if key[pygame.K_UP] == True and play2.top >= 0:
        play2.move_ip(0,-7)
    elif key[pygame.K_DOWN] == True and play2.bottom <= 600:
        play2.move_ip(0,7)
    if play1.top < bong.y:
        play1.top += 7
    if play1.bottom > bong.y:
        play1.bottom -= 7
    #displaying score
    font = pygame.font.Font(None, 74)
    text = font.render(str(score1),1, (0,0,0))
    screen.blit(text, (300, 10))
    text = font.render(str(score2),1, (0,0,0))
    screen.blit(text, (500, 10))
    for event in pygame.event.get():
        #making pygame quit
        if event.type == pygame.QUIT or score1 >= 10 or score2 >= 10:
            run = False
    pygame.display.update()
pygame.quit()
