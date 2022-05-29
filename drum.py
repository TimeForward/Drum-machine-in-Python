import pygame
from pygame import mixer
pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0 , 0)
white = (255,255,255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('freesansbold.ttf',32)

fps = 60
timer = pygame.time.Clock()


def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0,0 ,200, HEIGHT -200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT -200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text=label_font.render('Hi-Hat', True, white)
    screen.blit(hi_hat_text,(30, 30))
run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    pygame.display.flip()
pygame.quit()

