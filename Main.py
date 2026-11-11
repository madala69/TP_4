"""
Auteur : Adam STIET et Alexandre ODONI
Date : 8/10/2026
Objectif : créer un jeu casse-brique en programmation orientée objet
To do : partie 2.2 du sujet de TP
"""

from tkinter import *
from class_brique import brique
from class_raquette import raquette
from class_balle import balle


class Pile:
    """Pile LIFO : conserve l'historique des briques détruites."""
    def __init__(self):
        self.elements = []

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()

    def est_vide(self):
        return len(self.elements) == 0


class File:
    """File FIFO : conserve les positions des briques à créer."""
    def __init__(self):
        self.elements = []

    def enfiler(self, element):
        self.elements.append(element)

    def defiler(self):
        if not self.est_vide():
            return self.elements.pop(0)

    def est_vide(self):
        return len(self.elements) == 0


Fenetre = Tk()
Fenetre.title("Jeu de casse-brique génial !")
Fenetre.resizable(False, False)
Fenetre.geometry('500x650+400+50')
Fenetre.config(cursor='heart')

img = PhotoImage(file='image.png')

vitesse_balle = IntVar(value=5)

score_val = 0
vies_val = 3
historique_briques = Pile()
liste_briques = []
ma_balle = None
ma_raquette = None
fond = None
jeu_termine = False


def arreter_animations():
    if ma_balle is not None:
        ma_balle.arreter()
    if ma_raquette is not None:
        ma_raquette.arreter()

def quitter_jeu():
    arreter_animations()
    Fenetre.destroy()

def menu():
    global jeu_termine

    arreter_animations()
    jeu_termine = True

    for widget in Fenetre.winfo_children():
        widget.destroy()

    Menu = Canvas(Fenetre, width=500, height=600, background='black')
    BoutonJouer = Button(
        Fenetre, text='Lancer la partie', command=mainGame,
        relief='raised', font=('Arial', 13)
    )
    BoutonQuitter = Button(
        Fenetre, text='Quitter le jeu', command=quitter_jeu,
        relief='raised', font=('Arial', 13)
    )
    TitreJeu = Label(
        Fenetre, text='Casse Brique', bg='maroon', fg='white',
        font=('Arial', 28, 'bold')
    )

    Menu.pack()
    if img:
        Menu.create_image(250, 350, image=img)

    Menu.create_window(250, 200, window=TitreJeu)
    Menu.create_window(250, 320, window=BoutonJouer)
    Menu.create_window(250, 400, window=BoutonQuitter)


def mainGame():
    global score_val, vies_val, fond, label_score, label_vies
    global ma_raquette, liste_briques, historique_briques, jeu_termine

    arreter_animations()

    for widget in Fenetre.winfo_children():
        widget.destroy()

    score_val = 0
    vies_val = 3
    historique_briques = Pile()
    jeu_termine = False

    barre_infos = Frame(Fenetre, bg='black')
    barre_infos.pack(fill='x')

    label_score = Label(
        barre_infos, text=f"Mon score : {score_val}",
        bg='black', fg='green', font=('Arial', 15)
    )
    label_vies = Label(
        barre_infos, text=f"Vies : {vies_val}",
        bg='black', fg='green', font=('Arial', 15)
    )
    bouton_quitter = Button(
        barre_infos, text='Quitter', command=quitter_jeu
    )

    label_score.pack(side='left', padx=15, pady=5)
    label_vies.pack(side='left', padx=15, pady=5)
    bouton_quitter.pack(side='right', padx=10, pady=3)

    fond = Canvas(Fenetre, width=500, height=600, background='black')
    fond.pack()
    Fenetre.update_idletasks()

    file_positions_briques = File()
    for ligne in range(5):
        for colonne in range(7):
            pos_x = 15 + colonne * 68
            pos_y = 60 + ligne * 28
            file_positions_briques.enfiler((pos_x, pos_y))

    liste_briques = []
    while not file_positions_briques.est_vide():
        pos_x, pos_y = file_positions_briques.defiler()
        nouvelle_brique = brique(fond, pos_x, pos_y)
        liste_briques.append(nouvelle_brique)

    ma_raquette = raquette(fond, 210, 520)

    lancer_balle()


def lancer_balle():
    global ma_balle

    if jeu_termine:
        return

    ma_balle = balle(
        fond, 240, 300,
        vitesse=vitesse_balle.get(),
        raquette=ma_raquette,
        liste_briques=liste_briques,
        on_mort=perte_vie,
        on_score=augmenter_score
    )
    ma_balle.deplacer()


def augmenter_score(brique_cassee):
    global score_val

    if jeu_termine:
        return

    score_val += 10
    label_score.config(text=f"Mon score : {score_val}")

    historique_briques.empiler(brique_cassee)

    if len(liste_briques) == 0:
        victoire()


def perte_vie():
    global vies_val

    if jeu_termine:
        return

    vies_val -= 1
    label_vies.config(text=f"Vies : {vies_val}")

    if ma_balle is not None:
        fond.delete(ma_balle.id)
        ma_balle.arreter()

    if vies_val > 0:
        lancer_balle()
    else:
        mort()


def afficher_fin(titre, message):
    fenetre_fin = Toplevel(Fenetre)
    fenetre_fin.title(titre)
    fenetre_fin.resizable(False, False)

    def retour_menu():
        fenetre_fin.destroy()
        menu()

    texte = Label(fenetre_fin, text=message, font=('Arial', 14))
    bouton_menu = Button(
        fenetre_fin, text="Retour au menu", command=retour_menu
    )
    bouton_quitter = Button(
        fenetre_fin, text="Quitter", command=quitter_jeu
    )

    texte.pack(side='top', padx=20, pady=20)
    bouton_menu.pack(side='left', padx=10, pady=10)
    bouton_quitter.pack(side='right', padx=10, pady=10)


def mort():
    global jeu_termine

    if jeu_termine:
        return

    jeu_termine = True
    arreter_animations()
    afficher_fin(
        "Vous avez perdu !",
        f"Vous avez perdu !\nScore final : {score_val}"
    )


def victoire():
    global jeu_termine

    if jeu_termine:
        return

    jeu_termine = True
    arreter_animations()
    afficher_fin(
        "Victoire !",
        f"Toutes les briques sont détruites !\nScore final : {score_val}"
    )


Fenetre.protocol("WM_DELETE_WINDOW", quitter_jeu)

menu()
Fenetre.mainloop()