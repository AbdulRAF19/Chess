board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

def knight_moves(coords):
    piece_selected = board[coords[0]][coords[1]]
    color = piece_selected[0]
    if color == "w":
         colour2 = "b" 
    else:
        colour2 = "w"
    
    possible_moves = []
    row = coords[0]
    collumn = coords[1]
    if (row +2) <= 7 and (collumn-1) >= 0:
        if board[row+2][collumn-1] == "--" or board[row+2][collumn-1][0] == colour2:
            possible_moves.append([row+2, collumn-1])
    if (row +2) <= 7 and (collumn+1) <= 7:
        if board[row+2][collumn+1] == "--" or board[row+2][collumn+1][0] == colour2:
            possible_moves.append([row+2, collumn+1])
    if (row -2) >= 0 and (collumn-1) >= 0:
        if board[row-2][collumn-1] == "--" or board[row-2][collumn-1][0] == colour2:
            possible_moves.append([row-2, collumn-1])
    if (row -2) >= 0 and (collumn+1) <= 7:
        if board[row-2][collumn+1] == "--" or board[row-2][collumn+1][0] == colour2:
            possible_moves.append([row-2, collumn+1])
    if (collumn - 2) >= 0 and (row+1) <= 7:
        if board[row+1][collumn-2] == "--" or board[row+1][collumn-2][0] == colour2:
            possible_moves.append([row+1, collumn-2])
    if (collumn - 2) >= 0 and (row-1) >= 0:
        if board[row-1][collumn -2] == "--" or board[row-1][collumn-2][0] == colour2:
            possible_moves.append([row-1, collumn-2])
    if (collumn + 2) <= 7 and (row+1) <= 7:
        if board[row+1][collumn+2] == "--" or board[row+1][collumn+2][0] == colour2:
            possible_moves.append([row+1, collumn+2])
    if (collumn + 2) <= 7 and (row-1) >= 0:
        if board[row-1][collumn+2] == "--" or board[row-1][collumn+2][0] == colour2:
            possible_moves.append([row-1, collumn+2])
    return possible_moves, possible_moves



def king_moves(coords):
    piece_selected = board[coords[0]][coords[1]]
    color = piece_selected[0]
    if color == "w":
        color2 = "b"
    else:
        color2 = "w"
    possible_moves = []
    row = coords[0]
    collumn = coords[1]
    if (row - 1) >= 0:
        if board[row-1][collumn] == "--" or board[row-1][collumn][0] == color2:
            possible_moves.append([row-1, collumn])
    if (row + 1) <= 7:
        if board[row+1][collumn] == "--" or board[row+1][collumn][0] == color2:
            possible_moves.append([row+1, collumn])
    if (collumn - 1) >= 0:
        if board[row][collumn-1] == "--" or board[row][collumn-1][0] == color2:
            possible_moves.append([row, collumn-1])
    if (collumn + 1) <= 7:
        if board[row][collumn+1] == "--" or board[row][collumn+1][0] == color2:
            possible_moves.append([row, collumn+1])
    if (row - 1) >= 0 and (collumn - 1) >= 0:
        if board[row-1][collumn-1] == "--" or board[row-1][collumn-1][0] == color2:
            possible_moves.append([row-1, collumn-1])
    if (row - 1) >= 0 and (collumn + 1) <= 7:
        if board[row-1][collumn+1] == "--" or board[row-1][collumn+1][0] == color2:
            possible_moves.append([row-1, collumn+1])
    if (row + 1) <= 7 and (collumn - 1) >= 0:
        if board[row+1][collumn-1] == "--"  or board[row+1][collumn-1][0] == color2:
            possible_moves.append([row+1, collumn-1])
    if (row + 1) <= 7 and (collumn + 1) <= 7:
        if board[row+1][collumn+1] == "--" or board[row+1][collumn+1][0] == color2:
            possible_moves.append([row+1, collumn+1])
    return possible_moves, possible_moves


def rook_moves(coords):
    piece_selected = board[coords[0]][coords[1]]
    color = piece_selected[0]
    if color == "w":
        color2 = "b"
    else:
        color2 = "w"
    possible_moves = []
    row = coords[0]
    collumn = coords[1]
    for i in range(row-1, -1, -1):
        if board[i][collumn] == "--":
            possible_moves.append([i, collumn])
        elif board[i][collumn][0] == color2:
            possible_moves.append([i, collumn])
            break
        else:
            break
    for i in range(row+1, 8):
        if board[i][collumn] == "--":
            possible_moves.append([i, collumn])
        elif board[i][collumn][0] == color2:
            possible_moves.append([i, collumn])
            break
        else:
            break
    for i in range(collumn+1, 8):
        if board[row][i] == "--":
            possible_moves.append([row, i])
        elif board[row][i][0] == color2:
            possible_moves.append([row, i])
            break
        else:
            break
    for i in range(collumn-1, -1, -1):
        if board[row][i] == "--":
            possible_moves.append([row, i])
        elif board[row][i][0] == color2:
            possible_moves.append([row, i])
            break
        else:
            break
    return possible_moves, possible_moves





