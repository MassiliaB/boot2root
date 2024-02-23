import turtle

# Initialisation du module Turtle
turtle.setup(800, 600)
window = turtle.Screen()
t = turtle.Turtle()

# Fonction pour lire et exécuter les commandes du fichier texte
def execute_commands(filename):
    # Lecture du fichier
    with open(filename, 'r') as file:
        # Parcourir chaque ligne du fichier
        for line in file:
            # Diviser la ligne en mots
            words = line.split()
            # Vérifier chaque mot
            for i in range(len(words)):
                # Si le mot est "Tourne gauche"
                if words[i] == "Tourne" and words[i+1] == "gauche":
                    # Récupérer le nombre de degrés
                    degrees = int(words[i+3])
                    # Tourner à gauche du nombre de degrés spécifié
                    t.left(degrees)
                # Si le mot est "Tourne droite"
                elif words[i] == "Tourne" and words[i+1] == "droite":
                    # Récupérer le nombre de degrés
                    degrees = int(words[i+3])
                    # Tourner à droite du nombre de degrés spécifié
                    t.right(degrees)
                # Si le mot est "Avance"
                elif words[i] == "Avance":
                    # Récupérer le nombre de pas
                    steps = int(words[i+1])
                    # Avancer du nombre de pas spécifié
                    t.forward(steps)
                # Si le mot est "Recule"
                elif words[i] == "Recule":
                    # Récupérer le nombre de pas
                    steps = int(words[i+1])
                    # Reculer du nombre de pas spécifié
                    t.backward(steps)

# Appeler la fonction avec le nom du fichier en argument
execute_commands("turtle")

# Attendre un clic pour fermer la fenêtre
window.mainloop()
