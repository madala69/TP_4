"""
Auteur : Adam STIET et Alexandre ODONI
Date 8/10/2026
Objectif : créer un jeu casse birque en respectant les bonnes manières
To do : 
"""

from tkinter import *

Fenetre= Tk()
Fenetre.title("Jeu de casse brique génial !")
Fenetre.geometry('200x100+500+500')
Fenetre.mainloop()


classe brique:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color