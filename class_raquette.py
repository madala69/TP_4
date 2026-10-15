class raquette:
    def __init__(self, canvas, x, y, length=60, width=10, color="blue"):
        self.canvas = canvas

        # Coordonnées du rectangle (coin haut-gauche et bas-droit)
        x1 = x  
        y1 = y
        x2 = x + length
        y2 = y + width

        # On dessine la brique et on stocke son identifiant unique (id)
        self.id = self.canvas.create_rectangle( x1, y1, x2, y2, fill=color, outline="white")

    def aller_gauche(event):
        # Récupérer la position actuelle de la raquette [x1, y1, x2, y2]
        coords = canvas.coords(raquette)
        # Empêcher de sortir de l'écran à gauche (x1 > 0)
        if coords[0] > 0:
            canvas.move(raquette, -20, 0)  # Déplacement de -20 pixels sur l'axe X


    def aller_droite(event):
        coords = canvas.coords(raquette)
        # Empêcher de sortir de l'écran à droite (x2 < 400)
        if coords[2] < 400:
            canvas.move(raquette, 20, 0)  # Déplacement de +20 pixels sur l'axe X