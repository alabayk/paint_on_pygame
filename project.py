import pygame
import os
import shutil
from tkinter.filedialog import askopenfilename


def paint(nazad):
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
            back = pygame.image.load(f"{os.path.dirname(os.path.abspath(__file__))}\\prom-file.png")
            screen.blit(back, (0, 0))
        if not fon:
            text1 = f1.render('Выберите цвет кисти:', True, (180, 0, 0))
        else:
            text1 = f1.render('Выберите цвет фона:', True, (180, 0, 0))
        save = pygame.image.load('./data/save.png')
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
        screen.blit(save, (310, 10))
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
        baza()

        for event in pygame.event.get():
            # Выход из программы
            if event.type == pygame.QUIT:
                ask()
                running = False

            # Проверка на нажатие
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] >= 50:
                nazhat = True
                coords = event.pos
                if flag_ris:
                    svezh[0].append(zvet)
                    svezh.append([])
                    i_global += 1

            # Сохранение
            if event.type == pygame.MOUSEBUTTONDOWN and 310 <= event.pos[0] < 340 and 10 <= event.pos[1] < 40:
                ask()
                running = False
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
                if nazad:
                    shutil.copy(f"{os.path.dirname(os.path.abspath(__file__))}\\new.png",
                                f"{os.path.dirname(os.path.abspath(__file__))}\\prom-file.png")
                    back = pygame.image.load(f"{os.path.dirname(os.path.abspath(__file__))}\\prom-file.png")
                    screen.blit(back, (0, 0))
                    nazad = False
                pygame.image.save(screen, 'prom-file.png')
                if flag_pryam:
                    if event.pos[1] >= 50:
                        if coords[0] <= pygame.mouse.get_pos()[0] and coords[1] <= pygame.mouse.get_pos()[1]:
                            a, b = abs(coords[0]-pygame.mouse.get_pos()[0]), abs(coords[1]-pygame.mouse.get_pos()[1])
                            x, y = coords
                            history.append(((x, y), (a, b)))
                        elif coords[0] >= pygame.mouse.get_pos()[0] and coords[1] >= pygame.mouse.get_pos()[1]:
                            a, b = abs(coords[0]-pygame.mouse.get_pos()[0]), abs(coords[1]-pygame.mouse.get_pos()[1])
                            x, y = pygame.mouse.get_pos()
                            history.append(((x, y), (a, b)))
                        elif coords[0] <= pygame.mouse.get_pos()[0] and coords[1] >= pygame.mouse.get_pos()[1]:
                            a, b = abs(coords[0]-pygame.mouse.get_pos()[0]), abs(coords[1]-pygame.mouse.get_pos()[1])
                            x, y = coords[0], coords[1] - b
                            history.append(((x, y), (a, b)))
                        elif coords[0] >= pygame.mouse.get_pos()[0] and coords[1] <= pygame.mouse.get_pos()[1]:
                            a, b = abs(coords[0]-pygame.mouse.get_pos()[0]), abs(coords[1]-pygame.mouse.get_pos()[1])
                            x, y = coords[0] - a, coords[1]
                            history.append(((x, y), (a, b)))


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
                bg = pygame.image.load('./prom-file.png')
                screen.blit(bg, (0, 0))
                pygame.draw.rect(screen, zvet_pryam, [x, y,  a, b], 2)
                pygame.display.update()
            # 2 четверть
            elif coords[0] >= pygame.mouse.get_pos()[0] and coords[1] >= pygame.mouse.get_pos()[1]:
                a, b = abs(coords[0] - pygame.mouse.get_pos()[0]), abs(coords[1] - pygame.mouse.get_pos()[1])
                x, y = pygame.mouse.get_pos()
                # pygame.draw.rect(screen, zvet_lastika, [0, 50, width, height])
                bg = pygame.image.load('./prom-file.png')
                screen.blit(bg, (0, 0))
                pygame.draw.rect(screen, zvet_pryam, [x, y, a, b], 2)
                pygame.display.update()
            # 1 четверть
            elif coords[0] <= pygame.mouse.get_pos()[0] and coords[1] >= pygame.mouse.get_pos()[1]:
                a, b = abs(coords[0] - pygame.mouse.get_pos()[0]), abs(coords[1] - pygame.mouse.get_pos()[1])
                x, y = coords[0], coords[1] - b
                # pygame.draw.rect(screen, zvet_lastika, [0, 50, width, height])
                bg = pygame.image.load('./prom-file.png')
                screen.blit(bg, (0, 0))
                pygame.draw.rect(screen, zvet_pryam, [x, y, a, b], 2)
                pygame.display.update()
            # 3 четверть
            elif coords[0] >= pygame.mouse.get_pos()[0] and coords[1] <= pygame.mouse.get_pos()[1]:
                a, b = abs(coords[0] - pygame.mouse.get_pos()[0]), abs(coords[1] - pygame.mouse.get_pos()[1])
                x, y = coords[0] - a, coords[1]
                # pygame.draw.rect(screen, zvet_lastika, [0, 50, width, height])
                bg = pygame.image.load('./prom-file.png')
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] < 400:
                    paint(False)
                    running = False
                elif event.pos[0] >= 40:
                    proga_mashi_i_stepana()
                    running = False


