"""
Auteur : Adam STIET et Alexandre ODONI
Date : 8/10/2026
Objectif : créer un jeu casse-brique en programmation orientée objet
"""

from tkinter import *
from class_brique import brique
from class_raquette import raquette
from class_balle import balle


class Pile:
    def __init__(self):
        """
        Rôle de la fonction : Initialise une pile vide.
        Entrée : Aucune.
        Sortie : Aucune
        """
        self.elements = []

    def empiler(self, element):
        """
        Rôle de la fonction : Ajoute un élément au sommet de la pile.
        Entrée : element (objet) : L'élément à ajouter dans la pile.
        Sortie : Aucune.
        """
        self.elements.append(element)

    def depiler(self):
        """
        Rôle de la fonction : Retire et renvoie le dernier élément ajouté dans la pile.
        Entrée : Aucune.
        Sortie : element (objet) : Le dernier élément de la pile, ou None si la pile est vide.
        """
        if not self.est_vide():
            return self.elements.pop()

    def est_vide(self):
        """
        Rôle de la fonction : Vérifie si la pile ne contient aucun élément.
        Entrée : Aucune.
        Sortie : bool : True si la pile est vide, False sinon.
        """
        return len(self.elements) == 0


class File:
    def __init__(self):
        """
        Rôle de la fonction : Initialise une file vide.
        Entrée : Aucune.
        Sortie : Aucune.
        """
        self.elements = []

    def enfiler(self, element):
        """
        Rôle de la fonction : Ajoute un élément à la fin de la file.
        Entrée : element (objet) : L'élément à ajouter dans la file.
        Sortie : Aucune.
        """
        self.elements.append(element)

    def defiler(self):
        """
        Rôle de la fonction : Retire et renvoie le premier élément ajouté dans la file.
        Entrée : Aucune.
        Sortie : element (objet) : Le premier élément de la file, ou None si la file est vide.
        """
        if not self.est_vide():
            return self.elements.pop(0)

    def est_vide(self):
        """
        Rôle de la fonction : Vérifie si la file ne contient aucun élément.
        Entrée : Aucune.
        Sortie : bool : True si la file est vide, False sinon.
        """
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
    """
    Rôle de la fonction : Arrête les animations de la balle et de la raquette.
    Entrée : Aucune.
    Sortie : Aucune.
    """
    if ma_balle is not None:
        ma_balle.arreter()
    if ma_raquette is not None:
        ma_raquette.arreter()


def quitter_jeu():
    """
    Rôle de la fonction : Ferme proprement la fenêtre principale du jeu.
    Entrée : Aucune.
    Sortie : Aucune.
    """
    arreter_animations()
    Fenetre.destroy()


def menu():
    """
    Rôle de la fonction : Affiche le menu principal du jeu.
    Entrée : Aucune.
    Sortie : Aucune.
    """
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
    """
    Rôle de la fonction : Initialise une partie et crée les briques, la raquette et la zone de jeu.
    Entrée : Aucune.
    Sortie : Aucune.
    """
    global score_val, vies_val, fond, label_score, label_vies
    global ma_raquette, liste_briques, historique_briques, jeu_termine

    arreter_animations()

    for widget in Fenetre.winfo_children():
        widget.destroy()

    # Initialisation des valeurs de la partie
    score_val = 0
    vies_val = 3
    historique_briques = Pile()
    jeu_termine = False

    # Barre d'informations : score, vies et bouton pour quitter
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

    # Création des briques : les positions sont placées dans une File (FIFO)
    file_positions_briques = File()
    for ligne in range(5):
        for colonne in range(7):
            pos_x = 15 + colonne * 68
            pos_y = 60 + ligne * 28
            file_positions_briques.enfiler((pos_x, pos_y))

    # On récupère les positions dans leur ordre d'arrivée pour créer les briques
    liste_briques = []
    while not file_positions_briques.est_vide():
        pos_x, pos_y = file_positions_briques.defiler()
        nouvelle_brique = brique(fond, pos_x, pos_y)
        liste_briques.append(nouvelle_brique)

    # Création de la raquette
    ma_raquette = raquette(fond, 210, 520)

    # Lancement de la première balle
    lancer_balle()


def lancer_balle():
    """
    Rôle de la fonction : Crée une balle et démarre son déplacement.
    Entrée : Aucune.
    Sortie : Aucune.
    """
    global ma_balle

    if jeu_termine:
        return

    # La balle appelle perte_vie quand elle tombe et augmenter_score
    # quand elle détruit une brique.
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
    """
    Rôle de la fonction : Ajoute des points au score et conserve la brique détruite dans la pile.
    Entrée : brique_cassee (brique) : La brique qui vient d'être détruite.
    Sortie : Aucune.
    """
    global score_val

    if jeu_termine:
        return

    # On augmente le score
    score_val += 10
    label_score.config(text=f"Mon score : {score_val}")

    # On conserve la brique détruite dans la Pile (LIFO)
    historique_briques.empiler(brique_cassee)

    # Victoire lorsque toutes les briques ont été détruites
    if len(liste_briques) == 0:
        victoire()


def perte_vie():
    """
    Rôle de la fonction : Retire une vie et relance une balle ou termine la partie.
    Entrée : Aucune.
    Sortie : Aucune.
    """
    global vies_val

    if jeu_termine:
        return

    vies_val -= 1
    label_vies.config(text=f"Vies : {vies_val}")

    # On efface visuellement la balle tombée
    if ma_balle is not None:
        fond.delete(ma_balle.id)
        ma_balle.arreter()

    if vies_val > 0:
        lancer_balle()
    else:
        mort()


def afficher_fin(titre, message):
    """
    Rôle de la fonction : Affiche le résultat de la partie dans une fenêtre secondaire.
    Entrée : titre (str) : Le titre de la fenêtre de fin.
             message (str) : Le texte affiché au joueur.
    Sortie : Aucune.
    """
    fenetre_fin = Toplevel(Fenetre)
    fenetre_fin.title(titre)
    fenetre_fin.resizable(False, False)

    def retour_menu():
        """
        Rôle de la fonction : Ferme la fenêtre de fin et affiche le menu principal.
        Entrée : Aucune.
        Sortie : Aucune.
        """
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
    """
    Rôle de la fonction : Termine la partie lorsque le joueur a perdu toutes ses vies.
    Entrée : Aucune.
    Sortie : Aucune.
    """
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
    """
    Rôle de la fonction : Termine la partie lorsque toutes les briques ont été détruites.
    Entrée : Aucune.
    Sortie : Aucune.
    """
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