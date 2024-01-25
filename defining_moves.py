from board import board

def bishop_moves(coords, boardtype):
    piece_selected = boardtype[coords[0]][coords[1]]
    color = piece_selected[0]
    area = []
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
            area.append([i, collumn+num])
            if boardtype[i][collumn+num] == "--":
                possible_moves.append([i, collumn+num])
            elif boardtype[i][collumn+num][0] == color2:
                possible_moves.append([i, collumn+num])
                break
            else:
                break


    for i in range(row+1, 8):
        num = i - row
        if collumn - num < 0:
            break
        else:
            area.append([i, collumn-num])
            if boardtype[i][collumn-num] == "--":
                possible_moves.append([i, collumn-num])
            elif boardtype[i][collumn-num][0] == color2:
                possible_moves.append([i, collumn-num])
                break
            else:
                break
    for i in range(row-1, -1, -1):
        num = row - i
        if collumn - num < 0:
            break
        else:
            area.append([i, collumn-num])
            if boardtype[i][collumn-num] == "--":
                possible_moves.append([i, collumn-num])
            elif boardtype[i][collumn-num][0] == color2:
                possible_moves.append([i, collumn-num])
                break
            else:
                break
    for i in range(row-1, -1, -1):
        num = row - i
        if collumn + num > 7:
            break
        else:
            area.append([i, collumn+num])
            if boardtype[i][collumn+num] == "--":
                possible_moves.append([i, collumn+num])
            elif boardtype[i][collumn+num][0] == color2:
                possible_moves.append([i, collumn+num])
                break
            else:
                break
    return possible_moves, area


def king_moves(coords, boardtype):
    piece_selected = boardtype[coords[0]][coords[1]]
    color = piece_selected[0]
    if color == "w":
        color2 = "b"
    else:
        color2 = "w"
    possible_moves = []
    area = []
    row = coords[0]
    collumn = coords[1]
    if (row - 1) >= 0:
        if boardtype[row-1][collumn] == "--" or boardtype[row-1][collumn][0] == color2:
            possible_moves.append([row-1, collumn])
        area.append([row-1, collumn])
    if (row + 1) <= 7:
        if boardtype[row+1][collumn] == "--" or boardtype[row+1][collumn][0] == color2:
            possible_moves.append([row+1, collumn])
        area.append([row-1, collumn])
    if (collumn - 1) >= 0:
        if boardtype[row][collumn-1] == "--" or boardtype[row][collumn-1][0] == color2:
            possible_moves.append([row, collumn-1])
        area.append([row, collumn-1])
    if (collumn + 1) <= 7:
        if boardtype[row][collumn+1] == "--" or boardtype[row][collumn+1][0] == color2:
            possible_moves.append([row, collumn+1])
        area.append([row, collumn+1])
    if (row - 1) >= 0 and (collumn - 1) >= 0:
        if boardtype[row-1][collumn-1] == "--" or boardtype[row-1][collumn-1][0] == color2:
            possible_moves.append([row-1, collumn-1])
        area.append([row-1, collumn-1])
    if (row - 1) >= 0 and (collumn + 1) <= 7:
        if boardtype[row-1][collumn+1] == "--" or boardtype[row-1][collumn+1][0] == color2:
            possible_moves.append([row-1, collumn+1])
        area.append([row-1, collumn+1])
    if (row + 1) <= 7 and (collumn - 1) >= 0:
        if boardtype[row+1][collumn-1] == "--"  or boardtype[row+1][collumn-1][0] == color2:
            possible_moves.append([row+1, collumn-1])
        area.append([row+1, collumn-1])
    if (row + 1) <= 7 and (collumn + 1) <= 7:
        if boardtype[row+1][collumn+1] == "--" or boardtype[row+1][collumn+1][0] == color2:
            possible_moves.append([row+1, collumn+1])
        area.append([row+1, collumn+1])
    return possible_moves, area

