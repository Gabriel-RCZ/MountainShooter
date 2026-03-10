#!/usr/bin/python
# -*- coding: utf-8 -*-



import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, MENU_OPTION, WIN_WIDTH


class Menu:
    def __init__(self, window):
        #Desenhando imagens na Janela
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        selected_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'MOUNTAIN', COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'SHOOTER', COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            #Código para quando selecionar a opção ela trocar de cor
            for i in range(len(MENU_OPTION)):
                if i == selected_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            
            #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() ##Close Window
                    quit() ##End Pygame

            #Código para selecionar as opções no MENU
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if selected_option < len(MENU_OPTION) - 1:
                            selected_option += 1
                        else:
                            selected_option = 0

                    if event.key == pygame.K_UP:
                        if selected_option > 0:
                            selected_option -= 1
                        else:
                            selected_option = len(MENU_OPTION) - 1
                    #Selecionar opções no Menu
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[selected_option]

            pygame.display.flip()

    #Código das configurações de textos do Menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
