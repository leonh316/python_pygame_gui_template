import keyboard, pyautogui, pygame
from ctypes import windll

pygame.init()

appVersion = 'python_pygame_gui_template'
dev = False

white = (255,255,255)
black = (0,0,0)
red = (140,0,0)
light_red = (255,0,0)
yellow = (200,140,0)
light_yellow = (255,255,0)
green = (0,140,0)
light_green = (0,255,0)
darkblue = (21,35,45)
lightblue = (22,48,66)
textgrey = (170,170,170)
display_width = 300
display_height  = 450

display_width = 300
display_height  = 80
FPS = 30
alwaysOnTop = True

NOSIZE = 1
NOMOVE = 2
TOPMOST = -1
NOT_TOPMOST = -2

botMainApp = True

tinyfont = pygame.font.SysFont("comicsansms", 16)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

pygame.display.set_caption(appVersion)
gameDisplay = pygame.display.set_mode((display_width,display_height))
SetWindowPos = windll.user32.SetWindowPos
clock = pygame.time.Clock()

def always_on_top(yesOrNo):
    zorder = (NOT_TOPMOST, TOPMOST)[yesOrNo] # choose a flag according to bool
    hwnd = pygame.display.get_wm_info()['window'] # handle to the window
    SetWindowPos(hwnd, zorder, 0, 0, 0, 0, NOMOVE|NOSIZE)

def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,xScreen,yScreen):
    screen_text = tinyfont.render(msg, True, color)
    gameDisplay.blit(screen_text, [xScreen, yScreen])

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

def menu_nav_ui_box():
    pygame.draw.rect(gameDisplay, lightblue, [5,5,490,50])

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                print(1)

            if action == "play":
                print(2)

            if action == "main":
                game_intro()
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

def ui_menu_text():
    message_to_screen(appVersion, textgrey, 10, 10)
    message_to_screen("failsafe:mousemove top left screen", textgrey, 10, 30)
    message_to_screen('Controls', textgrey, 10, 80)
    message_to_screen('hotkeys', textgrey, 160, 80)
    message_to_screen('hotkey1 = ', textgrey, 160, 110)
    message_to_screen('hotkey2 = ', textgrey, 160, 140)
    message_to_screen('hotkey3 = ', textgrey, 160, 170)

def user_interface():
    always_on_top(True)
    gameDisplay.fill(darkblue)
    menu_nav_ui_box()
    button("start", 10,110,100,30, green, light_green, action="start")
    button("pause", 10,140,100,30, yellow, light_yellow, action="pause")
    button("quit", 10,170,100,30, red, light_red, action ="stop")
    ui_menu_text()
    pygame.display.update()
    clock.tick(FPS)