def knight_moves(coords, boardtype):         
    piece_selected = boardtype[coords[0]][coords[1]]
    color = piece_selected[0]
    if color == "w":
         colour2 = "b" 
    else:
        colour2 = "w"
    
    possible_moves = []
    area = []
    row = coords[0]
    collumn = coords[1]
    if (row +2) <= 7 and (collumn-1) >= 0:
        if boardtype[row+2][collumn-1] == "--" or boardtype[row+2][collumn-1][0] == colour2:
            possible_moves.append([row+2, collumn-1])
        area.append([row+2, collumn-1])
    if (row +2) <= 7 and (collumn+1) <= 7:
        if boardtype[row+2][collumn+1] == "--" or boardtype[row+2][collumn+1][0] == colour2:
            possible_moves.append([row+2, collumn+1])
        area.append([row+2, collumn + 1])
    if (row -2) >= 0 and (collumn-1) >= 0:
        if boardtype[row-2][collumn-1] == "--" or boardtype[row-2][collumn-1][0] == colour2:
            possible_moves.append([row-2, collumn-1])
        area.append([row-2, collumn-1])
    if (row -2) >= 0 and (collumn+1) <= 7:
        if boardtype[row-2][collumn+1] == "--" or boardtype[row-2][collumn+1][0] == colour2:
            possible_moves.append([row-2, collumn+1])
        area.append([row-2, collumn+1])
    if (collumn - 2) >= 0 and (row+1) <= 7:
        if boardtype[row+1][collumn-2] == "--" or boardtype[row+1][collumn-2][0] == colour2:
            possible_moves.append([row+1, collumn-2])
        area.append([row+1, collumn-2])
    if (collumn - 2) >= 0 and (row-1) >= 0:
        if boardtype[row-1][collumn -2] == "--" or boardtype[row-1][collumn-2][0] == colour2:
            possible_moves.append([row-1, collumn-2])
        area.append([row-1, collumn - 2])
    if (collumn + 2) <= 7 and (row+1) <= 7:
        if boardtype[row+1][collumn+2] == "--" or boardtype[row+1][collumn+2][0] == colour2:
            possible_moves.append([row+1, collumn+2])
        area.append([row+1, collumn+2])
    if (collumn + 2) <= 7 and (row-1) >= 0:
        if boardtype[row-1][collumn+2] == "--" or boardtype[row-1][collumn+2][0] == colour2:
            possible_moves.append([row-1, collumn+2])
        area.append([row-1, collumn+2])
    return possible_moves, area

def pawn_moves(coords, boardtype):
    piece_selected = boardtype[coords[0]][coords[1]]
    row = coords[0]
    collumn = coords[1]
    
    possible_moves = []
    area_covered = []



    if piece_selected[0] == "w":

        if row == 6:
            if boardtype[row-1][collumn] == "--":

                possible_moves.append([row-1, collumn])
                if boardtype[row-2][collumn] == "--":
                    possible_moves.append([row-2, collumn])
        else:
            if boardtype[row-1][collumn] == "--":
                possible_moves.append([row-1, collumn])
            
        
        if collumn == 0:
            if boardtype[row-1][1][0] == "b":
                possible_moves.append([row-1, 1])
            if boardtype[row-1][1][0] != "w":
                area_covered.append([row-1, 1])
        elif collumn == 7:
            if boardtype[row-1][6][0] == "b":
                possible_moves.append([row-1, 6])
            if boardtype[row-1][6][0] != "w":
                area_covered.append([row-1, 6])
        else:
            if boardtype[row-1][collumn + 1][0] == "b":
                possible_moves.append([row-1, collumn + 1])
            if boardtype[row-1][collumn + 1][0] != "w":
                area_covered.append([row-1, collumn+1])
            if boardtype[row-1][collumn - 1][0] == "b":
                possible_moves.append([row-1, collumn-1])
            if boardtype[row-1][collumn - 1][0] != "w":
                area_covered.append([row-1, collumn -1])
            
    else:
        if row == 1:
            if boardtype[row+1][collumn] == "--":
                possible_moves.append([row+1, collumn])
                if boardtype[row+2][collumn] == "--":
                    possible_moves.append([row+2, collumn])
        else:                   
            if boardtype[row+1][collumn] == "--":
                possible_moves.append([row+1, collumn])
        if collumn == 0:
            if boardtype[row+1][1][0] == "w":
                possible_moves.append([row+1, 1])
            if boardtype[row+1][1][0] != "b":
                area_covered.append([row+1, 1])
        elif collumn == 7:
            if boardtype[row+1][6][0] == "w":
                possible_moves.append([row+1, 6])
            if boardtype[row+1][6][0] != "b":
                area_covered.append([row+1, 6])
        else:
            if boardtype[row+1][collumn+1][0] == "w":
                possible_moves.append([row+1, collumn+1])
            if boardtype[row+1][collumn+1][0] != "b":
                area_covered.append([row+1, collumn+1])
            if boardtype[row+1][collumn-1][0] == "w":
                possible_moves.append([row+1, collumn-1])
            if boardtype[row+1][collumn-1][0] != "b":
                area_covered.append([row+1, collumn-1])
    return possible_moves, area_covered


