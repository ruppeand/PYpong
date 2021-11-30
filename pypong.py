import pygame

COLOR_WHITE =(255, 255, 255)
COLOR_BLACK =(0, 0, 0)
COLOR_GRAY = (50, 50, 50)
COLOR_GREEN =(0, 255, 0)

X_PLAYER = 600
X_MACHINE = 30

rect_player = None
rect_machine = None

def setup_init(pyg, scr):
    global rect_machine, rect_player

    #Mittellinie
    x, y = scr.get_size()
    pyg.draw.rect(scr, COLOR_GRAY, (x/2-5, 0, 10, y))

    # Spieler Zeichnen
    rect_player = pygame.Rect(X_PLAYER, y/2-35, 10, 70)
    rect_machine = pygame.Rect(X_MACHINE, y/2-35, 10, 70)

    pyg.draw.rect(scr, COLOR_WHITE, rect_player)
    pyg.draw.rect(scr, COLOR_WHITE, rect_machine)

    #Ball, Bildmitte, Radius = 7
    pyg.draw.circle(scr, COLOR_WHITE, (x/2, y/2), 7)

    font_score1 = pygame.font.SysFont(None, 200)
    font_score2 = pygame.font.SysFont(None, 200)

    text_score1 = font_score1.render(str(score_player), False, COLOR_GRAY)
    text_score2 = font_score2.render(str(score_player), False, COLOR_GRAY)

    scr.blit(text_score1, (120, 50))
    scr.blit(text_score2, (440, 50))