def file_save():
    class TextInputBox(pygame.sprite.Sprite):
        def __init__(self, x, y, w, font):
            super().__init__()
            self.color = (0, 0, 0)
            self.backcolor = None
            self.pos = (x, y)
            self.width = w
            self.font = font
            self.active = False
            self.text = ".png"
            self.render_text()
            self.a = []
            self.flag = False
            self.sp = [pygame.K_TAB, pygame.K_DELETE, pygame.K_SPACE, pygame.K_COMMA, pygame.K_INSERT, pygame.K_LEFT,
                       pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

        def render_text(self):
            t_surf = self.font.render(self.text, True, self.color, self.backcolor)
            self.image = pygame.Surface((max(self.width, t_surf.get_width() + 10), t_surf.get_height() + 10),
                                        pygame.SRCALPHA)
            if self.backcolor:
                self.image.fill(self.backcolor)
            self.image.blit(t_surf, (5, 5))
            pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
            self.rect = self.image.get_rect(topleft=self.pos)

        def update(self, event_list):
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                    self.active = self.rect.collidepoint(event.pos)
                if event.type == pygame.KEYDOWN and self.active:
                    if event.key == pygame.K_RETURN:
                        if len(self.a) != 0:
                            self.flag = True
                        else:
                            pass
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-5] + '.png'
                        self.a = self.a[:-1]
                        self.flag = False
                    elif event.key not in self.sp:
                        self.a.append(event.unicode)
                        self.text = ''.join(self.a) + '.png'
                        self.flag = False
                    self.render_text()
                    self.render_text()

        def show(self):
            return self.text

        def is_enter(self):
            return self.flag

        def is_text(self):
            if len(self.text) > 4 and self.text != 'prom-file.png'and self.text != 'new.png':
                return True
            else:
                return False

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font_1 = pygame.font.SysFont(None, 40)
    font_2 = pygame.font.Font(None, 30)
    font_3 = pygame.font.Font(None, 45)
    baze = font_2.render('click here to add text', True, (0, 0, 0))
    asking = font_2.render('Укажите желаемое название файла:', True, (0, 0, 0))
    save = font_2.render('Сохранить', True, (255, 255, 255))
    back = font_2.render('Вернуться к рисунку', True, (255, 255, 255))
    error = font_3.render('ОШИБКА! Файл с таким именем уже существует', True, (255, 0, 0))
    flag_error = False
    text_input_box = TextInputBox(200, 300, 400, font_1)
    group = pygame.sprite.Group(text_input_box)
    flag_1 = True
    flag_2 = False
    flag_save = False

    run = True
    while run:
        clock.tick(60)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= event.pos[0] < 600 and 450 <= event.pos[1] < 487:
                    shutil.copy(f"{os.path.dirname(os.path.abspath(__file__))}\\prom-file.png",
                                f"{os.path.dirname(os.path.abspath(__file__))}\\new.png")
                    paint(True)
                    run = False
                if 200 <= event.pos[0] < 600 and 300 <= event.pos[1] < 337:
                    flag_2 = True
                if flag_save:
                    if 201 <= event.pos[0] < 600 and 380 <= event.pos[1] < 417 and text_input_box.is_text():
                        flag_1 = False
                        text = text_input_box.show()
                        if os.path.isfile(f'{os.path.dirname(os.path.abspath(__file__))}\\{text}'):
                            pygame.draw.rect(screen, pygame.Color('red'), (201, 301, 398, 37), 2)
                            flag_error = True
                            flag_1 = True
                        else:
                            os.rename('prom-file.png', text)
                            print()
                            print(f"file has been saved as {os.path.dirname(os.path.abspath(__file__))}\\{text}")
                            run = False
        group.update(event_list)

        screen.fill(pygame.Color('white'))
        screen.blit(asking, (200, 220))
        pygame.draw.rect(screen, pygame.Color('gray'), (201, 450, 398, 37), )
        screen.blit(back, (301, 460))
        if text_input_box.is_text():
            pygame.draw.rect(screen, pygame.Color(100, 100, 100), (201, 380, 398, 37), )
            screen.blit(save, (346, 390))
            flag_save = True
        else:
            pygame.draw.rect(screen, pygame.Color(211, 211, 211), (201, 380, 398, 37), )
            screen.blit(save, (346, 390))
        if flag_1:
            if flag_2:
                group.draw(screen)
            else:
                pygame.draw.rect(screen, pygame.Color('black'), (201, 301, 398, 37), 2)
                screen.blit(baze, (300, 310))
        if flag_error:
            screen.blit(error, (30, 50))

        if text_input_box.is_enter() and text_input_box.is_text():
            flag_1 = False
            text = text_input_box.show()
            if os.path.isfile(f'{os.path.dirname(os.path.abspath(__file__))}\\{text}'):
                pygame.draw.rect(screen, pygame.Color('red'), (201, 301, 398, 37), 2)
                flag_error = True
                flag_1 = True
            else:
                os.rename('prom-file.png', text)
                final()
                print()
                print(f"file has been saved as {os.path.dirname(os.path.abspath(__file__))}\\{text}")
                run = False

        pygame.display.flip()

    pygame.quit()
    exit()


