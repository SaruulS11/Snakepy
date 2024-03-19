import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 620))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/tahomaGC.ttf", size)

def play():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        EASY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250), 
                            text_input="АМАРХАН", font=get_font(75), base_color="#d7fcd4", hovering_color="Orange")
        HARD_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="ХЭЦҮҮ", font=get_font(75), base_color="#d7fcd4", hovering_color="Orange")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="БУЦАХ", font=get_font(75), base_color="#d7fcd4", hovering_color="Orange")

        for button in [EASY_BUTTON, HARD_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from Easysnake import Easysnake
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from snake import snake
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Тоглоомын дүрэм:", True, "Black")
        OPTIONS_TEXT = get_font(45).render("1.Амархан үе - Могой талбөйн хүрээнээс гадуур\nгарсан үед талбөйн нөгөө тал руу шилжинэ.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(140, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("МОГОЙ", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250), 
                            text_input="ТОГЛОХ", font=get_font(75), base_color="#d7fcd4", hovering_color="Orange")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="ТУХАЙ", font=get_font(75), base_color="#d7fcd4", hovering_color="Orange")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="ГАРАХ", font=get_font(75), base_color="#d7fcd4", hovering_color="Orange")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

#2:30
