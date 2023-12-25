import pygame
from tkinter.filedialog import askopenfilename
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
running = True
flag_ris = True
flag_lastika = False
nazhat = False
rad = 4
filename = ''
zvet = pygame.Color('RED')
start = True

def baza():
    screen.fill(pygame.Color('black'))
    if flag_ris:
        pygame.draw.rect(screen, pygame.Color('Blue'), [0, 0, 30, 30], )
    elif flag_lastika:
        pygame.draw.rect(screen, pygame.Color('Green'), [0, 0, 30, 30], )
    pygame.draw.rect(screen, pygame.Color('white'), [750, 550, 50, 50], )
    pygame.draw.rect(screen, pygame.Color('gray'), [590, 0, 200, 40], )
    pygame.draw.rect(screen, pygame.Color('red'), [600, 0, 30, 30], )
    pygame.draw.rect(screen, pygame.Color('orange'), [630, 0, 30, 30], )
    pygame.draw.rect(screen, pygame.Color('yellow'), [660, 0, 30, 30], )
    pygame.draw.rect(screen, pygame.Color('green'), [690, 0, 30, 30], )
    pygame.draw.rect(screen, pygame.Color('blue'), [720, 0, 30, 30], )
    pygame.draw.rect(screen, pygame.Color('purple'), [750, 0, 30, 30], )
    pygame.draw.rect(screen, pygame.Color('brown'), [0, 30, 30, 30], )
while running:
    if start:
        baza()
        start = False

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
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= 750 and event.pos[1] >= 550:
            filename = askopenfilename()

        if event.type == pygame.MOUSEBUTTONDOWN and 600 <= event.pos[0] <= 629 and event.pos[1] <= 30:
            zvet = pygame.Color('red')
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and 630 <= event.pos[0] <= 659 and event.pos[1] <= 30:
            zvet = pygame.Color('orange')
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and 660 <= event.pos[0] <= 689 and event.pos[1] <= 30:
            zvet = pygame.Color('yellow')
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and 690 <= event.pos[0] <= 719 and event.pos[1] <= 30:
            zvet = pygame.Color('green')
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and 720 <= event.pos[0] <= 749 and event.pos[1] <= 30:
            zvet = pygame.Color('blue')
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and 750 <= event.pos[0] <= 779 and event.pos[1] <= 30:
            zvet = pygame.Color('purple')
            pygame.display.flip()
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] <= 30 and 30 <= event.pos[1] <= 59:
            baza()
            pygame.display.flip()
            start = True
        if event.type == pygame.MOUSEBUTTONUP:
            nazhat = False

    if flag_ris and nazhat:
        pygame.draw.circle(screen, zvet, pygame.mouse.get_pos(), rad)
        pygame.display.update()
    elif flag_lastika and nazhat:
        pygame.draw.circle(screen, pygame.Color('black'), pygame.mouse.get_pos(), rad)
        pygame.display.update()
