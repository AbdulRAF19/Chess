from board import board
import pygame as p



def show_promotion(screen, color, IMAGES):
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
            
from checkmate import check_for_check, black_attack, white_attack


def calculate_castle(rook_moves_b_1, rook_moves_b_2, rook_moves_w_1, rook_moves_w_2, king_moves_b, king_moves_w, color):
    possible_moves = []
    if color == "w":
        if king_moves_w == 0 and check_for_check("w", board) == False and rook_moves_w_2 == 0 and ([7, 5] not in black_attack(board) and board[7][5] == "--") and ([7, 6] not in black_attack(board) and board[7][6] == "--"):
            possible_moves.append([7, 6])
        if king_moves_w == 0 and check_for_check("w", board) == False and rook_moves_w_1 == 0 and ([7, 2] not in black_attack(board) and board[7][2] == "--") and ([7, 3] not in black_attack(board) and board[7][3] == "--"):
            possible_moves.append([7, 2])
    else:
        if king_moves_b == 0 and check_for_check("b", board) == False and rook_moves_b_2 == 0 and ([0, 5] not in white_attack(board) and board[0][5] == "--") and ([0, 6] not in white_attack(board) and board[0][6] == "--"):
            possible_moves.append([0, 6])
        if king_moves_b == 0 and check_for_check("b", board) == False and rook_moves_b_1 == 0 and ([0, 2] not in white_attack(board) and board[0][2] == "--") and ([0, 3] not in white_attack(board) and board[0][3] == "--"):
            possible_moves.append([0, 2])
    return possible_moves

   
def move_castle(coords):
    if coords[0] == 0:
        color = "b"
    else:
        color = "w"
    if color == "w":
        king_coords = [7, 4]
    else:
        king_coords = [0, 4]
    board[king_coords[0]][king_coords[1]] = "--"
    if coords[1] == 6:
        board[coords[0]][6] = color + "K"
        board[coords[0]][5] = color + "R"
        board[coords[0]][7] = "--"
    else:
        board[coords[0]][2] = color + "K"
        board[coords[0]][3] = color + 'R'
        board[coords[0]][0] = "--"
    board[king_coords[0]][king_coords[1]] = "--"

def show_castle(screen, coords, IMAGES):
    collumn = 4
    if coords[0] == 0:
        row = 0
        king_color = "b"
    else:
        row = 7
        king_color = "w"
    if coords[1] == 6:
        added_col = 1
        r_coords = 7
    else:
        added_col = -1
        r_coords = 0
    colors = [p.Color("white"), p.Color("gray")]
    color = colors[((row+collumn) % 2)]
    color1 = colors[((coords[0]+r_coords)%2)]
    p.draw.rect(screen, color, p.Rect(collumn*64, row*64, 64, 64))
    screen.blit(IMAGES[king_color+"R"], p.Rect((collumn+added_col)*64, row*64, 64, 64))
    p.draw.rect(screen, color1, p.Rect(r_coords*64, row*64, 64, 64))
    screen.blit(IMAGES[king_color+"K"], p.Rect((collumn+(2*added_col))*64, row*64, 64, 64))

def show_draw(screen):
    font = p.font.Font('freesansbold.ttf', 64)
    temp = "its a draw!"
    text = font.render(temp, True, "black", "white")
 
    textRect = text.get_rect()
 
    textRect.center = (512 // 2, 512 // 2)
    screen.blit(text, textRect)


