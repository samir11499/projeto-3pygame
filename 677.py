
# pip install pygame

import pygame
import random

pygame.init()

# ---------------- TELA ----------------

LARGURA = 1000
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("67 Game")

# ---------------- FPS ----------------

clock = pygame.time.Clock()
FPS = 80

# ---------------- CORES ----------------

AZUL_CEU = (120, 190, 255)

VERDE = (50, 180, 70)
VERDE2 = (20, 120, 40)

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

PELE = (255, 210, 170)

VERMELHO = (220, 50, 50)

AMARELO = (255, 220, 0)

ROSA = (255, 150, 150)

AZUL_CAMISA = (40, 100, 255)

# ---------------- FONTES ----------------

fonte = pygame.font.SysFont("Arial", 40)
fonte2 = pygame.font.SysFont("Arial", 24)

# ---------------- HIGH SCORE ----------------

high_score = 0

# ---------------- REINICIAR ----------------

def reiniciar():

    return {

        "x": 460,
        "y": 430,

        "vel": 8,

        "pontos": 0,

        "game_over": False,

        "objeto": None,

        "spawn_timer": 0
    }

jogo = reiniciar()

# ---------------- LOOP ----------------

rodando = True

while rodando:

    clock.tick(FPS)

    # ---------------- EVENTOS ----------------

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_r:
                jogo = reiniciar()

    # ---------------- MOVIMENTO ----------------

    teclas = pygame.key.get_pressed()

    if not jogo["game_over"]:

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            jogo["x"] -= jogo["vel"]

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            jogo["x"] += jogo["vel"]

    # limites
    if jogo["x"] < 0:
        jogo["x"] = 0

    if jogo["x"] > LARGURA - 90:
        jogo["x"] = LARGURA - 90

    # ---------------- SPAWN DO 67 ----------------

    if not jogo["game_over"]:

        jogo["spawn_timer"] += 1

        if jogo["objeto"] is None:

            if jogo["spawn_timer"] >= 40:

                jogo["spawn_timer"] = 0

                jogo["objeto"] = {

                    "x": random.randint(
                        50,
                        LARGURA - 80
                    ),

                    "y": -50,

                    # aumenta velocidade a cada 10 pontos
                    "vel": 3 + (jogo["pontos"] // 10) * 0.5

                }

    # ---------------- FUNDO ----------------

    tela.fill(AZUL_CEU)

    # sol
    pygame.draw.circle(
        tela,
        (255, 230, 0),
        (900, 90),
        50
    )

    # grama
    pygame.draw.rect(
        tela,
        VERDE,
        (0, 500, LARGURA, 100)
    )

    pygame.draw.rect(
        tela,
        VERDE2,
        (0, 530, LARGURA, 70)
    )

    # detalhes da grama
    for i in range(0, LARGURA, 20):

        pygame.draw.line(
            tela,
            VERDE2,
            (i, 500),
            (i + 4, 488),
            2
        )

    # ---------------- MENINO ----------------

    x = jogo["x"]
    y = jogo["y"]

    # cabeça
    pygame.draw.circle(
        tela,
        PELE,
        (x + 40, y + 30),
        25
    )

    # olhos felizes
    pygame.draw.arc(
        tela,
        PRETO,
        (x + 28, y + 18, 10, 8),
        0,
        3.14,
        2
    )

    pygame.draw.arc(
        tela,
        PRETO,
        (x + 42, y + 18, 10, 8),
        0,
        3.14,
        2
    )

    # sorriso
    pygame.draw.arc(
        tela,
        PRETO,
        (x + 24, y + 35, 32, 16),
        0,
        3.14,
        3
    )

    # bochechas
    pygame.draw.circle(
        tela,
        ROSA,
        (x + 24, y + 35),
        4
    )

    pygame.draw.circle(
        tela,
        ROSA,
        (x + 56, y + 35),
        4
    )

    # corpo
    pygame.draw.rect(
        tela,
        AZUL_CAMISA,
        (x + 18, y + 55, 45, 60),
        border_radius=8
    )

    # braços
    pygame.draw.line(
        tela,
        PELE,
        (x + 18, y + 70),
        (x - 5, y + 95),
        5
    )

    pygame.draw.line(
        tela,
        PELE,
        (x + 63, y + 70),
        (x + 85, y + 95),
        5
    )

    # pernas
    pygame.draw.line(
        tela,
        PRETO,
        (x + 30, y + 115),
        (x + 20, y + 150),
        5
    )

    pygame.draw.line(
        tela,
        PRETO,
        (x + 52, y + 115),
        (x + 60, y + 150),
        5
    )

    # tênis
    pygame.draw.ellipse(
        tela,
        BRANCO,
        (x + 10, y + 145, 22, 10)
    )

    pygame.draw.ellipse(
        tela,
        BRANCO,
        (x + 52, y + 145, 22, 10)
    )

    # hitbox
    jogador_rect = pygame.Rect(
        x + 10,
        y,
        70,
        160
    )

    # ---------------- 67 CAINDO ----------------

    if jogo["objeto"] is not None:

        obj = jogo["objeto"]

        obj["y"] += obj["vel"]

        texto67 = fonte.render(
            "67",
            True,
            AMARELO
        )

        tela.blit(
            texto67,
            (obj["x"], obj["y"])
        )

        rect67 = pygame.Rect(
            obj["x"],
            obj["y"],
            50,
            40
        )

        # pegou
        if jogador_rect.colliderect(rect67):

            jogo["pontos"] += 1

            # high score
            if jogo["pontos"] > high_score:
                high_score = jogo["pontos"]

            jogo["objeto"] = None

        # perdeu
        elif obj["y"] > ALTURA:

            jogo["game_over"] = True

    # ---------------- TEXTOS ----------------

    texto_pontos = fonte.render(
        f"Pontos: {jogo['pontos']}",
        True,
        PRETO
    )

    texto_recorde = fonte.render(
        f"High Score: {high_score}",
        True,
        PRETO
    )

    tela.blit(texto_pontos, (20, 20))
    tela.blit(texto_recorde, (20, 65))

    # ---------------- GAME OVER ----------------

    if jogo["game_over"]:

        over = fonte.render(
            "GAME OVER",
            True,
            VERMELHO
        )

        restart = fonte2.render(
            "Pressione R para reiniciar",
            True,
            PRETO
        )

        tela.blit(over, (350, 220))
        tela.blit(restart, (320, 270))

    pygame.display.flip()

pygame.quit()
