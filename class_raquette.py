class raquette:
    def __init__(self, canvas, x, y, length=80, width=10, color="blue"):
        self.canvas = canvas

        # Coordonnées du rectangle (coin haut-gauche et bas-droit)
        x1 = x  
        y1 = y
        x2 = x + length
        y2 = y + width

        # On dessine la raquette et on stocke son identifiant unique dans self.id
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")

        # --- NOUVEAU : Gestion de la vitesse ---
        self.vitesse_x = 0  # Vitesse actuelle (0 = à l'arrêt)
        self.vitesse = 6    # Vitesse max de la raquette (à ajuster, plus petit car mis à jour plus souvent)

        # Tkinter écoute l'appui ET le relâchement des flèches
        self.canvas.bind_all('<KeyPress-Left>', self.presser_gauche)
        self.canvas.bind_all('<KeyPress-Right>', self.presser_droite)
        self.canvas.bind_all('<KeyRelease-Left>', self.relacher_gauche)
        self.canvas.bind_all('<KeyRelease-Right>', self.relacher_droite)

        # Lancer l'animation
        self.boucle_mouvement()

    # --- Fonctions déclenchées quand on APPUIE sur la touche ---
    def presser_gauche(self, event):
        self.vitesse_x = -self.vitesse

    def presser_droite(self, event):
        self.vitesse_x = self.vitesse

    # --- Fonctions déclenchées quand on RELÂCHE la touche ---
    def relacher_gauche(self, event):
        # On arrête seulement si la raquette allait bien à gauche
        # (Pour éviter qu'elle s'arrête si on appuie déjà sur la droite)
        if self.vitesse_x == -self.vitesse:
            self.vitesse_x = 0

    def relacher_droite(self, event):
        if self.vitesse_x == self.vitesse:
            self.vitesse_x = 0

    # --- Boucle d'animation continue ---
    def boucle_mouvement(self):
        # 1. On récupère les coordonnées actuelles [x1, y1, x2, y2]
        coords = self.canvas.coords(self.id)
        
        # 2. On vérifie les collisions avec les bords gauche (0) et droit (500)
        # On ne se déplace que si on ne dépasse pas
        if self.vitesse_x < 0 and coords[0] > 0:
            self.canvas.move(self.id, self.vitesse_x, 0)
        elif self.vitesse_x > 0 and coords[2] < 500:
            self.canvas.move(self.id, self.vitesse_x, 0)
            
        # 3. La magie Tkinter : on redemande à exécuter cette fonction dans 16 millisecondes
        # 1000ms / 16ms = ~60 images par secondes (FPS)
        self.canvas.after(16, self.boucle_mouvement)