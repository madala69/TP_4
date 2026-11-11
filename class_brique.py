class brique:
    def __init__(self, canvas, x, y, length=60, width=20, vie=1, color="green"):
        """
        Rôle de la fonction : Initialise une brique et la dessine sur le canevas.
        Entrée : canvas (Canvas) : Le canevas sur lequel la brique est dessinée.
                 x (int) : La coordonnée horizontale du coin supérieur gauche.
                 y (int) : La coordonnée verticale du coin supérieur gauche.
                 length (int) : La longueur de la brique.
                 width (int) : La hauteur de la brique.
                 vie (int) : Le nombre de points de vie de la brique.
                 color (str) : La couleur de la brique.
        Sortie : Aucune.
        """
        self.canvas = canvas
        self.vie = vie

        x1 = x
        y1 = y
        x2 = x + length
        y2 = y + width

        self.id = self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=color, outline="white"
        )
