from tkinter import *
from random import choices


def drawGrid(width, rows):
    for widget in gridFrame.winfo_children(): # on détruit les éléments du gridFrame s'il y en a 
        widget.destroy()
    sizeBtwn = width / rows # on définit la largeur entre chaque ligne de la grille
    x, y = 0, 0 

    grid = Canvas(gridFrame, width=width, height=width, background='white') # création d'un objet de type Canvas dans le gridFrame
    for l in range(rows): #boucle dessinant des lignes à intervalles réguliers
        x += sizeBtwn
        y += sizeBtwn
        grid.create_line(x, 0, x, width) # lignes verticales 
        grid.create_line(0, y, width, y) # lignes horizontale

    grid.pack()
    return grid


def fillGrid(matrice, grid):
    for widget in gridFrame.winfo_children(): # on efface tous les carrés s'il y en a grâce à leur attribut tag
        widget.delete("square")
    sizeBtwn = 600 / len(matrice)
    for i in range(len(matrice)):
        for j in range(len(matrice)): # on parcours chaque case de la matrice
            if matrice[i][j] == 1: # si une case contient un "1", on dessine un carré rouge aux coordonées de la case 
                grid.create_rectangle(j * sizeBtwn, i * sizeBtwn, (j + 1)
                                      * sizeBtwn, (i + 1) * sizeBtwn, fill='red', tag='square')


def initMatrice(taille, pcVie):
    lifeProportion = pcVie/100
    values = [0, 1] # les deux valeurs possibles pour les cases de la matrice
    weights = [1 - lifeProportion, lifeProportion] # les probabilité associées à chaque valeur possible
    matrice = [[0 for _ in range(taille)] for _ in range(taille)] # on remplit la matrice de "0" pour l'initialiser
    for i in range(taille):
        for j in range(taille):
            matrice[i][j] = choices(values, weights)[0] # on tire une valeur au hasard dans le vecteur value selon les poids du vecteur weights
    return matrice


def initialise():
    global running
    running = FALSE # le jeu est stoppé
    global matrice
    matrice = initMatrice(taille.get(), pcVie.get()) # création de la matrice en récupérant les éléments des scale
    global myGrid
    myGrid = drawGrid(600, taille.get()) # dessin de la grille
    fillGrid(matrice, myGrid) # remplissage de la grille avec la matrice
    button0['state'] = NORMAL # activation du bouton Lancer
    button1['state'] = NORMAL # activation du bouton Arreter 


def nombreVoisins(matrice, x, y, rows):
    # le nombre de voisins corresponds à la somme des valeurs contenues dans toutes les cases voisines de la case en paramètre
    # on prends le modulo taille de la matrice des coordonnées de chaque cases pour obtenir une matrice torique 
    result = matrice[(x - 1) % rows][(y - 1) % rows] + matrice[(x - 1) % rows][y % rows] + \
        matrice[(x - 1) % rows][(y + 1) % rows] + matrice[x % rows][(y + 1) % rows] + \
        matrice[(x + 1) % rows][(y + 1) % rows] + matrice[(x + 1) % rows][y % rows] + \
        matrice[(x + 1) % rows][(y - 1) % rows] + \
        matrice[x % rows][(y - 1) % rows]
    return result


def newGeneration(matrice):
    newMatrice = [[0 for _ in range(len(matrice))] # initialisation de la nouvelle matrice de la meme taille que la précédente avec des "0"
                  for _ in range(len(matrice))]
    for i in range(len(matrice)):
        for j in range(len(matrice)): # pour chaque case, on apllique les règles du jeu de la vie selon le nombre de voisins
            if (matrice[i][j] == 1):
                if (nombreVoisins(matrice, i, j, len(matrice)) == 2 or nombreVoisins(matrice, i, j, len(matrice)) == 3):
                    newMatrice[i][j] = 1
                else:
                    newMatrice[i][j] = 0
            else:
                if (nombreVoisins(matrice, i, j, len(matrice)) == 3):
                    newMatrice[i][j] = 1
                else:
                    newMatrice[i][j] = 0
    return newMatrice


def canonplanneur():
    global running
    running = FALSE # le jeu est stoppé
    global matrice # initialisation de la matrice avec le dessin souhaité
    matrice = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
            0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(11):
        matrice[i] = matrice[i] + [0] * 62

    for i in range(89):
        matrice.append(100 * [0])

    for widget in gridFrame.winfo_children(): # on détruit les éléments qui peuvent être dans le gridFrame
        widget.destroy()
    scale1.set(100)
    global myGrid
    myGrid = drawGrid(600, 100) # dessin de la grille
    fillGrid(matrice, myGrid) # remplissage de la grille avec notre matrice
    # activation des boutons
    button0['state'] = NORMAL 
    button1['state'] = NORMAL


def galaxiekok():
    global running
    running = FALSE # le jeu est stoppé
    global matrice # initialisation de la matrice avec le dessin souhaité
    matrice = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for widget in gridFrame.winfo_children(): # on détruit les éléments qui peuvent être dans le gridFrame
        widget.destroy()
    scale1.set(15)
    global myGrid
    myGrid = drawGrid(600, 15) # dessin de la grille
    fillGrid(matrice, myGrid) # remplissage de la grille avec notre matrice
    # activation des boutons
    button0['state'] = NORMAL
    button1['state'] = NORMAL