def queen_moves(coords, boardtype):
    piece_selected = boardtype[coords[0]][coords[1]]
    color = piece_selected[0]
    if color == "w":
        color2 = "b"
    else:
        color2 = "w"
    possible_moves = []
    area = []
    row = coords[0]
    collumn = coords[1]
    for i in range(row-1, -1, -1):
        area.append([i, collumn])
        if boardtype[i][collumn] == "--":
            possible_moves.append([i, collumn])
        elif boardtype[i][collumn][0] == color2:
            possible_moves.append([i, collumn])
            break
        else:
            break
    for i in range(row+1, 8):
        area.append([i, collumn])
        if boardtype[i][collumn] == "--":
            possible_moves.append([i, collumn])
        elif boardtype[i][collumn][0] == color2:
            possible_moves.append([i, collumn])
            break
        else:
            break
    for i in range(collumn+1, 8):
        area.append([row, i])
        if boardtype[row][i] == "--":
            possible_moves.append([row, i])
        elif boardtype[row][i][0] == color2:
            possible_moves.append([row, i])
            break
        else:
            break
    for i in range(collumn-1, -1, -1):
        area.append([row, i])
        if boardtype[row][i] == "--":
            possible_moves.append([row, i])
        elif boardtype[row][i][0] == color2:
            possible_moves.append([row, i])
            break
        else:
            break
    for i in range(row+1, 8):
        num = i - row
        if collumn + num > 7:
            break
        else:
            area.append([i, collumn+num])
            if boardtype[i][collumn+num] == "--":
                possible_moves.append([i, collumn+num])
            elif boardtype[i][collumn+num][0] == color2:
                possible_moves.append([i, collumn+num])
                break
            else:
                break
    for i in range(row+1, 8):
        
        num = i - row
        if collumn - num < 0:
            break
        else:
            area.append([i, collumn-num])
            if boardtype[i][collumn-num] == "--":
                possible_moves.append([i, collumn-num])
            elif boardtype[i][collumn-num][0] == color2:
                possible_moves.append([i, collumn-num])
                break
            else:
                break
    for i in range(row-1, -1, -1):
        num = row - i
        if collumn - num < 0:
            break
        else:
            area.append([i, collumn-num])
            if boardtype[i][collumn-num] == "--":
                possible_moves.append([i, collumn-num])
            elif boardtype[i][collumn-num][0] == color2:
                possible_moves.append([i, collumn-num])
                break
            else:
                break
    for i in range(row-1, -1, -1):
        num = row - i
        if collumn + num > 7:
            break
        else:
            area.append([i, collumn+num])
            if boardtype[i][collumn+num] == "--":
                possible_moves.append([i, collumn+num])
            elif boardtype[i][collumn+num][0] == color2:
                possible_moves.append([i, collumn+num])
                break
            else:
                break
    return possible_moves, area
    

def rook_moves(coords, boardtype):
    piece_selected = boardtype[coords[0]][coords[1]]
    color = piece_selected[0]
    if color == "w":
        color2 = "b"
    else:
        color2 = "w"
    possible_moves = []
    area = []
    row = coords[0]
    collumn = coords[1]
    for i in range(row-1, -1, -1):
        area.append([i, collumn])
        if boardtype[i][collumn] == "--":
            possible_moves.append([i, collumn])
        elif boardtype[i][collumn][0] == color2:
            possible_moves.append([i, collumn])
            break
        else:
            break
    for i in range(row+1, 8):
        area.append([i, collumn])
        if boardtype[i][collumn] == "--":
            possible_moves.append([i, collumn])
        elif boardtype[i][collumn][0] == color2:
            possible_moves.append([i, collumn])
            break
        else:
            break
    for i in range(collumn+1, 8):
        area.append([row, i])
        if boardtype[row][i] == "--":
            possible_moves.append([row, i])
        elif boardtype[row][i][0] == color2:
            possible_moves.append([row, i])
            break
        else:
            break
    for i in range(collumn-1, -1, -1):
        area.append([row, i])
        if boardtype[row][i] == "--":
            possible_moves.append([row, i])
        elif boardtype[row][i][0] == color2:
            possible_moves.append([row, i])
            break
        else:
            break
    if board[0][0] == "wR":
        print(area)
    return possible_moves, area
