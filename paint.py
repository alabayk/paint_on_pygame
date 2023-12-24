import pygame
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
running = True
flag_ris = True
flag_lastika = False
nazhat = False
rad = 4

while running:
    if flag_ris:
        pygame.draw.rect(screen, pygame.Color('Blue'), [0, 0, 30, 30], )
    elif flag_lastika:
        pygame.draw.rect(screen, pygame.Color('Green'), [0, 0, 30, 30], )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 30 and event.pos[1] > 30:
            nazhat = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] <= 30 and event.pos[1] <= 30 and flag_ris:
            flag_ris = False
            flag_lastika = True
            pygame.draw.rect(screen, pygame.Color('Green'), [0, 0, 30, 30], )
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] <= 30 and event.pos[1] <= 30 and flag_lastika:
            flag_ris = True
            flag_lastika = False
            pygame.draw.rect(screen, pygame.Color('Blue'), [0, 0, 30, 30], )
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            nazhat = False

    if flag_ris and nazhat:
        pygame.draw.circle(screen, pygame.Color('RED'), pygame.mouse.get_pos(), rad)
        pygame.display.update()
    elif flag_lastika and nazhat:
        pygame.draw.circle(screen, pygame.Color('black'), pygame.mouse.get_pos(), rad)
        pygame.display.update()
