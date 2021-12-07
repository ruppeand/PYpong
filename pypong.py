import pygame

COLOR_WHITE =(255, 255, 255)
COLOR_BLACK =(0, 0, 0)
COLOR_GRAY = (50, 50, 50)
COLOR_GREEN =(0, 255, 0)

X_PLAYER = 600
X_MACHINE = 30

rect_player = None
rect_machine = None

score_player = 0
score_machine = 0

ball = []

dy_player = 0

def setup_init(pyg, scr):
    global rect_machine, rect_player, score_machine, score_player, ball, dy_player

    #Mittellinie#
    scr.fill(COLOR_BLACK)
    x, y = scr.get_size()
    pyg.draw.rect(scr, COLOR_GRAY, (x/2-5, 0, 10, y))

    # Spieler Zeichnen
    rect_player = pygame.Rect(X_PLAYER, y/2-35, 10, 70)
    rect_machine = pygame.Rect(X_MACHINE, y/2-35, 10, 70)

    pyg.draw.rect(scr, COLOR_WHITE, rect_player)
    pyg.draw.rect(scr, COLOR_WHITE, rect_machine)

    #Ball, Bildmitte, Radius = 7
    pyg.draw.circle(scr, COLOR_GREEN, (x/2, y/2), 7)

    font_score1 = pygame.font.SysFont(None, 200)
    font_score2 = pygame.font.SysFont(None, 200)

    text_score1 = font_score1.render(str(score_player), False, COLOR_GRAY)
    text_score2 = font_score2.render(str(score_machine), False, COLOR_GRAY)

    scr.blit(text_score1, (120, 50))
    scr.blit(text_score2, (440, 50))

    ball = [1, 1, int(x/2), int(y/2)]

def update_game(pyg, scr):
    global rect_machine, rect_player, score_machine, score_player

    scr.fill(COLOR_BLACK)
    # Mittellinie
    x, y = scr.get_size()
    pyg.draw.rect(scr, COLOR_GRAY, (x / 2 - 5, 0, 10, y))

    # Spieler Zeichnen
    #rect_player = pygame.Rect(X_PLAYER, y / 2 - 35, 10, 70)
    #rect_machine = pygame.Rect(X_MACHINE, y / 2 - 35, 10, 70)

    #Spieler bewegen
    rect_player.move_ip(0, dy_player)

    pyg.draw.rect(scr, COLOR_WHITE, rect_player)
    pyg.draw.rect(scr, COLOR_WHITE, rect_machine)

    #Ball bewegen
    ball[2] = ball[2] + ball[0]
    ball[3] = ball[3] + ball[1]

    if ball[3] > y - 14 or ball[3] - 14 < 0:
        ball[1] = ball[1] * - 1
    if ball[2] > x - 14 or ball[2] - 14 < 0:
        ball[0] = ball[0] * - 1

    # Ball, Bildmitte, Radius = 7
    pyg.draw.circle(scr, COLOR_GREEN, (ball[2], ball[3]), 7)

    font_score1 = pygame.font.SysFont(None, 200)
    font_score2 = pygame.font.SysFont(None, 200)

    text_score1 = font_score1.render(str(score_player), False, COLOR_GRAY)
    text_score2 = font_score2.render(str(score_machine), False, COLOR_GRAY)

    scr.blit(text_score1, (120, 50))
    scr.blit(text_score2, (440, 50))

def move_player(ev):
    global dy_player

    if ev.type == pygame.KEYDOWN:
        if pygame.key.name(ev.key) == "down":
            dy_player = 4
        elif pygame.key.name(ev.key) == "up":
            dy_player = -4
    elif ev.type == pygame.KEYUP:
        if pygame.key.name(ev.key) == "down" or pygame.key.name(ev.key) == "up":
            dy_player = 0