def pulsar():
    global running
    running = FALSE # le jeu est stoppé
    global matrice # initialisation de la matrice avec le dessin souhaité
    matrice = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for widget in gridFrame.winfo_children(): # on détruit les éléments qui peuvent être dans le gridFrame
        widget.destroy()
    scale1.set(17)
    global myGrid
    myGrid = drawGrid(600, 17) # dessin de la grille
    fillGrid(matrice, myGrid) # remplissage de la grille avec notre matrice
    # activation des boutons
    button0['state'] = NORMAL
    button1['state'] = NORMAL


def penta():
    global running
    running = FALSE # le jeu est stoppé
    global matrice # initialisation de la matrice avec le dessin souhaité
    matrice = [[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]

    for i in range(8):
        matrice = [18 * [0]] + matrice

    for i in range(9):
        matrice.append(18 * [0])

    for widget in gridFrame.winfo_children(): # on détruit les éléments qui peuvent être dans le gridFrame
        widget.destroy()
    scale1.set(18)
    global myGrid
    myGrid = drawGrid(600, 18)  # dessin de la grille
    fillGrid(matrice, myGrid)# remplissage de la grille avec notre matrice
    # activation des boutons
    button0['state'] = NORMAL
    button1['state'] = NORMAL


def start(): # activation lors du clic gauche sur le bouton Lancer
    global running
    running = TRUE # le jeu est lancé
    run()


def onerun(event): # activation lors du clic droit sur le bouton Lancer
    global matrice
    newMatrice = newGeneration(matrice) # création de la matrice de la génération suivante
    fillGrid(newMatrice, myGrid) # remplissage de la grille avec la matrice
    matrice = newMatrice


def run():
    if running: # vérifie que le jeu n'a pas été arrêté
        global matrice
        newMatrice = newGeneration(matrice) # création de la matrice de la génération suivante
        fillGrid(newMatrice, myGrid) # remplissage de la grille avec la matrice
        matrice = newMatrice
        # plus valeur vitesse du scale est grande plus le temps d'attente entre deux affichages d'une nouvelle génération est faible
        speed = int((1/vitesse.get())*1000)
        window.after(speed, run) # lancement de la fonction run après speed ms


def stop(): # activation lors du clic gauche sur le bouton Arreter
    global running
    running = FALSE # empeche le lancement du rafraichissement de la fonction run


running = TRUE
windowWidth = 800 # largeur de la fenetre
windowHeight = 600 # hauteur de la fenetre
window = Tk()
window.title('SR01 Jeu de la vie') # titre de la fenetre
window.geometry(f"{windowWidth}x{windowHeight}") # dimensions de la fenetre
window.resizable(height = FALSE, width = FALSE) # empeche l'utilisateur de redimensionner sa fenetre

# nouvelle frame à gauche pour la grille
gridFrame = Frame(window)
gridFrame.pack(side=LEFT)

# nouvelle frame à droite pour les boutons
buttonFrame = Frame(window, width=200, height=600)
buttonFrame.pack_propagate(False) # les widgets dans la frame n'hériteront pas des propriétés du frame
buttonFrame.pack(side=RIGHT)

button0 = Button(buttonFrame, text='Lancer', bg='#C0C0C0',
                 fg='#22427C', command=start, state=DISABLED)
button0.pack(fill=X, side=TOP)

# clic droit sur le boutton Lancer pour afficher uniquement la génération suivante
button0.bind('<Button-3>', onerun)

button1 = Button(buttonFrame, text='Arreter', bg='#C0C0C0',
                 fg='#22427C', command=stop, state=DISABLED)
button1.pack(fill=X, side=TOP)

button2 = Button(buttonFrame, text='Initialiser',
                 bg='#C0C0C0', fg='#22427C', command=initialise)
button2.pack(fill=X, side=TOP)

button3 = Button(buttonFrame, text='Quitter', bg='#C0C0C0',
                 fg='#22427C', command=window.quit)
button3.pack(fill=X, side=BOTTOM)

# variable pour récupérer la vitesse dans le scale
vitesse = IntVar()

scale3 = Scale(buttonFrame, orient=HORIZONTAL, fg='#22427C',
               from_=2, to=20, variable=vitesse)
scale3.pack(side=BOTTOM)

text3 = Label(buttonFrame, text='Vitesse', fg='#22427C')
text3.pack(side=BOTTOM)

# variable pour récupérer le pourcentage de vie dans le scale
pcVie = IntVar()

scale2 = Scale(buttonFrame, orient=HORIZONTAL, fg='#22427C',
               from_=10, to=90, variable=pcVie)
scale2.pack(side=BOTTOM)

text2 = Label(buttonFrame, text='% de Vie', fg='#22427C')
text2.pack(side=BOTTOM)

# variable pour récupérer la taille dans le scale
taille = IntVar()

scale1 = Scale(buttonFrame, orient=HORIZONTAL, fg='#22427C',
               from_=10, to=100, variable=taille)
scale1.pack(side=BOTTOM)

text1 = Label(buttonFrame, text='Taille de la grille', fg='#22427C')
text1.pack(side=BOTTOM)

# menu pour lancer les structures connues
menu = Menu(window, tearoff=0)
menu.add_command(label="Canon à planneurs", command=canonplanneur)
menu.add_command(label="Galaxie de kok", command=galaxiekok)
menu.add_command(label="Pulsar", command=pulsar)
menu.add_command(label="Pentadécathlon", command=penta)

# affichage du menu en popup à l'endroit x, y
def do_popup(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()


# affichage du menu au clic droit à n'importe quel endroit du bouton initialiser
button2.bind("<Button-3>", do_popup)

window.mainloop() # boucle infinie permettant d'afficher la page et d'attendre un évènement
