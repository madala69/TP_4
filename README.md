# Casse-brique

## Lancer le jeu

Exécuter le fichier `Main.py` avec Python 3 :

```bash
python Main.py
```

Le module Tkinter doit être disponible dans l'installation de Python.

## Règles du jeu

- Déplacer la raquette avec les flèches **gauche** et **droite**.
- Renvoyer la balle vers les briques pour les détruire.
- Chaque brique détruite rapporte **10 points**.
- Le joueur commence avec **3 vies**.
- Une vie est perdue lorsque la balle atteint le bas du canevas.
- La partie est gagnée lorsque toutes les briques sont détruites.
- La partie est perdue lorsque le nombre de vies atteint zéro.

## Fichiers du projet

- `Main.py` : fenêtre principale, menu, score, vies, conditions de victoire/défaite et structures de données.
- `class_brique.py` : classe `brique`, qui dessine une brique sur le canevas.
- `class_raquette.py` : classe `raquette`, qui gère le déplacement au clavier.
- `class_balle.py` : classe `balle`, qui gère le déplacement, les rebonds, les collisions et les événements de perte de vie et de score.

## Structures de données demandées

- **Liste** : `liste_briques` dans `Main.py` contient les briques encore présentes. Elle est parcourue et modifiée lors des collisions dans `class_balle.py`.
- **Pile (LIFO)** : la classe `Pile` est définie dans `Main.py`. Chaque brique détruite est ajoutée avec `empiler()` à `historique_briques`, ce qui conserve l'historique dans l'ordre LIFO. `depiler()` retire le dernier élément ajouté.
- **File (FIFO)** : la classe `File` est définie dans `Main.py`. Les positions des briques sont ajoutées avec `enfiler()`, puis récupérées avec `defiler()` pour créer la grille dans l'ordre d'arrivée.

## Dépôt Git

[Adresse du répertoire Git](https://github.com/madala69/TP_4)

## Périmètre réalisé

Cette version couvre l'interface, les commandes clavier, la balle, les rebonds, les collisions, les briques, le score, les vies et les conditions de fin de partie, ainsi que les trois structures de données demandées dans la section 2.1. Les fonctionnalités de la section 2.2 ne sont pas implémentées
