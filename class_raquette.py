class raquette:
    def __init__(self, canvas, x, y, length=80, width=10, color="blue"):
        """
        Rôle de la fonction : Initialise la raquette, ses commandes clavier et son animation.
        Entrée : canvas (Canvas) : Le canevas sur lequel la raquette est dessinée.
                 x (int) : La coordonnée horizontale du coin supérieur gauche.
                 y (int) : La coordonnée verticale du coin supérieur gauche.
                 length (int) : La longueur de la raquette.
                 width (int) : La hauteur de la raquette.
                 color (str) : La couleur de la raquette.
        Sortie : Aucune.
        """
        self.canvas = canvas

        x1 = x
        y1 = y
        x2 = x + length
        y2 = y + width

        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")

        self.vitesse_x = 0
        self.vitesse = 6
        self.actif = True
        self.after_id = None

        self.fenetre = self.canvas.winfo_toplevel()
        self.liaisons_clavier = []
        self.liaisons_clavier.append((
            '<KeyPress-Left>',
            self.fenetre.bind('<KeyPress-Left>', self.presser_gauche)
        ))
        self.liaisons_clavier.append((
            '<KeyPress-Right>',
            self.fenetre.bind('<KeyPress-Right>', self.presser_droite)
        ))
        self.liaisons_clavier.append((
            '<KeyRelease-Left>',
            self.fenetre.bind('<KeyRelease-Left>', self.relacher_gauche)
        ))
        self.liaisons_clavier.append((
            '<KeyRelease-Right>',
            self.fenetre.bind('<KeyRelease-Right>', self.relacher_droite)
        ))

        self.boucle_mouvement()

    def presser_gauche(self, event):
        """
        Rôle de la fonction : Déclenche le déplacement de la raquette vers la gauche.
        Entrée : event (Event) : L'événement clavier associé à l'appui sur la flèche gauche.
        Sortie : Aucune.
        """
        if self.actif:
            self.vitesse_x = -self.vitesse

    def presser_droite(self, event):
        """
        Rôle de la fonction : Déclenche le déplacement de la raquette vers la droite.
        Entrée : event (Event) : L'événement clavier associé à l'appui sur la flèche droite.
        Sortie : Aucune.
        """
        if self.actif:
            self.vitesse_x = self.vitesse

    def relacher_gauche(self, event):
        """
        Rôle de la fonction : Arrête le déplacement vers la gauche lorsque la touche est relâchée.
        Entrée : event (Event) : L'événement clavier associé au relâchement de la flèche gauche.
        Sortie : Aucune.
        """
        if self.vitesse_x == -self.vitesse:
            self.vitesse_x = 0

    def relacher_droite(self, event):
        """
        Rôle de la fonction : Arrête le déplacement vers la droite lorsque la touche est relâchée.
        Entrée : event (Event) : L'événement clavier associé au relâchement de la flèche droite.
        Sortie : Aucune.
        """
        if self.vitesse_x == self.vitesse:
            self.vitesse_x = 0

    def boucle_mouvement(self):
        """
        Rôle de la fonction : Déplace la raquette en respectant les limites du canevas.
        Entrée : Aucune.
        Sortie : Aucune.
        """
        if not self.actif:
            return

        coords = self.canvas.coords(self.id)
        if not coords:
            self.actif = False
            return

        largeur = self.canvas.winfo_width()

        if self.vitesse_x < 0 and coords[0] > 0:
            deplacement = max(self.vitesse_x, -coords[0])
            self.canvas.move(self.id, deplacement, 0)
        elif self.vitesse_x > 0 and coords[2] < largeur:
            deplacement = min(self.vitesse_x, largeur - coords[2])
            self.canvas.move(self.id, deplacement, 0)

        self.after_id = self.canvas.after(16, self.boucle_mouvement)

    def arreter(self):
        """
        Rôle de la fonction : Arrête le mouvement de la raquette et désactive ses raccourcis clavier.
        Entrée : Aucune.
        Sortie : Aucune.
        """
        if not self.actif:
            return

        self.actif = False
        self.vitesse_x = 0

        if self.after_id is not None:
            try:
                self.canvas.after_cancel(self.after_id)
            except Exception:
                pass
            self.after_id = None

        for touche, identifiant in self.liaisons_clavier:
            try:
                self.fenetre.unbind(touche, identifiant)
            except Exception:
                pass
