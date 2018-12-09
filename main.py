# 
import keyboard, pyautogui, pygame
import modules.utility as u
import modules.ui as ui
import modules.menu as m
import modules.functions as f

pygame.init()

appVersion = 'python_pygame_gui_template'
dev = False

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (0,102,0)
light_green = (0,255,0)
darkblue = (21,35,45)
lightblue = (22,48,66)
textgrey = (170,170,170)
display_width = 300
display_height  = 450
FPS = 30

botMainApp = True

font = pygame.font.SysFont(None, 25)
pygame.display.set_caption(appVersion)
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()


while botMainApp:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            botMainApp = False

    # Hot keys

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            botMainApp = False
        if event.key == pygame.K_p:
            print('hotkey1')
        if event.key == pygame.K_o:
            print('hotkey2')
        if event.key == pygame.K_i:
            print('hotkey3')


    ui.user_interface()

    