def ask():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font_2 = pygame.font.Font(None, 30)
    back = font_2.render('Вернуться к рисунку', True, (255, 255, 255))
    asking = font_2.render('Хотите ли Вы сохранить ваш рисунок?', True, (0, 0, 0))
    yes = font_2.render('Да', True, (255, 255, 255))
    no = font_2.render('Нет', True, (255, 255, 255))
    running = True

    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= event.pos[0] < 600 and 450 <= event.pos[1] < 487:
                    shutil.copy(f"{os.path.dirname(os.path.abspath(__file__))}\\prom-file.png",
                                f"{os.path.dirname(os.path.abspath(__file__))}\\new.png")
                    paint(True)
                    running = False
                if 200 <= event.pos[0] < 300 and 270 <= event.pos[1] < 370:
                    file_save()
                    running = False
                elif 500 <= event.pos[0] < 600 and 270 <= event.pos[1] < 370:
                    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}\\prom-file.png")
                    running = False

        screen.fill(pygame.Color('white'))
        pygame.draw.rect(screen, pygame.Color('gray'), (201, 450, 398, 37), )
        screen.blit(back, (301, 460))
        screen.blit(asking, (210, 170))
        pygame.draw.rect(screen, pygame.Color('green'), [200, 270, 100, 100])
        screen.blit(yes, (235, 310))
        # pygame.draw.line(screen, pygame.Color('blue'), (200, 270), (500, 270), 3)
        pygame.draw.rect(screen, pygame.Color('red'), [500, 270, 100, 100])
        screen.blit(no, (535, 310))
        pygame.display.flip()

def final():
    print('final')
    if os.path.isfile(f'{os.path.dirname(os.path.abspath(__file__))}\\prom-file.png'):
        print('yes - prom')
        os.remove(f"{os.path.dirname(os.path.abspath(__file__))}\\prom-file.png")
    if os.path.isfile(f'{os.path.dirname(os.path.abspath(__file__))}\\new.png'):
        print('yes - new')
        os.remove(f"{os.path.dirname(os.path.abspath(__file__))}\\new.png")

def proga_mashi_i_stepana():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font_1 = pygame.font.Font(None, 36)
    text = font_1.render('Скоро здесь будет что-то...', True, pygame.Color('red'))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(text, (250, 250))
        pygame.display.flip()


start()

