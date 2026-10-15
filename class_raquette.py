class raquette:
    def __init__(self, length, width, color="blue"):
        self.length = length
        self.width = width
        self.color = color
    def deplacer(self, dx, dy):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        largeur = self.canvas.winfo_width()
        hauteur = self.canvas.winfo_height()

        # if x1 + dx < 0:
        #     dx = -x1
        # elif x2 + dx > largeur:
        #     dx = largeur - x2

        # if y1 + dy < 0:
        #     dy = -y1
        # elif y2 + dy > hauteur:
        #     dy = hauteur - y2

        self.canvas.move(self.id, dx, dy)