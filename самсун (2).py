import PIL
import pygame
import os, sys
import random
from PIL import Image
file = 'data\sound.mp3'
n = random.randint(1, 10)
mapname = 'mapp%s.txt' % n 
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
effect = pygame.mixer.Sound('data\eep.wav')

#pygame.event.wait()
print('1')
tile_width = tile_height = 100
HEIGHT, WIDTH = 700, 1300
size = 1300, 700
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)
FPS = 50
clock = pygame.time.Clock()
player = None

def boundx(n, a=0, b=12):
    if n < a:
        return a
    elif n > b:
        return b
    return n

def boundy(n, a=0, b=6):
    if n < a:
        return a
    elif n > b:
        return b
    return n

def tolist(s):
    aa = [x for x in s]
    return aa

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                new_player = x, y
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y

def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры:",
                  "Не пытаться идти против правил,",
                  "успешно дойти до финиша (синего квадрата)"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)

def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_mapp = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_mapp))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_mapp))


running = True
password = ''
clr = (55, 55, 55)
k = 0
walls, fin = [], []
start_screen()
player, l_x, l_y = generate_level(load_level(mapname))
mapp = load_level(mapname)
background = PIL.Image.new("RGB", (100 * len(mapp[0]), 100 * len(mapp)), (55, 55, 55))

for i in range(len(mapp)):
    for j in range(len(mapp[i])):
        if mapp[i][j] == '.':
            im = PIL.Image.open('data/WALL.PNG')
            walls.append([j, i])
            background.paste(im, (100 * j, 100 * i))
        elif mapp[i][j] == '*':
            im = PIL.Image.open('data/TILE.PNG')
            fin.append([j, i])
            background.paste(im, (100 * j, 100 * i))

background.save("data/level.png")
background = load_image("level.png")
        
x, y = player[0] * 100, player[1] * 100
effect1 = pygame.mixer.Sound('data\crack.wav')
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            #print(int(0.01 * x), int(0.01 * y), fin)
            if [int(0.01 * x), int(0.01 * y)] in fin:
                pygame.mixer.music.stop()
                effect = pygame.mixer.Sound('data\win.wav')
                effect.play(0)
                print('Enter the password:')
                password = input()
                while password != 'tumba':
                    if password == 'tumba':
                        
                        
                        break
                    else:
                        print('try again')
                        password = input('Enter the password:')
                print('please wait...')
                if [int(0.01 * x), int(0.01 * y)] in fin and password == 'tumba':
                    effect = pygame.mixer.Sound('data\win.wav')
                    effect.play(-1)
                    print('1')
                    screen.fill(clr)
                    font = pygame.font.Font(None, 30)
                    text_coord = 50
                    string_rendered = font.render('YOU WIN!!!', 1, pygame.Color('yellow'))
                    intro_rect = string_rendered.get_rect()
                    intro_rect.top = text_coord
                    intro_rect.x = 10
                    text_coord += intro_rect.height
                    screen.blit(string_rendered, intro_rect)
                    running = False
                    break
                
            elif event.key == pygame.K_UP:
                
                k += 1
                #screen.fill(clr)
                if y - 20 > -20 and [x / 100, (y - 100) / 100] not in walls:
                    y -= 100
                    effect.play()
                else:
                    effect1.play(0)
                #screen.blit(background, (0, 0))
                screen.blit(load_image("creature.png", colorkey=(255, 255, 255)), (x, y))
                font = pygame.font.Font(None, 30)
                text_coord = 50
                string_rendered = font.render(str(k), 1, pygame.Color('blue'))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
                pygame.display.flip()
            elif event.key == pygame.K_LEFT:
                
                k += 1
                #screen.fill(clr)
                if x - 20 > -20 and [(x - 100) / 100, y / 100] not in walls:
                    x -= 100
                    effect.play()
                else:
                    effect1.play(0)
                #screen.blit(background, (0, 0))
                screen.blit(load_image("creature.png"), (x, y))
                font = pygame.font.Font(None, 30)
                text_coord = 50
                string_rendered = font.render(str(k), 1, pygame.Color('blue'))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
                pygame.display.flip()
            elif event.key == pygame.K_DOWN:
                
                k += 1
                #screen.fill(clr)
                if y + 20 < l_y * 100 + 20 and [x / 100, y / 100 + 1] not in walls:
                    y += 100
                    effect.play()
                else:
                    effect1.play(0)
                #screen.blit(background, (0, 0))
                screen.blit(load_image("creature.png", colorkey=(255, 255, 255)), (x, y))
                font = pygame.font.Font(None, 30)
                text_coord = 50
                string_rendered = font.render(str(k), 1, pygame.Color('blue'))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
                pygame.display.flip()
            elif event.key == pygame.K_RIGHT:
                
                k += 1
                #screen.fill(clr)
                if x + 20 < l_x * 100 + 20 and [x / 100 + 1, y / 100] not in walls:
                    x += 100
                    effect.play()
                else:
                    effect1.play(0)
                #for i in range(len(mapp)):
                #    for j in range(len(mapp[i])):
                #        if mapp[i][j] == '#':
                #            screen.blit(load_image('WALL.png', colorkey=(255, 255, 255)), (j * 100, i * 100))
                #        elif mapp[i][j] == '*':
                #            screen.blit(load_image('TILE.png', colorkey=(255, 255, 255)), (j * 100, i * 100))
                #if mapp[int(x) // 100][int(y) // 100] == '#':
                #    screen.blit(load_image('WALL.png', colorkey=(255, 255, 255)), (int(x) // 100, int(y) // 100))
                #elif mapp[i][j] == '*':
                #    screen.blit(load_image('TILE.png', colorkey=(255, 255, 255)), (int(x) // 100, int(y) // 100))
                #screen.blit(background, (0, 0))
                screen.blit(load_image("creature.png", colorkey=(255, 255, 255)), (x, y))
                font = pygame.font.Font(None, 30)
                text_coord = 50
                string_rendered = font.render(str(k), 1, pygame.Color('blue'))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
                pygame.display.flip()
        if fin in [x, y] and password == 'tumba':
            screen.fill(clr)
            font = pygame.font.Font(None, 30)
            text_coord = 50
            string_rendered = font.render('YOU WIN!!!', 1, pygame.Color('yellow'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
            
            
            running = False
        else:
            screen.fill(clr)
            for i in range(len(mapp)):
                for j in range(len(mapp[i])):
                    if mapp[i][j] == '#':
                        screen.blit(load_image('WALL.png', colorkey=(255, 255, 255)), (j * 100, i * 100))
                    elif mapp[i][j] == '*':
                        screen.blit(load_image('TILE.png', colorkey=(255, 255, 255)), (j * 100, i * 100))
            screen.blit(load_image("creature.png", colorkey=(255, 255, 255)), (x, y))
            font = pygame.font.Font(None, 30)
            text_coord = 50
            string_rendered = font.render(str(k), 1, pygame.Color('blue'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)


    pygame.display.flip()
