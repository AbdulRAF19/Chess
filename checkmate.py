from defining_moves import *

def create_board_copy():
    boardcopy = []
    for r in range(0, 8):
        temp_row = []
        for i in range(0, 8):
            temp_row.append(board[r][i])
        boardcopy.append(temp_row)
    return boardcopy

def piece_pick(coords):
    piece_selected = board[coords[0]][coords[1]]
    if piece_selected[1] == "p":
        return pawn_moves(coords)
    elif piece_selected[1] == "R":
        return rook_moves(coords)
    elif piece_selected[1] == "B":
        return bishop_moves(coords)
    elif piece_selected[1] == "Q":
        return queen_moves(coords)
    elif piece_selected[1] == "K":
        return king_moves(coords)
    elif piece_selected[1] == "N":
        return knight_moves(coords)
    
def white_attack(boardused):
    final_w_area = []
    all_white_area = []
    for i in range(0, 8):
        for j in range(0, 8):
            if "w" in boardused[i][j]:
                all_white_area += piece_pick([i, j])[1]
    for i in range(0, len(all_white_area)):
        if all_white_area[i] not in final_w_area:
            final_w_area.append(all_white_area[i])
    return final_w_area

#return total area covered for check
def black_attack(boardused):
    final_b_area = []
    all_black_area = []
    for i in range(0, 8):
        for j in range(0, 8):
            if "b" in boardused[i][j]:
                all_black_area += piece_pick([i, j])[1]
    for i in range(0, len(all_black_area)):
        if all_black_area[i] not in final_b_area:
            final_b_area.append(all_black_area[i])
    return final_b_area
#return total area covered for check

def king_moves_exe(coords):
    king_selected = board[coords[0]][coords[1]]
    row = coords[0]
    collumn = coords[1]
    real_king_moves = []
    king_moves_main = king_moves(coords)[0]
    if king_selected[0] == "w":
        
        area = black_attack(board)
        for i in range(0, len(king_moves_main)):
            if king_moves_main[i] not in area:
                real_king_moves.append(king_moves_main[i])
    else:
        area = white_attack(board)
        for i in range(0, len(king_moves_main)):
            if king_moves_main[i] not in area:
                real_king_moves.append(king_moves_main[i])
    return real_king_moves

#uses the area covered to work out where the king can go becasue the king cant move into check

def check_for_check(color, board_used):
    if color == "w":
        piece = "wK"
    else:
        piece = "bK"
    for i in range(0, 8):
        if piece in board_used[i]:
            row = i
            break
    for i in range(0, 8):
        if piece == board_used[row][i]:
            collumn = i
            break
    if color == "w":
        area = black_attack(board_used)
        if [row, collumn] in area:
            return True
        else:
            return False
    else:
        area = white_attack(board_used)
        if [row, collumn] in area:
            return True
        else:
            return False

#this will check if the color (parameter) king is in check

def move(coords, endlocation, boardused):
    piece_selected = boardused[coords[0]][coords[1]]
    row = coords[0]
    collumn = coords[1]
    row1 = endlocation[0]
    collumn1 = endlocation[1]
    boardused[row][collumn] = "--"
    boardused[row1][collumn1] = piece_selected

#will move a piece to a location

def available_moves_exe(coords, function):
    piece_selected = board[coords[0]][coords[1]]
    color1 = piece_selected[0]
    moves = function(coords)[0]
    real_available_moves = []
    for i in range(0, len(moves)):
        boardcopy = create_board_copy()
        move(coords, moves[i], boardcopy)
        if check_for_check(color1, boardcopy) == False:
            real_available_moves.append(moves[i])
    return real_available_moves

#in chess you cant move to reveal check so this cheks if a moves does not cause check so is possible 
def available_moves_bishop_exe(coords):
    return available_moves_exe(coords, bishop_moves)


def available_moves_pawn_exe(coords):
    return available_moves_exe(coords, pawn_moves)

def available_moves_rook_exe(coords):
    return available_moves_exe(coords, rook_moves)



def available_moves_knight_exe(coords):
    return available_moves_exe(coords, knight_moves)
def available_moves_queen_exe(coords):
    return available_moves_exe(coords, queen_moves)

def possible_moves_in_check(coords):
    possible_moves = []
    piece_selected = board[coords[0]][coords[1]]
    color = piece_selected[0]
    if piece_selected[1] == "p":
        temporary_moves = available_moves_pawn_exe(coords)
    elif piece_selected[1] == "Q":
        temporary_moves = available_moves_queen_exe(coords)
    elif piece_selected[1] == "B":
        temporary_moves = available_moves_bishop_exe(coords)
    elif piece_selected[1] == "R":
        temporary_moves = available_moves_rook_exe(coords)
    elif piece_selected[1] == "N":
        temporary_moves = available_moves_knight_exe(coords)
    elif piece_selected[1] == "K":
        temporary_moves = king_moves_exe(coords)
    for i in range(0, len(temporary_moves)):
        boardcopy = create_board_copy()
        move(coords, temporary_moves[i], boardcopy)
        if check_for_check(color, boardcopy) == False:
            possible_moves.append(temporary_moves[i])
    return possible_moves



def checkmate_check(color):

    if color == "w":
        piece = "wK"
    else:
        piece = "bK"
    
    for i in range(0, 8):
        for j in range(0, 8):
            if piece == board[i][j]:
                coords = [i, j]
    total_possible_moves = []
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j][0] == color and (board[i][j][1] != "K"):
                total_possible_moves.append(possible_moves_in_check([i, j]))


    if (check_for_check(color, board) == True) and (len(king_moves_exe(coords)) == 0) and (len(total_possible_moves) == 0):
        return True
    else:
        return False

