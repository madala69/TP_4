"""
Auteur : Adam STIET et Alexandre ODONI
Date 8/10/2026
Objectif : créer un jeu casse birque en respectant les bonnes manières
TODO: Faire en classes
"""

from tkinter import *
from class_brique import brique
from class_raquette import raquette
from class_balle import balle

Fenetre = Tk()
Fenetre.title("Jeu de casse brique génial !")
Fenetre.resizable(False, False)
Fenetre.geometry('500x600+400+50')
Fenetre.config(cursor='heart')
img = PhotoImage(file='image.png')

# Variable globale Tkinter pour garder en mémoire la vitesse choisie (par défaut : 5)
vitesse_balle = IntVar(value=5)


def menu():   #menu
    for widget in Fenetre.winfo_children():
            widget.destroy()

    Menu=Canvas(Fenetre,width=500,height=600,background='black')
    BoutonMenu=Button(Fenetre, text='Lancer la partie', command=mainGame, relief='raised',  font=('Arial', 13))
    TitreJeu=Label(Fenetre, text='Casse Brique',bg='maroon', fg='white',font=('Arial', 28, 'bold'))
    BoutonParametre=Button(Fenetre, text='Parametres', command=parametres, relief='raised', font=('Arial', 13))
    BoutonLeaderboard=Button(Fenetre, text='Leaderboard', command=meilleursScores, relief='raised',  font=('Arial', 13))

    Menu.pack()
    Menu.create_image(300,350,image=img)    #crée une image enfant du parent Menu
    Menu.create_window(250,300,window=BoutonMenu)   #crée un enfant du parent Menu
    Menu.create_window(250,350,window=BoutonLeaderboard)
    Menu.create_window(250,400,window=BoutonParametre)
    Menu.create_window(250,200, window=TitreJeu)


def parametres():   #menu parametres
    for widget in Fenetre.winfo_children():
        widget.destroy()

    fond=Canvas(Fenetre,width=500,height=600,background='black')
    BoutonMenu=Button(Fenetre, text='Retour au menu', command=menu, relief='raised',  font=('Arial', 13))   
    Check = Checkbutton(Fenetre, width = 15, text='White Mode', font=('Arial', 15))
    Check2 = Checkbutton(Fenetre, width = 15, text='Option 2', font=('Arial', 15))


    fond.pack()
    fond.create_window(240,500,window=BoutonMenu)
    fond.create_window(240,150,window=Check)
    fond.create_window(240,200,window=Check2)


def meilleursScores():
    for widget in Fenetre.winfo_children():
        widget.destroy()
    
    fond=Canvas(Fenetre,width=500,height=600,background='black')
    BoutonMenu=Button(Fenetre, text='Retour au menu', command=menu, relief='raised', font=('Arial', 13))
    MeilleurScore=Label(Fenetre, text='Meilleurs Scores',bg='red', fg='white',font=('Arial', 28, 'bold'))


    fond.pack()
    fond.create_window(240,500,window=BoutonMenu)
    fond.create_window(250,100, window=MeilleurScore)


def mainGame():
    for widget in Fenetre.winfo_children():
        widget.destroy()

    score_val = 5
    vies_val = 3

    fond=Canvas(Fenetre,width=500,height=600,background='black')        
    score=Label(Fenetre, text=f"Mon score : {score_val}", anchor='nw',  bg='black', fg='green', font=('Arial', 15))
    vies=Label(Fenetre, text=f"Vies: {vies_val}", bg='black', fg='green',font=('Arial', 15))

    fond.pack()
    fond.create_window(80,20, window=score)
    fond.create_window(450,20, window=vies)

    # 2. Création des briques
    liste_briques = []
    for ligne in range(5):
        for colonne in range(7):
            pos_x = 15 + colonne * 68  
            pos_y = 60 + ligne * 28   
            nouvelle_brique = brique(fond, pos_x, pos_y)
            liste_briques.append(nouvelle_brique)

    # 3. On stocke la raquette dans une variable "ma_raquette"
    ma_raquette = raquette(fond, 100, 500)

    # 4. On met à jour la fenêtre pour que fond.winfo_width() fasse bien 500x600
    Fenetre.update()

    # 5. On crée la balle avec la vitesse du curseur (vitesse_balle.get()) et la raquette
    ma_balle = balle(
        fond, 200, 300, 
        vitesse=vitesse_balle.get(), 
        raquette=ma_raquette, 
        liste_briques=liste_briques
    )
    ma_balle.deplacer()



def mort():
    mort = Toplevel(Fenetre)
    mort.title("Vous avez perdu !")
    mort.overrideredirect(True)
    mort.geometry('+450+150')

    boutonmort = Button(mort, text="Fermer", command=mort.destroy)
    textemort= Label(mort, text='Vous etes mort!')

    textemort.pack(side='top',padx=20, pady=20)
    boutonmort.pack(side='bottom', padx=20, pady=20)


menu()
Fenetre.mainloop()