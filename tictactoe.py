from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
from ia import *

window = Tk()
window.title("Tic Tac Toe !")

clicked = True
count = 0

# initialise les scores des joueurs X et O à zéro.
x_scores = 0
o_scores = 0

# affiche scores.
x_label = Label(window, text="Joueur X : " + str(x_scores), font=("Open Sans", 13))
o_label = Label(window, text="Joueur O : " + str(o_scores), font=("Open Sans", 13))
x_label.grid(row=3, column=0, columnspan=3)
o_label.grid(row=4, column=0, columnspan=3)

# désactive toutes les cases/boutons.
def disable_buttons():
    b1.configure(state = DISABLED)
    b2.configure(state = DISABLED)
    b3.configure(state = DISABLED)
    b4.configure(state = DISABLED)
    b5.configure(state = DISABLED)
    b6.configure(state = DISABLED)
    b7.configure(state = DISABLED)
    b8.configure(state = DISABLED)
    b9.configure(state = DISABLED)

# vérifie toutes les possibiltiés de jeu.
def checkifwon():
    global winner, x_scores, o_scores
    winner = False # on débute toujours le jeu avec aucun gagnant.
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.configure(bg="green")
        b2.configure(bg="green")
        b3.configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.configure(bg="green")
        b5.configure(bg="green")
        b6.configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.configure(bg="green")
        b8.configure(bg="green")
        b9.configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.configure(bg="green")
        b4.configure(bg="green")
        b7.configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.configure(bg="green")
        b5.configure(bg="green")
        b8.configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.configure(bg="green")
        b6.configure(bg="green")
        b9.configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.configure(bg="green")
        b5.configure(bg="green")
        b9.configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.configure(bg="green")
        b5.configure(bg="green")
        b7.configure(bg="green")
        winner = True
        x_scores += 1
        x_label.config(text="Joueur X : " + str(x_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur X a gagné !")
        disable_buttons()
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.configure(bg="green")
        b2.configure(bg="green")
        b3.configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.configure(bg="green")
        b5.configure(bg="green")
        b6.configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.configure(bg="green")
        b8.configure(bg="green")
        b9.configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.configure(bg="green")
        b4.configure(bg="green")
        b7.configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.configure(bg="green")
        b5.configure(bg="green")
        b8.configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.configure(bg="green")
        b6.configure(bg="green")
        b9.configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.configure(bg="green")
        b5.configure(bg="green")
        b9.configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.configure(bg="green")
        b5.configure(bg="green")
        b7.configure(bg="green")
        winner = True
        o_scores += 1
        o_label.config(text="Joueur O : " + str(o_scores))
        messagebox.showinfo("Tic Tac Toe", "Félicitation, le joueur O a gagné !")
        disable_buttons()

    # vérifier si égalité.
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
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

# création des 9 boutons/cases.
    b1 = Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace", command=lambda: click_button(b1))
    b2 = Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace", command=lambda: click_button(b2))
    b3 = Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace", command=lambda: click_button(b3))

    b4 = Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace", command=lambda: click_button(b4))
    b5 = Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace", command=lambda: click_button(b5))
    b6 = Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace", command=lambda: click_button(b6))

    b7 = Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace", command=lambda: click_button(b7))
    b8 = Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace", command=lambda: click_button(b8))
    b9 = Button(window, text=" ", font=("Open Sans", 20), height=100, width=100, bg="SystemButtonFace", command=lambda: click_button(b9))

# création de la grille de jeu.
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

# menu principal.
main_menu = Menu(window)
window.configure(menu = main_menu)

option_menu = Menu(main_menu, tearoff= False)
main_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Rejouer", command=play_again)
option_menu.add_command(label="Jouer contre IA", command=play_with_ia)

play_again()

# affiche la fenêtre du jeu.
window.mainloop()