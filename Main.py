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


def menu():
    for widget in Fenetre.winfo_children():
        widget.destroy()

    Menu = Canvas(Fenetre, width=500, height=600, background='black')
    BoutonMenu = Button(Fenetre, text='Lancer la partie', command=mainGame, relief='raised')
    TitreJeu = Label(Fenetre, text='Casse Brique', bg='maroon', fg='white', font=('Arial', 28, 'bold'))
    BoutonParametre = Button(Fenetre, text='Parametres', command=parametres, relief='raised')
    BoutonLeaderboard = Button(Fenetre, text='Leaderboard', command=meilleursScores, relief='raised')

    Menu.pack()
    Menu.create_image(300, 350, image=img)
    Menu.create_window(250, 300, window=BoutonMenu)
    Menu.create_window(250, 340, window=BoutonLeaderboard)
    Menu.create_window(250, 380, window=BoutonParametre)
    Menu.create_window(250, 200, window=TitreJeu)


def parametres():
    for widget in Fenetre.winfo_children():
        widget.destroy()

    fond = Canvas(Fenetre, width=500, height=600, background='black')
    
    # Création du curseur (Scale) relié à la variable vitesse_balle
    curseur_vitesse = Scale(
        Fenetre, from_=2, to=15, orient=HORIZONTAL, 
        label="Vitesse de la balle", variable=vitesse_balle,
        bg='black', fg='white', highlightthickness=0, length=200
    )
    BoutonMenu = Button(Fenetre, text='Retour au menu', command=menu, relief='raised')   

    fond.pack()
    fond.create_window(250, 220, window=curseur_vitesse)
    fond.create_window(250, 300, window=BoutonMenu)


def meilleursScores():
    for widget in Fenetre.winfo_children():
        widget.destroy()
    
    fond = Canvas(Fenetre, width=500, height=600, background='black')
    BoutonMenu = Button(Fenetre, text='Retour au menu', command=menu, relief='raised')   

    fond.pack()
    fond.create_window(250, 300, window=BoutonMenu)


def mainGame():
    for widget in Fenetre.winfo_children():
        widget.destroy()

    score_val = 5
    vies_val = 3

    fond = Canvas(Fenetre, width=500, height=600, background='black')        
    score = Label(Fenetre, text=f"Mon score : {score_val}", anchor='nw', bg='black', fg='green', font=('Arial', 15))
    vies = Label(Fenetre, text=f"Vies: {vies_val}", bg='black', fg='green', font=('Arial', 15))

    # 1. TRÈS IMPORTANT : Afficher le canvas AVANT Fenetre.update()
    fond.pack()
    fond.create_window(80, 20, window=score)
    fond.create_window(450, 20, window=vies)

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


menu()
Fenetre.mainloop()