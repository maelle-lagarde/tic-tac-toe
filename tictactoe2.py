from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
import random

window = Tk()
window.title("Tic Tac Toe !")

# variables globales.
clicked = True
count = 0
x_scores = 0
o_scores = 0

# affiche scores.
x_label = Label(window, text="Joueur X : " + str(x_scores), font=("Open Sans", 13))
o_label = Label(window, text="Joueur O : " + str(o_scores), font=("Open Sans", 13))
x_label.grid(row=3, column=0, columnspan=3)
o_label.grid(row=4, column=0, columnspan=3)

# désactive toutes les cases/boutons.
def disable_buttons():
    buttons["b1"].configure(state = DISABLED)
    buttons["b2"].configure(state = DISABLED)
    buttons["b3"].configure(state = DISABLED)
    buttons["b4"].configure(state = DISABLED)
    buttons["b5"].configure(state = DISABLED)
    buttons["b6"].configure(state = DISABLED)
    buttons["b7"].configure(state = DISABLED)
    buttons["b8"].configure(state = DISABLED)
    buttons["b9"].configure(state = DISABLED)

buttons = {"b1": " ", "b2": " ", "b3": " ",
           "b4": " ", "b5": " ", "b6": " ",
           "b7": " ", "b8": " ", "b9": " "}

# +------- 1 JOUEUR ------- +

# jouer seul contre IA avec random.

def one_player():
    global clicked, count
    empty_buttons = [b for b in buttons.values() if b["text"] == " "]
    if empty_buttons:
        # choisi un emplacement de manière aléatoire avec random.
        button = random.choice(empty_buttons)
        # ajoute un symbole X ou O.
        if clicked:
            button["text"] = "O"
        else:
            button["text"] = "X"
        count += 1
        # vérifie si victoire ou égalité.
        checkifwon()
        if count == 9 and not winner:
            disable_buttons()
        else:
            clicked = not clicked

#+------- 2 JOUEURS ------- +

def two_players():
    global clicked, count, buttons
    # ajoute un symbole X ou O.
    if clicked:
        buttons["text"] = "X"
    else:
        buttons["text"] = "O"
    count += 1
    # vérifie si victoire ou égalité.
    checkifwon()
    if count == 9 and not winner:
        disable_buttons()
    else:
        clicked = not clicked

#+------- FONCTIONS DE JEU ------- +