def bishop_moves(coords):
    piece_selected = board[coords[0]][coords[1]]
    color = piece_selected[0]
    if color == "w":
        color2 = "b"
    else:
        color2 = "w"
    possible_moves = []
    row = coords[0]
    collumn = coords[1]

    for i in range(row+1, 8):
        num = i - row
        if collumn + num > 7:
            break
        else:
            if board[i][collumn+num] == "--":
                possible_moves.append([i, collumn+num])
            elif board[i][collumn+num][0] == color2:
                possible_moves.append([i, collumn+num])
            else:
                break


    for i in range(row+1, 8):
        num = i - row
        if collumn - num < 0:
            break
        else:
            if board[i][collumn-num] == "--":
                possible_moves.append([i, collumn-num])
            elif board[i][collumn-num][0] == color2:
                possible_moves.append([i, collumn-num])
                break
            else:
                break
    for i in range(row-1, -1, -1):
        num = row - i
        if collumn - num < 0:
            break
        else:
            if board[i][collumn-num] == "--":
                possible_moves.append([i, collumn-num])
            elif board[i][collumn-num][0] == color2:
                possible_moves.append([i, collumn-num])
                break
            else:
                break
    for i in range(row-1, -1, -1):
        num = row - i
        if collumn + num > 7:
            break
        else:

            if board[i][collumn+num] == "--":
                possible_moves.append([i, collumn+num])
            elif board[i][collumn+num][0] == color2:
                possible_moves.append([i, collumn+num])
                break
            else:
                break
    return possible_moves, possible_moves



        


def queen_moves(coords):
    piece_selected = board[coords[0]][coords[1]]
    color = piece_selected[0]
    if color == "w":
        color2 = "b"
    else:
        color2 = "w"
    possible_moves = []
    row = coords[0]
    collumn = coords[1]
    for i in range(row-1, -1, -1):
        if board[i][collumn] == "--":
            possible_moves.append([i, collumn])
        elif board[i][collumn][0] == color2:
            possible_moves.append([i, collumn])
            break
        else:
            break
    for i in range(row+1, 8):
        if board[i][collumn] == "--":
            possible_moves.append([i, collumn])
        elif board[i][collumn][0] == color2:
            possible_moves.append([i, collumn])
            break
        else:
            break
    for i in range(collumn+1, 8):
        if board[row][i] == "--":
            possible_moves.append([row, i])
        elif board[row][i][0] == color2:
            possible_moves.append([row, i])
            break
        else:
            break
    for i in range(collumn-1, -1, -1):
        if board[row][i] == "--":
            possible_moves.append([row, i])
        elif board[row][i][0] == color2:
            possible_moves.append([row, i])
            break
        else:
            break
    for i in range(row+1, 8):
        num = i - row
        if collumn + num > 7:
            break
        else:
            if board[i][collumn+num] == "--":
                possible_moves.append([i, collumn+num])
            elif board[i][collumn+num][0] == color2:
                possible_moves.append([i, collumn+num])
                break
            else:
                break
    for i in range(row+1, 8):
        num = i - row
        if collumn - num < 0:
            break
        else:
            if board[i][collumn-num] == "--":
                possible_moves.append([i, collumn-num])
            elif board[i][collumn-num][0] == color2:
                possible_moves.append([i, collumn-num])
                break
            else:
                break
    for i in range(row-1, -1, -1):
        num = row - i
        if collumn - num < 0:
            break
        else:
            if board[i][collumn-num] == "--":
                possible_moves.append([i, collumn-num])
            elif board[i][collumn-num][0] == color2:
                possible_moves.append([i, collumn-num])
                break
            else:
                break
    for i in range(row-1, -1, -1):
        num = row - i
        if collumn + num > 7:
            break
        else:

            if board[i][collumn+num] == "--":
                possible_moves.append([i, collumn+num])
            elif board[i][collumn+num][0] == color2:
                possible_moves.append([i, collumn+num])
                break
            else:
                break
    return possible_moves, possible_moves

    
    


        

    
    
def pawn_moves(coords):
    piece_selected = board[coords[0]][coords[1]]
    row = coords[0]
    collumn = coords[1]
    
    possible_moves = []
    area_covered = []



    if piece_selected[0] == "w":

        if row == 6:
            if board[row-1][collumn] == "--":

                possible_moves.append([row-1, collumn])
            if board[row-2][collumn] == "--":
                possible_moves.append([row-2, collumn])
        else:
            if board[row-1][collumn] == "--":
                possible_moves.append([row-1, collumn])
            
        
        if collumn == 0:
            if board[row-1][1][0] == "b":
                possible_moves.append([row-1, 1])
            if board[row-1][1][0] != "w":
                area_covered.append([row-1, 1])
        elif collumn == 7:
            if board[row-1][6][0] == "b":
                possible_moves.append([row-1, 6])
            if board[row-1][6][0] != "w":
                area_covered.append([row-1, 6])
        else:
            if board[row-1][collumn + 1][0] == "b":
                possible_moves.append([row-1, collumn + 1])
            if board[row-1][collumn + 1][0] != "w":
                area_covered.append([row-1, collumn+1])
            if board[row-1][collumn - 1][0] == "b":
                possible_moves.append([row-1, collumn-1])
            if board[row-1][collumn - 1][0] != "w":
                area_covered.append([row-1, collumn -1])
            
    else:
        if row == 1:
            if board[row+1][collumn] == "--":
                possible_moves.append([row+1, collumn])
            if board[row+2][collumn] == "--":
                possible_moves.append([row+2, collumn])
        else:
            if board[row+1][collumn] == "--":
                possible_moves.append([row+1, collumn])
        if collumn == 0:
            if board[row+1][1][0] == "w":
                possible_moves.append([row+1, 1])
            if board[row+1][1][0] != "b":
                area_covered.append([row+1, 1])
        elif collumn == 7:
            if board[row+1][6][0] == "w":
                possible_moves.append([row+1, 6])
            if board[row+1][6][0] != "b":
                area_covered.append([row+1, 6])
        else:
            if board[row+1][collumn+1][0] == "w":
                possible_moves.append([row+1, collumn+1])
            if board[row+1][collumn+1][0] != "b":
                area_covered.append([row+1, collumn+1])
            if board[row+1][collumn-1][0] == "w":
                possible_moves.append([row+1, collumn-1])
            if board[row+1][collumn-1][0] != "b":
                area_covered.append([row+1, collumn-1])
    return possible_moves, area_covered