class balle:
    def __init__(self, canvas, x, y, taille=20, vitesse=5, color="red"):
        self.canvas = canvas
        self.taille = taille
        self.color = color

        # Composantes de déplacement : non nulles = déplacement en diagonale
        self.dx = vitesse
        self.dy = -vitesse  # Part vers le haut à droite

        # Création de l'ovale sur le canvas
        self.id = self.canvas.create_oval(x, y, x + taille, y + taille, fill=self.color, outline="")

    def deplacer(self):
        # 1. Coordonnées actuelles de la balle
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        largeur = self.canvas.winfo_width()
        hauteur = self.canvas.winfo_height()

        # 2. Rebond sur les murs verticaux (gauche et droite)
        if x1 <= 0 or x2 >= largeur:
            self.dx = -self.dx  # Inverse le sens horizontal

        # 3. Rebond sur les murs horizontaux (haut et bas)
        if y1 <= 0 or y2 >= hauteur:
            self.dy = -self.dy  # Inverse le sens vertical

        # 4. Déplacement effectif
        self.canvas.move(self.id, self.dx, self.dy)

        # 5. Appel récursif toutes les ~16 ms (~60 FPS)
        self.canvas.after(16, self.deplacer)