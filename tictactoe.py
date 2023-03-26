from random import randint
from tkinter import *

root = Tk()
root.title("Tic Tac Toe !")

# variables globales.
player_character = ""
ai_character = ""
positions = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
turn = 1
turns = 0
game_over = False # toujours faux quand le jeu commence.

# initialise les scores des joueurs X et O à zéro.
x_scores = 0
o_scores = 0

# affiche les scores.
x_label = Label(root, text="Player X : " + str(x_scores), font=("Open Sans", 13))
o_label = Label(root, text="Player O : " + str(o_scores), font=("Open Sans", 13))
x_label.grid(row=9, column=0, columnspan=3)
o_label.grid(row=10, column=0, columnspan=3)

Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 5, weight=1)
Grid.rowconfigure(root, 6, weight=1)
Grid.rowconfigure(root, 7, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)

def check_game_over(pos):
    global game_over
    global turns
    global x_scores
    global o_scores
    if pos[0] + pos[1] + pos[2] == 'XXX' or \
        pos[3] + pos[4] + pos[5] == 'XXX' or \
        pos[6] + pos[7] + pos[8] == 'XXX' or \
        pos[0] + pos[3] + pos[6] == 'XXX' or \
        pos[1] + pos[4] + pos[7] == 'XXX' or \
        pos[2] + pos[5] + pos[8] == 'XXX' or \
        pos[0] + pos[4] + pos[8] == 'XXX' or \
        pos[2] + pos[4] + pos[6] == 'XXX':
        game_over = True
        win_label = Label(root, text="X Wins!", font=("Open Sans", 13)).grid(row=8, column=0, columnspan = 3)
        x_scores += 1
        x_label.config(text="Player X : " + str(x_scores))
    elif pos[0] + pos[1] + pos[2] == 'OOO' or \
            pos[3] + pos[4] + pos[5] == 'OOO' or \
            pos[6] + pos[7] + pos[8] == 'OOO' or \
            pos[0] + pos[3] + pos[6] == 'OOO' or \
            pos[1] + pos[4] + pos[7] == 'OOO' or \
            pos[2] + pos[5] + pos[8] == 'OOO' or \
            pos[0] + pos[4] + pos[8] == 'OOO' or \
            pos[2] + pos[4] + pos[6] == 'OOO':
        game_over = True
        win_label = Label(root, text="O Wins!", font=("Open Sans", 13)).grid(row=8, column=0, columnspan = 3)
        o_scores += 1
        o_label.config(text="Player O : " + str(o_scores))
    else:
        check_tie(pos)
        game_over = False
    return game_over

def ai_turn():
    global turns
    global turn
    global game_over
    while turn == 0 and turns < 9 and game_over == False:
        ai_select = randint(0, 8)
        if positions[ai_select] == '-':
            positions[ai_select] = ai_character
            if 0 <= ai_select <= 2:
                r = 5
            elif 3 <= ai_select <= 5:
                r = 6
            else:
                r = 7
            if ai_select == 0 or ai_select == 3 or ai_select == 6:
                c = 0
            elif ai_select == 1 or ai_select == 4 or ai_select == 7:
                c = 1
            else:
                c = 2
            new_button = Button(root, text=positions[ai_select])
            new_button.grid(row=r, column=c, sticky='nesw')
            game_over = check_game_over(positions)

            # vérifie si la partie est terminée
            game_over = check_game_over(positions)
            if game_over:
                break

            # vérifie si égalité.
            if check_tie(positions):
                game_over = True
                showinfo("Égalité!")
                break

            turn = 1
            turns += 1

def check_tie(pos):
    global game_over
    if turns == 9 and not game_over:
        game_over = True
        messagebox.showinfo("Tic Tac Toe", "Égalité !")
        return True
    return False

def x_select():
    global player_character
    global ai_character
    player_character = "X"
    ai_character = "O"
    player_label = Label(root, text="You have selected " + player_character, font=("Open Sans", 13)).grid(row=3, column=0, columnspan = 3)
    start_button = Button(root, text="Start!", font=("Open Sans", 13), command=draw_board).grid(row=4, column=0, columnspan = 3)

def o_select():
    global player_character
    global ai_character
    player_character = "O"
    ai_character = "X"
    player_label = Label(root, text="You have selected " + player_character, font=("Open Sans", 13)).grid(row=3, column=0, columnspan = 3)
    start_button = Button(root, text="Start!", font=("Open Sans", 13), command=draw_board).grid(row=4, column=0, columnspan = 3)

def player_position(position):
    global turn
    global turns
    global positions
    global game_over
    if 0 <= position <= 2:
        r = 5
    elif 3 <= position <= 5:
        r = 6
    else:
        r = 7
    if position == 0 or position == 3 or position == 6:
        c = 0
    elif position == 1 or position == 4 or position == 7:
        c = 1
    else:
        c = 2
    if turn == 1 and turns < 9 and game_over == False:
        if positions[position] == "-":
            positions[position] = player_character
            new_button = Button(root, text=positions[position]).grid(row=r, column=c)
            game_over = check_game_over(positions)
            turn = 0
            turns += 1
            ai_turn()

def draw_board():
    global positions
    global turn
    global turns
    global game_over
    turn = 1
    turns = 0
    game_over = False
    positions = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    top_left = Button(root, text=positions[0], command=lambda: player_position(0))
    top_left.grid(row=5, column=0, sticky='nesw')
    top_mid = Button(root, text=positions[1], command=lambda: player_position(1)).grid(row=5, column=1, sticky='nesw')
    top_right = Button(root, text=positions[2], command=lambda: player_position(2)).grid(row=5, column=2, sticky='nesw')
    middle_left = Button(root, text=positions[3], command=lambda: player_position(3)).grid(row=6, column=0, sticky='nesw')
    middle_mid = Button(root, text=positions[4], command=lambda: player_position(4)).grid(row=6, column=1, sticky='nesw')
    middle_right = Button(root, text=positions[5], command=lambda: player_position(5)).grid(row=6, column=2, sticky='nesw')
    bottom_left = Button(root, text=positions[6], command=lambda: player_position(6)).grid(row=7, column=0, sticky='nesw')
    bottom_mid = Button(root, text=positions[7], command=lambda: player_position(7)).grid(row=7, column=1, sticky='nesw')
    bottom_right = Button(root, text=positions[8], command=lambda: player_position(8)).grid(row=7, column=2, sticky='nesw')
    win_label = Label(root, text="                ").grid(row=8, column=0, columnspan=3)

# définition des widgets.
main_label = Label(root, text="Welcome to Tic Tac Toe !", font=("Open Sans", 13))
player_select_label = Label(root, text="Select a character to play as.", font=("Open Sans", 13))
x_button = Button(root, text="X", font=("Open Sans", 13), command=x_select)
o_button = Button(root, text="O", font=("Open Sans", 13), command=o_select)

# dessine sur la grille de jeu.
main_label.grid(row=0, column=0, columnspan = 3)
player_select_label.grid(row=1, column=0, columnspan = 3)
x_button.grid(row=2, column=0, sticky = 'ew')
o_button.grid(row=2, column=2, sticky = 'ew')

root.mainloop()