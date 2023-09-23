import pygame
from pygame.locals import *
from sys import exit
from random import randint
import os
import time

pygame.init()

# Carregar uma imagem de fundo.
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#cria o botao
class Button():
	def __init__(self, image, x_pos, y_pos):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		tela.blit(self.image, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

#definindo o botao de play
button_surface = pygame.image.load("play.png")
button_surface = pygame.transform.scale(button_surface, (210, 109))
button = Button(button_surface, 363, 410)

button_surface2 = pygame.image.load("volta.png")
button_surface2 = pygame.transform.scale(button_surface2, (104, 79))
button2 = Button(button_surface2, 52, 460)

button_sergio = pygame.image.load("sergio.png")
button_sergio = pygame.transform.scale(button_sergio, (205, 297))
sergio = Button(button_sergio, 216, 237)

button_claudio = pygame.image.load("claudio.png")
button_claudio = pygame.transform.scale(button_claudio, (198, 293))
claudio = Button(button_claudio, 493, 238)

button_curto = pygame.image.load("curto.png")
button_curto = pygame.transform.scale(button_curto, (183, 91))
curto = Button(button_curto, 389, 222)

button_infinito = pygame.image.load("infinito.png")
button_infinito = pygame.transform.scale(button_infinito, (180, 91))
infinito = Button(button_infinito, 394, 348)

button_surface3 = pygame.image.load("casa.png")
button_surface3 = pygame.transform.scale(button_surface3, (121, 122))
button3 = Button(button_surface3, 81, 413)

#função pra colocar sprite na comida
#class Food(pygame.sprite.Sprite):
#    def __init__(self):
#        pygame.sprite.Sprite.__init__(self)
#        self.sprites = []
#        self.sprites.append('Documentos/comida.png')
#        self.atual = 0
#        self.image = self.sprites[self.atual]
#        #self.rect = self.image.get_rect()

#food = Food()

BackGround = Background('61_Sem_Titulo.png', [0,0])
Tela_Inicial = Background('inicio.png', [0,0])
Tela_Selecao = Background('selecao.png', [0,0])
Tela_Modo = Background('modo.png', [0,0])
Tela_Creditos = Background('creditos.png', [0,0])

# Musica de fundo e Volume.
pygame.mixer.music.set_volume(0.2)
m_fundo = pygame.mixer.music.load('tela_inicio.wav')
pygame.mixer.music.play(-1)

# Musica quando come a comida.
m_comida = pygame.mixer.Sound('smw_dragon_coin.wav')
m_dano = pygame.mixer.Sound('dano.wav')
m_botao = pygame.mixer.Sound('botao_inicio.wav')
m_botao2 = pygame.mixer.Sound('botao_selecao.wav')
m_comida2 = pygame.mixer.Sound('comida_final.wav')

# Tamanho da tela.
largura = 800
altura = 500

# Posicao da cobrinha.
x_cobra = int(largura//2)
y_cobra = int(altura//2)

velocidade = 2.5
x_controle = velocidade
y_controle = 0

# Posicao da comida.
x_comida = randint(120, 650)
y_comida = randint(120, 450)

# Quantidade de vezes que a cobrinha comeu a comida.
pontos = 0

#Parametro, Tamanho, Negrito e Italico.
fonte = pygame.font.SysFont('Comic Sans', 25, True, False)

# Montando a tela.
tela = pygame.display.set_mode((largura, altura))

# Nome que vai ter o arquivo na hora que abrir.
pygame.display.set_caption('TRABALHO DE ENGENHARIA DE SOFTWARE')

relogio = pygame.time.Clock()

# Tamanho da cobra.
lista_cobra = []

# Tamanho inicial da cobra.
tam_inicial = 2

# Variavel com valor boolean para resetar o jogo.
morreu = False

# Contador de partidas.
cont = 0
rec0 = 0
rec = 0
rec2 = 0
inicio = 0
modo = 0

# Carregar os arquivos de imagens
def carregar_arquivos(self):
    diretorio = os.path.join(os.getcwd(), 'img')

# Funcao que desenha a cobra.
def aumenta_cobra(lista_cobra):
    for xy in lista_cobra:
        pygame.draw.circle(tela, (44, 44, 44), (xy[0], xy[1]), 15) #skin preta (Sérgio)

def aumenta_cobra2(lista_cobra):
    for xy in lista_cobra:
        pygame.draw.circle(tela, (126, 20, 186), (xy[0], xy[1]), 15) #skin roxa (Cláudio)

def iniciar():
    global pontos, tam_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_comida, y_comida, morreu, velocidade
    m_fundo = pygame.mixer.music.load('tela_inicio.wav')
    pygame.mixer.music.play(-1)
    pontos = 0
    tam_inicial = 2
    velocidade = 2.5
    x_cobra = int(largura//2)
    y_cobra = int(altura//2)
    lista_cobra = []
    lista_cabeca = []
    morreu = False

def reiniciar():
    global pontos, tam_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_comida, y_comida, morreu, velocidade
    gameplay = pygame.mixer.music.load('musica_gameplay.wav')
    pygame.mixer.music.play(-1)
    pontos = 0
    tam_inicial = 2
    velocidade = 2.5
    x_cobra = int(largura//2)
    y_cobra = int(altura//2)
    lista_cobra = []
    lista_cabeca = []
    x_comida = randint(120, 550)
    y_comida = randint(120, 350)
    morreu = False

while 1:
    relogio.tick(60)
    
    #tela de inicio
    if inicio == 0:
        tela.fill([255, 255, 255])
        tela.blit(Tela_Inicial.image, Tela_Inicial.rect)

        texto = f'Recorde: {rec0}'
        recorde = fonte.render(texto, True, (110, 75, 24))
        centro = recorde.get_rect()
        centro = (295, 135)
        tela.blit(recorde, centro)
        cont = 0
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    m_botao.play()
                    time.sleep(0.1)
                    inicio = 1
        button.update()

    #tela de seleção de personagem 
    if inicio == 1:
        tela.fill([255, 255, 255])
        tela.blit(Tela_Selecao.image, Tela_Selecao.rect)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if button2.rect.collidepoint(pygame.mouse.get_pos()):
                    m_botao.play()
                    time.sleep(0.1)
                    inicio = 0
                if sergio.rect.collidepoint(pygame.mouse.get_pos()):
                    skin = 0
                    m_botao2.play()
                    time.sleep(0.1)
                    inicio = 2
                if claudio.rect.collidepoint(pygame.mouse.get_pos()):
                    skin = 1
                    m_botao2.play()
                    time.sleep(0.1)
                    inicio = 2
                    
        button2.update()
        sergio.update()
        claudio.update()

    # Selecao do modo longo/infinito ou curto.
    if inicio == 2:
        tela.fill([255, 255, 255])
        tela.blit(Tela_Modo.image, Tela_Modo.rect)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
                if button2.rect.collidepoint(pygame.mouse.get_pos()):
                    m_botao.play()
                    time.sleep(0.1)
                    inicio = 1
                if curto.rect.collidepoint(pygame.mouse.get_pos()):
                    modo = 1
                    m_botao2.play()
                    time.sleep(0.3)
                    gameplay = pygame.mixer.music.load('musica_gameplay.wav')
                    pygame.mixer.music.play(-1)
                    inicio = 3
                if infinito.rect.collidepoint(pygame.mouse.get_pos()):
                    modo = 2
                    m_botao2.play()
                    time.sleep(0.3)
                    gameplay = pygame.mixer.music.load('musica_gameplay.wav')
                    pygame.mixer.music.play(-1)
                    inicio = 3
                    
        button2.update()
        curto.update()
        infinito.update()

    #tela de gameplay do jogo
    if inicio == 3:
        tela.fill([255, 255, 255])
        tela.blit(BackGround.image, BackGround.rect)
    
        # definindo a comida com os sprites
        #comida = Food((x_comida, y_comida))
        #group = pygame.sprite.RenderPlain()
        #group.add(comida)
        #group.draw(tela)
        #pygame.display.flip()

        # Mensagem de quantidade de pontos.
        if modo == 1:
            msg = f'Pontos: {pontos}/30'
        else:
            msg = f'Pontos: {pontos}'
        # Mensagem de quantidade de partidas.
        msg2 = f'Mortes: {cont}'

        # Mensagem de recorde.
        if modo == 1:
            msg3 = f'Recorde: {rec}'
        else:
            msg3 = f'Recorde: {rec2}'

        # Texto, pixelado, RGB. Exibe a Mensagem na tela 'Pontos' e 'Partidas'.
        textinho = fonte.render(msg, True, (161, 115, 66))
        textinho2 = fonte.render(msg2, True, (161, 115, 66))
        textinho3 = fonte.render(msg3, True, (161, 115, 66))

        # Imprimir a mensagem na tela. Parametros: Eixo X e Eixo Y.
        tela.blit(textinho, (15, 5))
        tela.blit(textinho2, (15, 30))
        tela.blit(textinho3, (15, 55))

        # Quando clicar no 'X' o jogo fecha. 
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

        # Movimentacao dentro do jogo com w, d, a, s e faz com que continue andando.
            if evento.type == KEYDOWN:
                if evento.key == K_a or evento.key == K_LEFT:
                    if x_controle == velocidade:
                        pass

                    else:
                        x_controle = -velocidade
                        y_controle = 0

                if evento.key == K_d or evento.key == K_RIGHT:
                    if x_controle == -velocidade:
                        pass

                    else:
                        x_controle = velocidade
                        y_controle = 0

                if evento.key == K_w or evento.key == K_UP:
                    if y_controle == velocidade:
                        pass

                    else:
                        y_controle = -velocidade
                        x_controle = 0

                if evento.key == K_s or evento.key == K_DOWN:
                    if y_controle == -velocidade:
                        pass

                    else:
                        y_controle = velocidade
                        x_controle = 0

        x_cobra = x_cobra + x_controle
        y_cobra = y_cobra + y_controle

        # Desenho da cobrinha. Parametros: RGB, eixo x, eixo y, raio e preenchimetno do circulo.
        if skin == 0:
            cobrinha = pygame.draw.circle(tela, (44, 44, 44), (x_cobra, y_cobra), 15) #skin preta da centopeia (Sérgio)
        if skin == 1:
            cobrinha = pygame.draw.circle(tela, (126, 20, 186), (x_cobra, y_cobra), 15) #skin roxa da centopeia (Cláudio)

        # Desenho da comida.
        if modo == 1 and pontos == 29:
            comida = pygame.draw.circle(tela, (0, 0, 0), (x_comida, y_comida), 8)
        else:
            comida = pygame.draw.circle(tela, (214, 192, 26), (x_comida, y_comida), 8)
        #comida = Food((x_comida, y_comida))

        # Desenhos das paredes.
        t_teto = pygame.draw.rect(tela, (0, 0, 0), (0, 0, 800, 1))
        t_chao = pygame.draw.rect(tela, (0, 0, 0), (0, 499, 800, 30))
        parede_esquerda = pygame.draw.rect(tela, (0, 0, 0), (0, 0, 2, 500))
        parede_direita = pygame.draw.rect(tela, (0, 0, 0), (799, 0, 30, 500))

        # Colisao a comida.
        if cobrinha.colliderect(comida):
            if modo == 1 and pontos == 29:
                pontos += 1
                if pontos >= rec:
                    rec = pontos

                pygame.mixer.music.set_volume(0.5)
                m_comida2.play()
            else:
                x_comida = randint(50, 750)
                y_comida = randint(10, 450)
                #Food.draw(tela)
                #Food.update()

                # Aumenta a contagem de pontos
                pontos +=1
                if pontos >= rec and modo == 1:
                    rec = pontos
                if pontos >= rec2 and modo == 2:
                    rec2 = pontos

                # Musica
                m_comida.play()

                # Aumenta o tamanho da cobra.
                tam_inicial += 2

                # Aumenta a velocidade da cobra.
                velocidade += 0.2

        # Posicoes que a cobra ja assumiu.
        lista_cabeca = []
        lista_cabeca.append(x_cobra)
        lista_cabeca.append(y_cobra)

        # Tamanho da cobra.
        lista_cobra.append(lista_cabeca)

        # Reiniciar o jogo, apresenta uma mensagem de 'Game Over' e reseta todas as posicoes
        if lista_cobra.count(lista_cabeca) > 1 or cobrinha.colliderect(t_teto) or cobrinha.colliderect(t_chao) or cobrinha.colliderect(parede_direita) or cobrinha.colliderect(parede_esquerda):
            velocidade = 2.5
            m_dano.play()
            time.sleep(0.3)
            m_morte = pygame.mixer.music.load('morte.wav')
            pygame.mixer.music.play(-1)
            fonte2 = pygame.font.SysFont('Comic Sans', 25, True, False)
            fonte3 = pygame.font.SysFont('Press Start 2P', 65, True, False)
            msg = 'GAME OVER'
            msg2 = "Pressione a tecla 'R' para reiniciar o jogo"
            msg3 = "ou pressione a tecla 'E' para voltar a tela inicial"
            textinho = fonte3.render(msg, True, (255, 255, 255))
            textinho2 = fonte2.render(msg2, True, (255, 255, 255))
            textinho3 = fonte2.render(msg3, True, (255, 255, 255))
            ret_textinho = textinho.get_rect()
            ret_textinho2 = textinho2.get_rect()
            ret_textinho3 = textinho3.get_rect()
            morreu = True
            pontos = 0
            tam_inicial = 2
            x_cobra = int(largura//2)
            y_cobra = int(altura//2)
            lista_cobra = []
            lista_cabeca = []

            # Deixa a tela preta, reinicia ao clicar na tecla 'R' e apresenta uma mensagem de 'Game Over'.
            while morreu:
                tela.fill((0, 0 ,0))
                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        pygame.quit()
                        exit()

                    if evento.type == KEYDOWN:
                        if evento.key == K_r:
                            cont += 1
                            velocidade = 2.5
                            pygame.mixer.music.stop()
                            reiniciar()

                        if evento.key == K_e:
                            inicio = 0
                            if modo == 1:
                                rec0 = rec
                            else:
                                rec0 = rec2
                            pygame.mixer.music.stop()
                            iniciar()

                ret_textinho.center = (400, 215)
                ret_textinho2.center = (400, 250)
                ret_textinho3.center = (400, 280)
                tela.blit(textinho, ret_textinho)
                tela.blit(textinho2, ret_textinho2)
                tela.blit(textinho3, ret_textinho3)
                pygame.display.flip()

        if x_cobra > largura:
            x_cobra = 0

        if x_cobra < 0:
            x_cobra = largura

        if y_cobra < 0:
            y_cobra = altura

        if y_cobra > altura:
            y_cobra = 0

        # Condicao para a cobra parar de crescer indefinidamente.
        if len(lista_cobra) > tam_inicial:
            del lista_cobra[0]

        # Chama a funcao que aumenta o tamanho da cobra.
        if skin == 0:
            aumenta_cobra(lista_cobra)
        if skin == 1:
            aumenta_cobra2(lista_cobra)

        if modo == 1 and pontos == 30:
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(0.2)
            m_creditos = pygame.mixer.music.load('musica_creditos.wav')
            pygame.mixer.music.play(-1)
            tela.fill([255, 255, 255])
            tela.blit(Tela_Creditos.image, Tela_Creditos.rect)
            while pontos == 30:
                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        pygame.quit()
                        exit()
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if button3.rect.collidepoint(pygame.mouse.get_pos()):
                            m_botao.play()
                            time.sleep(0.1)
                            inicio = 0
                            rec0 = rec
                            modo = 0
                            pontos = 0
                            pygame.mixer.music.stop()
                            iniciar()
                button3.update()
                pygame.display.flip()

    pygame.display.flip()
