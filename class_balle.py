class balle:
    def __init__(self, canvas, x, y, taille=15, vitesse=5, color="red",
                 raquette=None, liste_briques=None, on_mort=None, on_score=None):
        self.canvas = canvas
        self.taille = taille
        self.color = color
        self.raquette = raquette
        self.liste_briques = liste_briques
        self.on_mort = on_mort
        self.on_score = on_score

        self.dx = vitesse
        self.dy = -vitesse
        self.actif = True
        self.after_id = None

        self.id = self.canvas.create_oval(
            x, y, x + taille, y + taille, fill=self.color, outline="white"
        )

    def deplacer(self):
        if not self.actif:
            return

        coords = self.canvas.coords(self.id)
        if not coords:
            self.actif = False
            return

        x1, y1, x2, y2 = coords
        largeur = self.canvas.winfo_width()
        hauteur = self.canvas.winfo_height()

        if x1 <= 0:
            self.dx = abs(self.dx)
        elif x2 >= largeur:
            self.dx = -abs(self.dx)

        if y1 <= 0:
            self.dy = abs(self.dy)

        if y2 >= hauteur:
            self.actif = False
            if self.on_mort is not None:
                self.on_mort()
            return

        objets_touches = self.canvas.find_overlapping(x1, y1, x2, y2)

        if (self.raquette is not None
                and self.raquette.id in objets_touches
                and self.dy > 0):
            self.dy = -abs(self.dy)

        if self.liste_briques is not None:
            for b in self.liste_briques[:]:
                if b.id in objets_touches:
                    self.canvas.delete(b.id)
                    self.liste_briques.remove(b)

                    self.dy = -self.dy

                    if self.on_score is not None:
                        self.on_score(b)
                    break

        if not self.actif:
            return

        self.canvas.move(self.id, self.dx, self.dy)

        self.after_id = self.canvas.after(16, self.deplacer)

    def arreter(self):
        self.actif = False

        if self.after_id is not None:
            try:
                self.canvas.after_cancel(self.after_id)
            except Exception:
                pass
            self.after_id = None