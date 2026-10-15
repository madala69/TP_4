class raquette:
    def __init__(self, canvas, x, y, length=60, width=10, color="blue"):
        self.canvas = canvas

        # Coordonnées du rectangle (coin haut-gauche et bas-droit)
        x1 = x  
        y1 = y
        x2 = x + length
        y2 = y + width

        # On dessine la raquette et on stocke son identifiant unique dans self.id
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")

        # Tkinter écoute les flèches et lance automatiquement la bonne fonction
        self.canvas.bind_all('<Left>', self.aller_gauche)
        self.canvas.bind_all('<Right>', self.aller_droite)

    def aller_gauche(self, event):
        # 1. On récupère les coordonnées actuelles [x1, y1, x2, y2] de notre raquette (self.id)
        coords = self.canvas.coords(self.id)
        
        # 2. Si le bord gauche (coords[0], c'est-à-dire x1) est supérieur à 0 :
        if coords[0] > 0:
            # 3. On décale la raquette de -20 pixels sur X (vers la gauche) et 0 sur Y
            self.canvas.move(self.id, -20, 0)

    def aller_droite(self, event):
        # 1. On récupère les coordonnées actuelles [x1, y1, x2, y2]
        coords = self.canvas.coords(self.id)
        
        # 2. Si le bord droit (coords[2], c'est-à-dire x2) est inférieur à 500 (largeur de ta fenêtre) :
        if coords[2] < 500:
            # 3. On décale la raquette de +20 pixels sur X (vers la droite) et 0 sur Y
            self.canvas.move(self.id, 20, 0)