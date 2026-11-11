class brique:
    def __init__(self, canvas, x, y, length=60, width=20, vie=1, color="green"):
        self.canvas = canvas
        self.vie = vie

        x1 = x
        y1 = y
        x2 = x + length
        y2 = y + width

        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")