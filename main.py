import math
import pygame as p
from defining_moves import *
from checkmate import *
from math import *
from special_moves import *


def draw_cross(screen, sq):
    col = sq[1] * 64
    row = sq[0] * 64
    col1 = col + 64
    row1 = row + 64
    p.draw.line(screen, "black", (row, col), (row1, col1))
    


def show_check_mate(screen, color):
    piece = color + "K"
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == piece:
                row = i
                collumn = j
                break
    draw_cross(screen, [row, collumn])


def show_promotion(screen, color):
    if color == "w":
        row = 0
        piece = "wQ"
    else:
        row = 7
        piece = "bQ"
    colors = [p.Color("white"), p.Color("gray")]
    for col in range(0, 8):
        sq_color = colors[((row+col) % 2)]
        if board[row][col] ==  piece:
            p.draw.rect(screen, sq_color, p.Rect(col*64, row*64, 64, 64))
            screen.blit(IMAGES[piece], p.Rect(col*64, row*64, 64, 64))
            

def remove_check(screen, color):
    if color == "w":
        piece = "wK"
    else:
        piece = "bK"
    for i in range(0, 8):
        if piece in board[i]:
            row = i
            break
    collumn = board[i].index(piece)
    colors = [p.Color("white"), p.Color("gray")]
    color = colors[((row+collumn) % 2)]
    collumn = board[i].index(piece)
    p.draw.rect(screen, color, p.Rect(collumn*64, row*64, 64, 64))
    screen.blit(IMAGES[piece], p.Rect(collumn*64, row*64, 64, 64))



def show_check(screen, color):
    if color == "w":
        piece = "wK"
    else:
        piece = "bK"
    for i in range(0, 8):
        if piece in board[i]:
            row = i
            break
    
    collumn = board[i].index(piece)
    p.draw.rect(screen, "red", p.Rect(collumn*64, row*64, 64, 64))
    screen.blit(IMAGES[piece], p.Rect(collumn*64, row*64, 64, 64))

def show_available_moves(screen, coords_total):
    for i in range(0, len(coords_total)):
        row = coords_total[i][0]
        collumn = coords_total[i][1]
        row1 = (row * 64) + 32
        collumn1 = (collumn * 64) + 32
        p.draw.circle(screen, "blue", (collumn1, row1), 15)


def remove_available_moves(screen, coords_total):
    for i in range(0, len(coords_total)):
        colors = [p.Color("white"), p.Color("gray")]
        row = coords_total[i][0]
        collumn = coords_total[i][1]
        color = colors[((row+collumn) % 2)]
        p.draw.rect(screen, color, p.Rect(collumn*64, row*64, 64, 64))
        if board[row][collumn] != "--":
            piece = board[row][collumn]
            screen.blit(IMAGES[piece], p.Rect(collumn*64, row*64, 64, 64))

def move_on_board(screen, coords_orig, end_coords):
    colors = [p.Color("white"), p.Color("gray")]
    row = coords_orig[0]
    collumn = coords_orig[1]
    color = colors[((row+collumn) % 2)]
    p.draw.rect(screen, color, p.Rect(collumn*64, row*64, 64, 64))
    piece = board[coords_orig[0]][coords_orig[1]]
    row1 = end_coords[0]
    collumn1 = end_coords[1]
    color1 = colors[((row1+collumn1) % 2)]
    p.draw.rect(screen, color1, p.Rect(collumn1*64, row1*64, 64, 64))
    screen.blit(IMAGES[piece], p.Rect(collumn1*64, row1*64, 64, 64))


def piece_pick_main(piece):
    a = piece[1]
    if a == "K":
        return king_moves_exe
    elif a == "Q":
        return available_moves_queen_exe
    elif a == "p":
        return available_moves_pawn_exe
    elif a == "N":
        return available_moves_knight_exe
    elif a == "B":
        return available_moves_bishop_exe
    elif a == "R":
        return available_moves_rook_exe
    

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def LoadImages():
    pieces = ["wp", "bp", "bB", "bK", "bN", "bQ", "bR", "wB", "wK", "wN", "wQ", "wR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(piece + ".png"), (64 , 64))


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for collumn in range(DIMENSION):
            color = colors[((row+collumn)%2)]
            p.draw.rect(screen, color, p.Rect(collumn*64, row*64, 64, 64))

def drawPices(screen, board):
    for row in range(8):
        for collumn in range(8):
            piece = board[row][collumn]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(collumn*64, row*64, 64, 64))

def drawGameState(screen, board):
    drawBoard(screen)
    drawPices(screen, board)


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    LoadImages()
    check_black = False
    check_white = False
    drawGameState(screen, board)
    running = True
    whitetomove = True
    count_clicks = 0
    while running: 
        if whitetomove == True:
            color = "w"
            color1 = "b"
        else:
            color = "b"
            color1 = "w"
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                collumn = location[0]//64
                row = location[1]//64
                sqselected1 = [math.floor(row), math.floor(collumn)]                            
                if count_clicks == 0:
                    if board[sqselected1[0]][sqselected1[1]][0] == color:
                        piece = (board[sqselected1[0]][sqselected1[1]])
                        coords_piece = sqselected1
                        if color == "b":
                            if check_black == False:
                                function = piece_pick_main(piece)
                                moves = function([math.floor(row), math.floor(collumn)])
                                count_clicks += 1 
                            else:
                                moves = possible_moves_in_check([math.floor(row), math.floor(collumn)])
                        else:
                            if check_white == False:
                                function = piece_pick_main(piece)
                                moves = function([math.floor(row), math.floor(collumn)])
                                count_clicks += 1
                            else:
                                moves = possible_moves_in_check([math.floor(row), math.floor(collumn)])

                        show_available_moves(screen, moves)
                    check1 = check_for_check(color1, board)
                    if check1 == False:
                        remove_check(screen, color1)
                    

                    
                elif count_clicks == 1:
                    if board[sqselected1[0]][sqselected1[1]][0] == color:
                        count_clicks = 0
                        remove_available_moves(screen, moves)
                        running = True
                    elif sqselected1 in moves:
                        remove_available_moves(screen, moves)
                        move_on_board(screen, coords_piece, sqselected1)
                        move(coords_piece, sqselected1, board)
                        if color == "w":
                            promotion_row = 0
                        else:
                            promotion_row = 7
                            
                        for i in range(0, 8):
                            if board[promotion_row][i][1] == "p":
                                print(True)
                                print(board)
                                board[promotion_row][i] = (color + "Q")

                        show_promotion(screen, color)
                        check = check_for_check(color1, board)
                        if check == True:
                            if color1 == "b":
                                check_black = True
                            else:
                                check_white = True

                            show_check(screen, color1)
                        elif check == False:
                            remove_check(screen, color1)
                        checkmate = checkmate_check(color1)
                        if checkmate_check == True:
                            show_check_mate(screen, color1)
                        count_clicks = 0
                        if whitetomove == True:
                            whitetomove = False
                        else:
                            whitetomove = True
                        running = True
        clock.tick(MAX_FPS)
        p.display.flip()

main()
