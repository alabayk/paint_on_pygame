import pygame
from tkinter.filedialog import askopenfilename


def paint():
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode([width, height])
    screen.fill(pygame.Color('white'))

    running = True
    flag_ris = True
    flag_lastika = False
    nazhat = False
    rad = 4
    filename = ''
    zvet = pygame.Color('RED')
    zvet_lastika = pygame.Color('white')
    previous = pygame.Color('white')
    fon = False
    clean = True
    openfile = True
    prev = False

    def baza():
        brush = pygame.image.load('./data/paint-brush.png')
        eraser = pygame.image.load('./data/eraser.png')
        clear = pygame.image.load('./data/clear.png')
        zalivka = pygame.image.load('./data/zalivka.png')
        papka = pygame.image.load('./data/papka.png')
        if flag_lastika:
            pygame.draw.rect(screen, pygame.Color('gray'), [10, 10, 30, 30], )
            screen.blit(eraser, (10, 10))
            pygame.display.update()
        elif flag_ris:
            pygame.draw.rect(screen, pygame.Color('gray'), [10, 10, 30, 30], )
            screen.blit(brush, (10, 10))
            pygame.display.update()
        if fon:
            pygame.draw.rect(screen, pygame.Color('blue'), [125, 5, 40, 40], )
            pygame.draw.rect(screen, pygame.Color('gray'), [130, 10, 30, 30], )
            screen.blit(zalivka, (130, 10))
            pygame.display.update()
        else:
            pygame.draw.rect(screen, pygame.Color('gray'), [125, 5, 40, 40], )
            pygame.draw.rect(screen, pygame.Color('gray'), [130, 10, 30, 30], )
            screen.blit(brush, (130, 10))
            pygame.display.update()
        pygame.draw.rect(screen, pygame.Color('gray'), [165, 0, 635, 50], )
        pygame.draw.rect(screen, pygame.Color('gray'), [0, 0, 125, 10], )
        pygame.draw.rect(screen, pygame.Color('gray'), [0, 0, 165, 5], )
        pygame.draw.rect(screen, pygame.Color('gray'), [0, 40, 125, 10], )
        pygame.draw.rect(screen, pygame.Color('gray'), [0, 45, 165, 5], )
        pygame.draw.rect(screen, pygame.Color('gray'), [0, 0, 10, 50], )
        pygame.draw.rect(screen, pygame.Color('gray'), [40, 0, 10, 50], )
        pygame.draw.rect(screen, pygame.Color('gray'), [80, 0, 10, 50], )
        pygame.draw.rect(screen, pygame.Color('gray'), [120, 0, 5, 50], )
        pygame.draw.rect(screen, pygame.Color('white'), [540, 10, 30, 30], )
        pygame.draw.rect(screen, pygame.Color('black'), [570, 10, 30, 30], )
        pygame.draw.rect(screen, pygame.Color('red'), [600, 10, 30, 30], )
        pygame.draw.rect(screen, pygame.Color('orange'), [630, 10, 30, 30], )
        pygame.draw.rect(screen, pygame.Color('yellow'), [660, 10, 30, 30], )
        pygame.draw.rect(screen, pygame.Color('green'), [690, 10, 30, 30], )
        pygame.draw.rect(screen, pygame.Color('blue'), [720, 10, 30, 30], )
        pygame.draw.rect(screen, pygame.Color('purple'), [750, 10, 30, 30], )
        if clean:
            pygame.draw.rect(screen, pygame.Color('gray'), [50, 10, 30, 30], )
            screen.blit(clear, (50, 10))
            pygame.display.update()
        if openfile:
            pygame.draw.rect(screen, pygame.Color('gray'), [90, 10, 30, 30], )
            screen.blit(papka, (90, 10))
            pygame.display.update()
    while running:
        # Отрисовка интерфейса
        baza()

        for event in pygame.event.get():
            # Выход из программы
            if event.type == pygame.QUIT:
                running = False

            # Проверка на нажатие
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] >= 50:
                nazhat = True

            # Смена режима ластик/кисть
            if event.type == pygame.MOUSEBUTTONDOWN and 10 <= event.pos[0] <= 39 \
                    and 10 <= event.pos[1] <= 39 and flag_ris:
                flag_ris = False
                flag_lastika = True

            elif event.type == pygame.MOUSEBUTTONDOWN and 10 <= event.pos[0] <= 39 \
                    and 10 <= event.pos[1] <= 39 and flag_lastika:
                flag_ris = True
                flag_lastika = False

            # Смена режима цвет кисти/цвет фона
            if event.type == pygame.MOUSEBUTTONDOWN and 130 <= event.pos[0] <= 159 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                fon = True
            elif event.type == pygame.MOUSEBUTTONDOWN and 130 <= event.pos[0] <= 159 \
                    and 10 <= event.pos[1] <= 39 and fon:
                fon = False

            # Открытие файла
            if event.type == pygame.MOUSEBUTTONDOWN and 90 <= event.pos[0] <= 119 and 10 <= event.pos[1] <= 39:
                previous = zvet
                zvet = zvet_lastika
                prev = True
                filename = askopenfilename()
                print(filename)

            # Выбор цвета в палитре
            if event.type == pygame.MOUSEBUTTONDOWN and 540 <= event.pos[0] <= 569 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('white')
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 570 <= event.pos[0] <= 599 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('black')
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 600 <= event.pos[0] <= 629 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('red')
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 630 <= event.pos[0] <= 659 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('orange')
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 660 <= event.pos[0] <= 689 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('yellow')
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 690 <= event.pos[0] <= 719 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('green')
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 720 <= event.pos[0] <= 749 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('blue')
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 750 <= event.pos[0] <= 779 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('purple')
                pygame.display.update()

            # Очистить экран
            if event.type == pygame.MOUSEBUTTONDOWN and 50 <= event.pos[0] <= 79 \
                    and 10 <= event.pos[1] <= 39:
                screen.fill(zvet_lastika)
                baza()
                pygame.display.flip()

            # Задний фон
            if event.type == pygame.MOUSEBUTTONDOWN and 540 <= event.pos[0] <= 569 and 10 <= event.pos[1] <= 39 and fon:
                screen.fill(pygame.Color('white'))
                baza()
                zvet_lastika = pygame.Color('white')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 570 <= event.pos[0] <= 599 and 10 <= event.pos[1] <= 39 and fon:
                screen.fill(pygame.Color('black'))
                baza()
                zvet_lastika = pygame.Color('black')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 600 <= event.pos[0] <= 629 and 10 <= event.pos[1] <= 39 and fon:
                screen.fill(pygame.Color('red'))
                baza()
                zvet_lastika = pygame.Color('red')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 630 <= event.pos[0] <= 659 and 10 <= event.pos[1] <= 39 and fon:
                screen.fill(pygame.Color('orange'))
                baza()
                zvet_lastika = pygame.Color('orange')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 660 <= event.pos[0] <= 689 and 10 <= event.pos[1] <= 39 and fon:
                screen.fill(pygame.Color('yellow'))
                baza()
                zvet_lastika = pygame.Color('yellow')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 690 <= event.pos[0] <= 719 and 10 <= event.pos[1] <= 39 and fon:
                screen.fill(pygame.Color('green'))
                baza()
                zvet_lastika = pygame.Color('green')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 720 <= event.pos[0] <= 749 and 10 <= event.pos[1] <= 39 and fon:
                screen.fill(pygame.Color('blue'))
                baza()
                zvet_lastika = pygame.Color('blue')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 750 <= event.pos[0] <= 779 and 10 <= event.pos[1] <= 39 and fon:
                screen.fill(pygame.Color('purple'))
                baza()
                zvet_lastika = pygame.Color('purple')
                fon = False
                pygame.display.flip()
            # Проверка на отжатие мыши
            if event.type == pygame.MOUSEBUTTONUP:
                nazhat = False

        # Рисование кистью
        if flag_ris and nazhat:
            pygame.draw.circle(screen, zvet, pygame.mouse.get_pos(), rad)
            pygame.display.update()

        # Стирание ластиком
        elif flag_lastika and nazhat:
            pygame.draw.circle(screen, zvet_lastika, pygame.mouse.get_pos(), rad)
            pygame.display.update()

        # Отсутствие лишней прорисовки
        if prev:
            zvet = previous
            prev = False


paint()
