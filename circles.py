import pygame
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
running = True
flag_ris = True
nazhat = False
coords = ()
rad = 4

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            nazhat = True
            coords = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            nazhat = False

    if flag_ris and nazhat:
        pygame.draw.circle(screen, pygame.Color('RED'), coords, rad)
        pygame.display.update()
