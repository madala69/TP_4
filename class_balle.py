class balle:
    def __init__(self, canvas, x, y, taille=15, vitesse=5, color="red", raquette=None, liste_briques=None, on_mort=None):
        self.canvas = canvas
        self.taille = taille
        self.color = color
        self.raquette = raquette
        self.liste_briques = liste_briques
        self.on_mort = on_mort  

        self.dx = vitesse
        self.dy = -vitesse

        self.id = self.canvas.create_oval(x, y, x + taille, y + taille, fill=self.color, outline="white")

    def deplacer(self):
            # 1. Coordonnées actuelles de la balle
            x1, y1, x2, y2 = self.canvas.coords(self.id)
            largeur = self.canvas.winfo_width()
            hauteur = self.canvas.winfo_height()

            # 2. Rebond sur les murs gauche et droite
            if x1 <= 0 or x2 >= largeur:
                self.dx = -self.dx

            # 3. Rebond sur le mur du haut
            if y1 <= 0:
                self.dy = -self.dy

            # 4. Liste de tous les éléments du Canvas qui touchent la balle
            objets_touches = self.canvas.find_overlapping(x1, y1, x2, y2)

            # 4a. Collision avec la raquette
            if self.raquette is not None and self.raquette.id in objets_touches and self.dy > 0:
                self.dy = -self.dy

            # 4b. Collision avec les briques
            if self.liste_briques is not None:
                for b in self.liste_briques[:]:  # On parcourt une copie de la liste
                    if b.id in objets_touches:
                        self.canvas.delete(b.id)       # 1. Efface la brique de l'écran
                        self.liste_briques.remove(b)   # 2. Retire la brique de la liste
                        self.dy = -self.dy             # 3. Fait rebondir la balle
                        break                          # Une seule brique cassée par rebond

            # 5. Déplacement effectif
            self.canvas.move(self.id, self.dx, self.dy)

            # 6. Appel récursif tant que la balle ne tombe pas en bas
            if y2 < hauteur:
                self.canvas.after(16, self.deplacer)
            else:
                if self.on_mort is not None:
                    self.on_mort()  # Appelle la fonction de rappel pour gérer la mort de la balle
        