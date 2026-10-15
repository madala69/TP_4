"""
Auteur : Adam STIET et Alexandre ODONI
Date 8/10/2026
Objectif : créer un jeu casse birque en respectant les bonnes manières
TODO: 
"""

from tkinter import *
from class_brique import brique
from class_raquette import raquette
from class_balle import balle


Fenetre= Tk()   #définition de la fenetre tkinter
Fenetre.title("Jeu de casse brique génial !")
Fenetre.resizable(False, False)   #interdiction de changer la taille de la fenetre (antibug)
Fenetre.geometry('500x600+400+50')
Fenetre.config(cursor='heart')  #forme du curseur
img = PhotoImage(file='image.png') #importation d'une image


def menu():   #menu
    for widget in Fenetre.winfo_children():
            widget.destroy()

    Menu=Canvas(Fenetre,width=500,height=600,background='black')
    BoutonMenu=Button(Fenetre, text='Lancer la partie', command=mainGame, relief='raised')
    TitreJeu=Label(Fenetre, text='Casse Brique',bg='maroon', fg='white',font=('Arial', 28, 'bold'))
    BoutonParametre=Button(Fenetre, text='Parametres', command=parametres, relief='raised')
    BoutonLeaderboard=Button(Fenetre, text='Leaderboard', command=meilleursScores, relief='raised')

    Menu.pack()
    Menu.create_image(300,350,image=img)    #crée une image enfant du parent Menu
    Menu.create_window(250,300,window=BoutonMenu)   #crée un enfant du parent Menu
    Menu.create_window(250,340,window=BoutonLeaderboard)
    Menu.create_window(250,380,window=BoutonParametre)
    Menu.create_window(250,200, window=TitreJeu)


def parametres():   #menu parametres
    for widget in Fenetre.winfo_children():
        widget.destroy()

    fond=Canvas(Fenetre,width=500,height=600,background='black')
    BoutonMenu=Button(Fenetre, text='Retour au menu', command=menu, relief='raised')   

    fond.pack()
    fond.create_window(250,300,window=BoutonMenu)


def meilleursScores():
    for widget in Fenetre.winfo_children():
        widget.destroy()
    
    fond=Canvas(Fenetre,width=500,height=600,background='black')
    BoutonMenu=Button(Fenetre, text='Retour au menu', command=menu, relief='raised')   

    fond.pack()
    fond.create_window(250,300,window=BoutonMenu)
      
def mainGame():     #menu maingame
    for widget in Fenetre.winfo_children():
            widget.destroy()

    score=5
    vies=3

    fond=Canvas(Fenetre,width=500,height=600,background='black')        
    score=Label(Fenetre, text=f"Mon score : {score}", anchor='nw',  bg='black', fg='green', font=('Arial', 15))
    vies=Label(Fenetre, text=f"Vies: {vies}", bg='black', fg='green',font=('Arial', 15))


    liste_briques = []
    for ligne in range(5):
        for colonne in range(7):
            pos_x = 15 + colonne * 68  
            pos_y = 60 + ligne * 28   

            nouvelle_brique = brique(fond, pos_x, pos_y)
            liste_briques.append(nouvelle_brique)

    raquette(fond,100,500)
    balle(fond,123,480)

    fond.pack()
    fond.create_window(80,20, window=score)
    fond.create_window(450,20, window=vies)

menu()

Fenetre.mainloop()
