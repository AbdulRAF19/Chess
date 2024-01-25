import pygame as p

def create_white_timer(screen):
    time = "15:00"
    font = p.font.Font('freesansbold.ttf', 64)
    text = font.render(time, True, "black", "white")
    textRect = text.get_rect()
    textRect.center = (608, 480)
    screen.blit(text, textRect)
    
def create_black_timer(screen):
    time = "15:00"
    time = "15:00"
    font = p.font.Font('freesansbold.ttf', 64)
    text = font.render(time, True, "black", "white")
    textRect = text.get_rect()
    textRect.center = (608, 32)
    screen.blit(text, textRect)
    pass

def edit_white_timer(screen, time):
    pass

def edit_black_timer(screen, time):
    pass
