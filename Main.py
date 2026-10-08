"""
Auteur : Adam STIET et Alexandre ODONI
Date 8/10/2026
Objectif : créer un jeu casse birque en respectant les bonnes manières
To do : 
"""

from tkinter import *

Fenetre= Tk()
Fenetre.title("Jeu de casse brique génial !")
Fenetre.resizable(False, False)
Fenetre.geometry('500x600+400+50')
Fenetre.config(cursor='heart')
img = PhotoImage(file='image.png') #transparent image


def mainGame():
    for widget in Fenetre.winfo_children():
            widget.destroy()
        
    score=Label(Fenetre, text="Mon score:")
    vies=Label(Fenetre, text="Vies", fg='green')
    fond=Canvas(Fenetre,width=500,height=600,background='black')

    fond.pack()
    score.pack(side='right')
    vies.pack(side='left')


Menu=Canvas(Fenetre,width=500,height=600,background='black')
BoutonMenu=Button(Fenetre, text='Lancer la partie', command=mainGame, relief='raised')
TitreJeu=Label(Fenetre, text='Casse Brique',bg='black', fg='green',font=('Arial', 28, 'bold'))
Menu.pack()

Menu.create_image(300,350,image=img)
Menu.create_window(250,300,window=BoutonMenu)
Menu.create_window(250,200, window=TitreJeu)


Fenetre.mainloop()


# classe brique:
#     def __init__(self, length, width, color="red"):
#         self.length = length
#         self.width = width
#         self.color = color