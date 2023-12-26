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
    flag_pryam = False
    flag = True
    nazhat = False
    rad = 4
    zvet = pygame.Color('black')
    zvet_pryam = pygame.Color('red')
    zvet_lastika = pygame.Color('white')
    previous = pygame.Color('white')
    fon = False
    clean = True
    openfile = True
    prev = False
    coords = ()
    history = []
    svezh = [[]]
    nach = True
    flag = False
    i_global = 0

    white = True
    black = False
    red = True
    orange = True
    yellow = True
    green = True
    blue = True
    purple = True

    def baza():
        f1 = pygame.font.Font(None, 24)
        if flag:
            back = pygame.image.load('./Безымянный.png')
            screen.blit(back, (0, 0))
        if not fon:
            text1 = f1.render('Выберите цвет кисти:', True, (180, 0, 0))
        else:
            text1 = f1.render('Выберите цвет фона:', True, (180, 0, 0))
        brush = pygame.image.load('./data/paint-brush.png')
        eraser = pygame.image.load('./data/eraser.png')
        clear = pygame.image.load('./data/clear.png')
        zalivka = pygame.image.load('./data/zalivka.png')
        papka = pygame.image.load('./data/papka.png')
        kvadrat = pygame.image.load('./data/kvadrat.png')
        if flag_lastika:
            pygame.draw.rect(screen, pygame.Color('gray'), [10, 10, 30, 30], )
            screen.blit(eraser, (10, 10))
            pygame.display.update()
        elif flag_ris:
            pygame.draw.rect(screen, pygame.Color('gray'), [10, 10, 30, 30], )
            screen.blit(brush, (10, 10))
            pygame.display.update()
        elif flag_pryam:
            pygame.draw.rect(screen, pygame.Color('gray'), [10, 10, 30, 30], )
            screen.blit(kvadrat, (10, 10))
            pygame.display.update()
        if fon:
            pygame.draw.rect(screen, pygame.Color('blue'), [125, 5, 40, 40], )
            pygame.draw.rect(screen, pygame.Color('gray'), [130, 10, 30, 30], )
            screen.blit(zalivka, (130, 10))
            pygame.display.update()
        else:
            pygame.draw.rect(screen, pygame.Color('gray'), [125, 5, 40, 40], )
            pygame.draw.rect(screen, pygame.Color('gray'), [130, 10, 30, 30], )
            screen.blit(zalivka, (130, 10))
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
        if white:
            pygame.draw.rect(screen, pygame.Color('gray'), [540, 10, 30, 30], 4)
        pygame.draw.rect(screen, pygame.Color('black'), [570, 10, 30, 30], )
        if black:
            pygame.draw.rect(screen, pygame.Color('gray'), [570, 10, 30, 30], 4)
        pygame.draw.rect(screen, pygame.Color('red'), [600, 10, 30, 30], )
        if red:
            pygame.draw.rect(screen, pygame.Color('gray'), [600, 10, 30, 30], 4)
        pygame.draw.rect(screen, pygame.Color('orange'), [630, 10, 30, 30], )
        if orange:
            pygame.draw.rect(screen, pygame.Color('gray'), [630, 10, 30, 30], 4)
        pygame.draw.rect(screen, pygame.Color('yellow'), [660, 10, 30, 30], )
        if yellow:
            pygame.draw.rect(screen, pygame.Color('gray'), [660, 10, 30, 30], 4)
        pygame.draw.rect(screen, pygame.Color('green'), [690, 10, 30, 30], )
        if green:
            pygame.draw.rect(screen, pygame.Color('gray'), [690, 10, 30, 30], 4)
        pygame.draw.rect(screen, pygame.Color('blue'), [720, 10, 30, 30], )
        if blue:
            pygame.draw.rect(screen, pygame.Color('gray'), [720, 10, 30, 30], 4)
        pygame.draw.rect(screen, pygame.Color('purple'), [750, 10, 30, 30], )
        if purple:
            pygame.draw.rect(screen, pygame.Color('gray'), [750, 10, 30, 30], 4)
        screen.blit(text1, (350, 17))
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
        if nach:
            baza()
        if flag:
            bg = pygame.image.load('./Безымянный.png')
            screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            # Выход из программы
            if event.type == pygame.QUIT:
                start()
                running = False

            # Проверка на нажатие
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] >= 50:
                nazhat = True
                coords = event.pos
                if flag_ris:
                    svezh[0].append(zvet)
                    svezh.append([])
                    i_global += 1

            # Смена режима ластик/кисть
            if event.type == pygame.MOUSEBUTTONDOWN and 10 <= event.pos[0] <= 39 and 10 <= event.pos[1] <= 39:
                if flag_ris:
                    flag_ris = False
                    flag_lastika = True
                    flag_pryam = False
                elif flag_lastika:
                    flag_ris = False
                    flag_lastika = False
                    flag_pryam = True
                elif flag_pryam:
                    flag_pryam = False
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
                if filename != '':
                    screen.fill(zvet_lastika)
                    foto = pygame.image.load(filename)
                    pygame.display.update()
                    razmer = foto.get_rect().size
                    for i in range(1, 100):
                        if razmer[0] / i <= 800 and razmer[1] / i <= 550:
                            foto = pygame.transform.scale(foto, (int(razmer[0] / i), int(razmer[1] / i)))
                            razmer = foto.get_rect().size
                            break
                    position = ((width + 1) // 2 - (razmer[0] + 1) // 2, (height + 1) // 2 - (razmer[1] + 1) // 2 + 25)
                    screen.blit(foto, position)

            # Выбор цвета в палитре
            if event.type == pygame.MOUSEBUTTONDOWN and 540 <= event.pos[0] <= 569 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('white')
                white = False
                black = True
                red = True
                orange = True
                yellow = True
                green = True
                blue = True
                purple = True
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 570 <= event.pos[0] <= 599 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('black')
                white = True
                black = False
                red = True
                orange = True
                yellow = True
                green = True
                blue = True
                purple = True
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 600 <= event.pos[0] <= 629 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('red')
                white = True
                black = True
                red = False
                orange = True
                yellow = True
                green = True
                blue = True
                purple = True
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 630 <= event.pos[0] <= 659 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('orange')
                white = True
                black = True
                red = True
                orange = False
                yellow = True
                green = True
                blue = True
                purple = True
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 660 <= event.pos[0] <= 689 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('yellow')
                white = True
                black = True
                red = True
                orange = True
                yellow = False
                green = True
                blue = True
                purple = True
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 690 <= event.pos[0] <= 719 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('green')
                white = True
                black = True
                red = True
                orange = True
                yellow = True
                green = False
                blue = True
                purple = True
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 720 <= event.pos[0] <= 749 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('blue')
                white = True
                black = True
                red = True
                orange = True
                yellow = True
                green = True
                blue = False
                purple = True
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 750 <= event.pos[0] <= 779 \
                    and 10 <= event.pos[1] <= 39 and not fon:
                zvet = pygame.Color('purple')
                white = True
                black = True
                red = True
                orange = True
                yellow = True
                green = True
                blue = True
                purple = False
                pygame.display.update()

            # Очистить экран
            if event.type == pygame.MOUSEBUTTONDOWN and 50 <= event.pos[0] <= 79 \
                    and 10 <= event.pos[1] <= 39:
                screen.fill(zvet_lastika)
                baza()
                history = []
                svezh = [[]]
                i_global = 0
                pygame.display.flip()

            # Задний фон
            if event.type == pygame.MOUSEBUTTONDOWN and 540 <= event.pos[0] <= 569\
                    and 10 <= event.pos[1] <= 39 and fon and zvet_lastika != pygame.Color('white'):
                screen.fill(pygame.Color('white'))
                baza()
                zvet_lastika = pygame.Color('white')
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 570 <= event.pos[0] <= 599\
                    and 10 <= event.pos[1] <= 39 and fon and zvet_lastika != pygame.Color('black'):
                screen.fill(pygame.Color('black'))
                baza()
                zvet_lastika = pygame.Color('black')
                black = True
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 600 <= event.pos[0] <= 629\
                    and 10 <= event.pos[1] <= 39 and fon and zvet_lastika != pygame.Color('red'):
                screen.fill(pygame.Color('red'))
                baza()
                zvet_lastika = pygame.Color('red')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 630 <= event.pos[0] <= 659\
                    and 10 <= event.pos[1] <= 39 and fon and zvet_lastika != pygame.Color('orange'):
                screen.fill(pygame.Color('orange'))
                baza()
                zvet_lastika = pygame.Color('orange')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 660 <= event.pos[0] <= 689\
                    and 10 <= event.pos[1] <= 39 and fon and zvet_lastika != pygame.Color('yellow'):
                screen.fill(pygame.Color('yellow'))
                baza()
                zvet_lastika = pygame.Color('yellow')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 690 <= event.pos[0] <= 719\
                    and 10 <= event.pos[1] <= 39 and fon and zvet_lastika != pygame.Color('green'):
                screen.fill(pygame.Color('green'))
                baza()
                zvet_lastika = pygame.Color('green')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 720 <= event.pos[0] <= 749\
                    and 10 <= event.pos[1] <= 39 and fon and zvet_lastika != pygame.Color('blue'):
                screen.fill(pygame.Color('blue'))
                baza()
                zvet_lastika = pygame.Color('blue')
                fon = False
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and 750 <= event.pos[0] <= 779\
                    and 10 <= event.pos[1] <= 39 and fon and zvet_lastika != pygame.Color('purple'):
                screen.fill(pygame.Color('purple'))
                baza()
                zvet_lastika = pygame.Color('purple')
                fon = False
                pygame.display.flip()

            # Проверка на отжатие мыши
            if event.type == pygame.MOUSEBUTTONUP:
                nazhat = False
                pygame.image.save(screen, 'Безымянный.png')
                if flag_pryam:
                    if event.pos[1] >= 50:
                        if coords[0] <= pygame.mouse.get_pos()[0] and coords[1] <= pygame.mouse.get_pos()[1]:
                            a, b = abs(coords[0]-pygame.mouse.get_pos()[0]), abs(coords[1]-pygame.mouse.get_pos()[1])
                            x, y = coords
                            history.append(((x, y), (a, b)))
                            # print(history)
                        elif coords[0] >= pygame.mouse.get_pos()[0] and coords[1] >= pygame.mouse.get_pos()[1]:
                            a, b = abs(coords[0]-pygame.mouse.get_pos()[0]), abs(coords[1]-pygame.mouse.get_pos()[1])
                            x, y = pygame.mouse.get_pos()
                            history.append(((x, y), (a, b)))
                            # print(history)
                        elif coords[0] <= pygame.mouse.get_pos()[0] and coords[1] >= pygame.mouse.get_pos()[1]:
                            a, b = abs(coords[0]-pygame.mouse.get_pos()[0]), abs(coords[1]-pygame.mouse.get_pos()[1])
                            x, y = coords[0], coords[1] - b
                            history.append(((x, y), (a, b)))
                            # print(history)
                        elif coords[0] >= pygame.mouse.get_pos()[0] and coords[1] <= pygame.mouse.get_pos()[1]:
                            a, b = abs(coords[0]-pygame.mouse.get_pos()[0]), abs(coords[1]-pygame.mouse.get_pos()[1])
                            x, y = coords[0] - a, coords[1]
                            history.append(((x, y), (a, b)))
                            # print(history)


        # Рисование кистью
        if flag_ris and nazhat:
            svezh[i_global].append(coords)
            pygame.draw.circle(screen, zvet, pygame.mouse.get_pos(), rad)
            pygame.draw.line(screen, zvet, coords, pygame.mouse.get_pos(), 3 * rad)
            coords = pygame.mouse.get_pos()
            pygame.display.update()

        # Стирание ластиком
        if flag_lastika and nazhat:
            pygame.draw.circle(screen, zvet_lastika, pygame.mouse.get_pos(), rad)
            pygame.draw.line(screen, zvet_lastika, coords, pygame.mouse.get_pos(), 3 * rad)
            coords = pygame.mouse.get_pos()
            pygame.display.update()

        # Рисование прямоугольника
        if flag_pryam and nazhat:
            pygame.display.flip()
            # 4 четверть
            if coords[0] <= pygame.mouse.get_pos()[0] and coords[1] <= pygame.mouse.get_pos()[1]:
                a, b = abs(coords[0] - pygame.mouse.get_pos()[0]), abs(coords[1] - pygame.mouse.get_pos()[1])
                x, y = coords
                # pygame.draw.rect(screen, zvet_lastika, [0, 50, width, height])
                bg = pygame.image.load('./Безымянный.png')
                screen.blit(bg, (0, 0))
                pygame.draw.rect(screen, zvet_pryam, [x, y,  a, b], 2)
                pygame.display.update()
            # 2 четверть
            elif coords[0] >= pygame.mouse.get_pos()[0] and coords[1] >= pygame.mouse.get_pos()[1]:
                a, b = abs(coords[0] - pygame.mouse.get_pos()[0]), abs(coords[1] - pygame.mouse.get_pos()[1])
                x, y = pygame.mouse.get_pos()
                # pygame.draw.rect(screen, zvet_lastika, [0, 50, width, height])
                bg = pygame.image.load('./Безымянный.png')
                screen.blit(bg, (0, 0))
                pygame.draw.rect(screen, zvet_pryam, [x, y, a, b], 2)
                pygame.display.update()
            # 1 четверть
            elif coords[0] <= pygame.mouse.get_pos()[0] and coords[1] >= pygame.mouse.get_pos()[1]:
                a, b = abs(coords[0] - pygame.mouse.get_pos()[0]), abs(coords[1] - pygame.mouse.get_pos()[1])
                x, y = coords[0], coords[1] - b
                # pygame.draw.rect(screen, zvet_lastika, [0, 50, width, height])
                bg = pygame.image.load('./Безымянный.png')
                screen.blit(bg, (0, 0))
                pygame.draw.rect(screen, zvet_pryam, [x, y, a, b], 2)
                pygame.display.update()
            # 3 четверть
            elif coords[0] >= pygame.mouse.get_pos()[0] and coords[1] <= pygame.mouse.get_pos()[1]:
                a, b = abs(coords[0] - pygame.mouse.get_pos()[0]), abs(coords[1] - pygame.mouse.get_pos()[1])
                x, y = coords[0] - a, coords[1]
                # pygame.draw.rect(screen, zvet_lastika, [0, 50, width, height])
                bg = pygame.image.load('./Безымянный.png')
                screen.blit(bg, (0, 0))
                pygame.draw.rect(screen, zvet_pryam, [x, y, a, b], 2)
                pygame.display.update()

        # Отсутствие лишней прорисовки
        if prev:
            zvet = previous
            prev = False


def start():
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode([width, height])
    screen.fill(pygame.Color('white'))
    pygame.display.flip()
    running = True

    def osnova():
        screen.fill(pygame.Color('white'))
        pygame.draw.rect(screen, pygame.Color('purple'), [0, 0, 400, 600])
        pygame.draw.rect(screen, pygame.Color('green'), [400, 0, 400, 600])
        f1 = pygame.font.Font(None, 100)
        text1 = f1.render('PAINT', True, (180, 0, 0))
        screen.blit(text1, (100, 250))
        text2 = f1.render('ДРУГОЕ', True, (180, 0, 0))
        screen.blit(text2, (450, 250))

        pygame.display.flip()
    while running:
        osnova()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] < 400:
                paint()
                running = False


start()
# paint()
