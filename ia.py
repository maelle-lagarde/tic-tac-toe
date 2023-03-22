import random

def ia(board, signe):
    board = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    # vérifier si le signe est valide.
    if signe != "X" and signe != "O":
        return False

    # trouver un emplacement disponible.
    emplacements_disponibles = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                choice = emplacements_disponibles.append[i][j]

    # choisir un emplacement aléatoire.
    if len(emplacements_disponibles) > 0:
        emplacement_choisi = random.choice(emplacements_disponibles)
        return emplacement_choisi
    else:
        return False

def play_with_ia():
    return ia(board, signe)

def ia_move(board):
    pass

