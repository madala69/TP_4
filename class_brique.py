class brique:
    def __init__(self, canvas, x, y, length=60, width=20, vie=1, color="green"):
        self.canvas = canvas
        self.vie = vie

        # Coordonnées du rectangle (coin haut-gauche et bas-droit)
        x1 = x
        y1 = y
        x2 = x + length
        y2 = y + width

        # On dessine la brique et on stocke son identifiant unique (id)
        self.id = self.canvas.create_rectangle( x1, y1, x2, y2, fill=color, outline="white")
