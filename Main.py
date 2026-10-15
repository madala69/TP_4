"""
Auteur : Adam STIET et Alexandre ODONI
Date 8/10/2026
Objectif : créer un jeu casse birque en respectant les bonnes manières
TODO: 
"""

from tkinter import *

Fenetre= Tk()   #définition de la fenetre tkinter
Fenetre.title("Jeu de casse brique génial !")
Fenetre.resizable(False, False)   #interdiction de changer la taille de la fenetre (antibug)
Fenetre.geometry('500x600+400+50')
Fenetre.config(cursor='heart')  #forme du curseur
img = PhotoImage(file='image.png') #importation d'une image


def menu():   #menu
    Menu=Canvas(Fenetre,width=500,height=600,background='black')
    BoutonMenu=Button(Fenetre, text='Lancer la partie', command=mainGame, relief='raised')
    TitreJeu=Label(Fenetre, text='Casse Brique',bg='black', fg='green',font=('Arial', 28, 'bold'))
    BoutonParametre=Button(Fenetre, text='Parametres', command=parametres, relief='raised')

    Menu.pack()
    Menu.create_image(300,350,image=img)    #crée une image enfant du parent Menu
    Menu.create_window(250,300,window=BoutonMenu)   #crée un enfant du parent Menu
    Menu.create_window(250,340,window=BoutonParametre)
    Menu.create_window(250,200, window=TitreJeu)


def parametres():   #menu parametres
    for widget in Fenetre.winfo_children():
        widget.destroy()

    fond=Canvas(Fenetre,width=500,height=600,background='black')     
    fond.pack()

      
def mainGame():     #menu maingame
    for widget in Fenetre.winfo_children():
            widget.destroy()

    fond=Canvas(Fenetre,width=500,height=600,background='black')        
    score=Label(Fenetre, text="Mon score:", anchor='nw')
    vies=Label(Fenetre, text="Vies", bg='black', fg='green',font=('Arial', 15))

    fond.pack()
    fond.create_window(50,20, window=score)
    fond.create_window(200,100, window=vies)


menu()

Fenetre.mainloop()
