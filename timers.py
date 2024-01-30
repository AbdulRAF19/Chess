import pygame as p

def create_white_timer(screen, time):
    font = p.font.Font('freesansbold.ttf', 64)
    text = font.render(time, True, "black", "white")
    textRect = text.get_rect()
    textRect.center = (608, 480)
    screen.blit(text, textRect)
    
def create_black_timer(screen, time):
    font = p.font.Font('freesansbold.ttf', 64)
    text = font.render(time, True, "black", "white")
    textRect = text.get_rect()
    textRect.center = (608, 32)
    screen.blit(text, textRect)

def edit_white_timer(screen, time):
    font = p.font.Font('freesansbold.ttf', 64)
    text = font.render(time, True, "black", "white")
    textRect = text.get_rect()
    textRect.center = (608, 480)
    screen.blit(text, textRect)


def edit_black_timer(screen, time):
    font = p.font.Font('freesansbold.ttf', 64)
    text = font.render(time, True, "black", "white")
    textRect = text.get_rect()
    textRect.center = (608, 32)
    screen.blit(text, textRect)

def convert_time(time):
    num = time
    mins = 0
    while num >= 60:
        mins += 1
        num -= 60
    seconds = num
    string = ""
    if mins < 10:
        string += ("0"  + str(mins) + ":")
    else:
        string += (str(mins) + ":")
    if seconds < 10:
        string += ("0" + str(seconds))
    else:
        string += (str(seconds))
    return string 





    