# vérifie toutes les possibiltiés de jeu.
def checkifwon():
    global winner, x_scores, o_scores
    winner = False # on débute toujours le jeu avec aucun gagnant.
    if buttons["b1"]["text"] == "X" and buttons["b2"]["text"] == "X" and buttons["b3"]["text"] == "X":
        buttons["b1"].configure(bg="green")
        buttons["b2"].configure(bg="green")
        buttons["b3"].configure(bg="green")
        winner = True
        # on incrémente la victoire dans score.
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif buttons["b4"]["text"] == "X" and buttons["b5"]["text"] == "X" and buttons["b6"]["text"] == "X":
        buttons["b4"].configure(bg="green")
        buttons["b5"].configure(bg="green")
        buttons["b6"].configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif buttons["b7"]["text"] == "X" and buttons["b8"]["text"] == "X" and buttons["b9"]["text"] == "X":
        buttons["b7"].configure(bg="green")
        buttons["b8"].configure(bg="green")
        buttons["b9"].configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif buttons["b1"]["text"] == "X" and buttons["b4"]["text"] == "X" and buttons["b7"]["text"] == "X":
        buttons["b1"].configure(bg="green")
        buttons["b4"].configure(bg="green")
        buttons["b7"].configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif buttons["b2"]["text"] == "X" and buttons["b5"]["text"] == "X" and buttons["b8"]["text"] == "X":
        buttons["b2"].configure(bg="green")
        buttons["b5"].configure(bg="green")
        buttons["b8"].configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif buttons["b3"]["text"] == "X" and buttons["b6"]["text"] == "X" and buttons["b9"]["text"] == "X":
        buttons["b3"].configure(bg="green")
        buttons["b6"].configure(bg="green")
        buttons["b9"].configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif buttons["b1"]["text"] == "X" and buttons["b5"]["text"] == "X" and buttons["b9"]["text"] == "X":
        buttons["b1"].configure(bg="green")
        buttons["b5"].configure(bg="green")
        buttons["b9"].configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif buttons["b3"]["text"] == "X" and buttons["b5"]["text"] == "X" and buttons["b7"]["text"] == "X":
        buttons["b3"].configure(bg="green")
        buttons["b5"].configure(bg="green")
        buttons["b7"].configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif buttons["b1"]["text"] == "O" and buttons["b2"]["text"] == "O" and buttons["b3"]["text"] == "O":
        buttons["b1"].configure(bg="green")
        buttons["b2"].configure(bg="green")
        buttons["b3"].configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif buttons["b4"]["text"] == "O" and buttons["b5"]["text"] == "O" and buttons["b6"]["text"] == "O":
        buttons["b4"].configure(bg="green")
        buttons["b5"].configure(bg="green")
        buttons["b6"].configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif buttons["b7"]["text"] == "O" and buttons["b8"]["text"] == "O" and buttons["b9"]["text"] == "O":
        buttons["b7"].configure(bg="green")
        buttons["b8"].configure(bg="green")
        buttons["b9"].configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif buttons["b1"]["text"] == "O" and buttons["b4"]["text"] == "O" and buttons["b7"]["text"] == "O":
        buttons["b1"].configure(bg="green")
        buttons["b4"].configure(bg="green")
        buttons["b7"].configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif buttons["b2"]["text"] == "O" and buttons["b5"]["text"] == "O" and buttons["b8"]["text"] == "O":
        buttons["b2"].configure(bg="green")
        buttons["b5"].configure(bg="green")
        buttons["b8"].configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif buttons["b3"]["text"] == "O" and buttons["b6"]["text"] == "O" and buttons["b9"]["text"] == "O":
        buttons["b3"].configure(bg="green")
        buttons["b6"].configure(bg="green")
        buttons["b9"].configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif buttons["b1"]["text"] == "O" and buttons["b5"]["text"] == "O" and buttons["b9"]["text"] == "O":
        buttons["b1"].configure(bg="green")
        buttons["b5"].configure(bg="green")
        buttons["b9"].configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif buttons["b3"]["text"] == "O" and buttons["b5"]["text"] == "O" and buttons["b7"]["text"] == "O":
        buttons["b3"].configure(bg="green")
        buttons["b5"].configure(bg="green")
        buttons["b7"].configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()

    # vérifie si égalité.
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "Égalité !")
        disable_buttons()

def click_button(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Cette case est déjà utilisée, choisissez-en une autre !")

# permet de relancer une partie.
def play_again():
    global buttons, clicked, count
    clicked = True
    count = 0

# création des 9 boutons/cases.
    buttons = {
        "b1": Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace",
                     command=lambda: click_button(buttons["b1"])),
        "b2": Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace",
                     command=lambda: click_button(buttons["b2"])),
        "b3": Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace",
                     command=lambda: click_button(buttons["b3"])),
        "b4": Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace",
                     command=lambda: click_button(buttons["b4"])),
        "b5": Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace",
                     command=lambda: click_button(buttons["b5"])),
        "b6": Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace",
                     command=lambda: click_button(buttons["b6"])),
        "b7": Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace",
                     command=lambda: click_button(buttons["b7"])),
        "b8": Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace",
                     command=lambda: click_button(buttons["b8"])),
        "b9": Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace",
                     command=lambda: click_button(buttons["b9"]))
    }

# création de la grille de jeu.
    buttons["b1"].grid(row=0, column=0)
    buttons["b2"].grid(row=0, column=1)
    buttons["b3"].grid(row=0, column=2)

    buttons["b4"].grid(row=1, column=0)
    buttons["b5"].grid(row=1, column=1)
    buttons["b6"].grid(row=1, column=2)

    buttons["b7"].grid(row=2, column=0)
    buttons["b8"].grid(row=2, column=1)
    buttons["b9"].grid(row=2, column=2)

# menu principal.
main_menu = Menu(window)
window.configure(menu = main_menu)

option_menu = Menu(main_menu, tearoff= False)
main_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Rejouer", command=play_again)
option_menu.add_command(label="Mode un joueur", command=one_player)
option_menu.add_command(label="Mode deux joueurs", command=two_players)

play_again()

# affiche la fenêtre du jeu.
window.mainloop()