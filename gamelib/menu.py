import sys
import media
import pygame
from pygame.locals import *


def novoJogo(screen):
    # Falta o game.. rs
    pass


class Menu(object):    

    def __init__(self, screen):
        media.executar_musica("menu_loop.wav", 0.75)
        self.screen = screen
        self.menu = NFMenu(["Novo Jogo", lambda: novoJogo(screen)], ["Sair", sys.exit])
        self.clock = pygame.time.Clock()
        events = pygame.event.get()
        self.menu.update(events)
        self.menu.draw(self.screen)
        self.bg = media.carrega_imagem_menu('menu_background.jpg')
        self.fonteGrande = pygame.font.Font(media.carrega_fonte("BLADRMF_.TTF"), 120)

    def loop(self):
        while True:
            self.clock.tick(40)
            events = pygame.event.get()
            self.menu.update(events)
            self.screen.blit(self.bg, (0, 0))
            ren = self.fonteGrande.render("Jump", 1, (255, 255, 255))
            self.screen.blit(ren, (350-ren.get_width()/2, 180))
            self.menu.draw(self.screen)
            pygame.display.flip()


class NFMenu:

    def __init__(self, *vetor_funcoes_menu):

        self.vetor_funcoes_menu = vetor_funcoes_menu
        self.som_menu_item = media.obter_som('menu_item.wav')
        self.hcolor = (255, 0, 0)
        self.fonte = pygame.font.Font(media.carrega_fonte("GOODTIME.ttf"), 50)
        self.posicao_atual = 0
        self.width = 1
        self.color = [255, 255, 255]
        self.hcolor = [150, 50, 100]
        self.height = len(self.vetor_funcoes_menu)*self.fonte.get_height()
        for funcao in self.vetor_funcoes_menu:
            texto = funcao[0]
            ren = self.fonte.render(texto, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()
        self.x = 350-(self.width/2)
        self.y = 450-(self.height/2)

    def draw(self, surface):
        i=0
        for funcao in self.vetor_funcoes_menu:
            if i==self.posicao_atual:
                clr = self.hcolor
            else:
                clr = self.color
            texto = funcao[0]
            ren = self.fonte.render(texto, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, ((self.x+self.width/2) - ren.get_width()/2, self.y + i*(self.fonte.get_height()+4)))
            i+=1
            
    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.posicao_atual += 1
                    self.som_menu_item.play()
                if e.key == pygame.K_UP:
                    self.posicao_atual -= 1
                    self.som_menu_item.play()
                if e.key == pygame.K_RETURN:
                    self.vetor_funcoes_menu[self.posicao_atual][1]()
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    sys.exit()
        if self.posicao_atual > len(self.vetor_funcoes_menu)-1:
            self.posicao_atual = 0
        if self.posicao_atual < 0:
            self.posicao_atual = len(self.vetor_funcoes_menu)-1