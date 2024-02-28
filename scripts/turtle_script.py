import turtle

turtle.setup(800, 600)
window = turtle.Screen()
t = turtle.Turtle()

def execute_commands(filename):
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for i in range(len(words)):
                if words[i] == "Tourne" and words[i+1] == "gauche":
                    degrees = int(words[i+3])
                    t.left(degrees)
                elif words[i] == "Tourne" and words[i+1] == "droite":
                    degrees = int(words[i+3])
                    t.right(degrees)
                elif words[i] == "Avance":
                    steps = int(words[i+1])
                    t.forward(steps)
                elif words[i] == "Recule":
                    steps = int(words[i+1])
                    t.backward(steps)

execute_commands("turtle")
window.mainloop()
