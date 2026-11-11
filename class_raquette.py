class raquette:
    def __init__(self, canvas, x, y, length=80, width=10, color="blue"):
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
        if self.actif:
            self.vitesse_x = -self.vitesse

    def presser_droite(self, event):
        if self.actif:
            self.vitesse_x = self.vitesse

    def relacher_gauche(self, event):
        if self.vitesse_x == -self.vitesse:
            self.vitesse_x = 0

    def relacher_droite(self, event):
        if self.vitesse_x == self.vitesse:
            self.vitesse_x = 0

    def boucle_mouvement(self):
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