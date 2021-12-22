from tkinter import *
from random import choices


def drawGrid(width, rows):
    for widget in gridFrame.winfo_children():
        widget.destroy()
    sizeBtwn = width // rows
    x, y = 0, 0

    grid = Canvas(gridFrame, width=width, height=width, background='white')
    for l in range(rows):
        x += sizeBtwn
        y += sizeBtwn
        grid.create_line(x, 0, x, width)
        grid.create_line(0, y, width, y)

    grid.pack()
    return grid


def fillGrid(matrice, grid):
    for widget in gridFrame.winfo_children():
        widget.delete("square")
    sizeBtwn = 600 // len(matrice)
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 1:
                grid.create_rectangle(j * sizeBtwn, i * sizeBtwn, (j + 1)
                                      * sizeBtwn, (i + 1) * sizeBtwn, fill='red', tag='square')


def initMatrice(taille, pcVie):
    lifeProportion = pcVie/100
    values = [0, 1]
    weights = [1 - lifeProportion, lifeProportion]
    matrice = [[0 for _ in range(taille)] for _ in range(taille)]
    for i in range(taille):
        for j in range(taille):
            matrice[i][j] = choices(values, weights)[0]
    return matrice


def initialise():
    global running
    running = FALSE
    global matrice
    matrice = initMatrice(taille.get(), pcVie.get())
    global myGrid
    myGrid = drawGrid(600, taille.get())
    fillGrid(matrice, myGrid)
    button1['state'] = NORMAL
    button2['state'] = NORMAL


def nombreVoisins(matrice, x, y, rows):
<<<<<<< HEAD
    result = \
        matrice[(x - 1 + rows) % rows][(y - 1 + rows) % rows] + matrice[(x - 1 + rows) % rows][(y + rows) % rows] + \
        matrice[(x - 1 + rows) % rows][(y + 1 + rows) % rows] + matrice[(x + rows) % rows][(y + 1 + rows) % rows] + \
        matrice[(x + 1 + rows) % rows][(y + 1 + rows) % rows] + matrice[(x + 1 + rows) % rows][(y + rows) % rows] +\
        matrice[(x + 1 + rows) % rows][(y - 1 + rows) % rows] + \
        matrice[(x + rows) % rows][(y - 1 + rows) % rows]
=======
    result = matrice[(x - 1) % rows][(y - 1) % rows] + matrice[(x - 1) % rows][(y) % rows] + \
        matrice[(x - 1) % rows][(y + 1) % rows] + matrice[(x) % rows][(y + 1) % rows] + \
        matrice[(x + 1) % rows][(y + 1) % rows] + matrice[(x + 1) % rows][(y) % rows] +\
        matrice[(x + 1) % rows][(y - 1) % rows] + \
        matrice[(x) % rows][(y - 1) % rows]
>>>>>>> 91c7bbd1921844a1e52d39fb8014c46bbbcb81c8
    return result


def newGeneration(matrice):
    newMatrice = matrice
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if (matrice[i][j] == 1):
                if (nombreVoisins(matrice, i, j, len(matrice)) >= 4):
                    newMatrice[i][j] = 0
                elif (nombreVoisins(matrice, i, j, len(matrice)) <= 1):
                    newMatrice[i][j] = 0
                else:
                    newMatrice[i][j] = 1
            else:
                if (nombreVoisins(matrice, i, j, len(matrice)) == 3):
                    newMatrice[i][j] = 1
                else:
                    newMatrice[i][j] = 0
    return newMatrice

def easterEgg():
    matrice = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(8):
        matrice[i] = matrice [i] + [0] * 83

    for i in range(92):
        matrice.insert(0, 100*[0])


    for widget in gridFrame.winfo_children():
        widget.destroy()
    myGrid = drawGrid(600, 100, gridFrame)
    fillGrid(matrice, myGrid)
    




def start():
    global running
    running = TRUE
    run()


def run():
    if running:
        global matrice
        newMatrice = newGeneration(matrice)
        fillGrid(newMatrice, myGrid)
        matrice = newMatrice
        speed = int((1/vitesse.get())*1000)
        window.after(speed, run)


def stop():
    global running
    running = FALSE


running = TRUE
windowWidth = 800
windowHeight = 600
window = Tk()
window.title('SR01 Jeu de la vie')
window.geometry(f"{windowWidth}x{windowHeight}")

gridFrame = Frame(window)
gridFrame.pack(side=LEFT)

buttonFrame = Frame(window, width=200, height=600, bg='#DCDCDC')
buttonFrame.pack_propagate(False)
buttonFrame.pack(side=RIGHT)

button1 = Button(buttonFrame, text='Lancer', bg='#C0C0C0',
                 fg='#22427C', command=start, state=DISABLED)
button1.pack(fill=X, side=TOP)

button2 = Button(buttonFrame, text='Arreter',
                 bg='#C0C0C0', fg='#22427C', command=stop, state=DISABLED)
button2.pack(fill=X, side=TOP)

button3 = Button(buttonFrame, text='Initialiser',
                 bg='#C0C0C0', fg='#22427C', command=initialise)
button3.pack(fill=X, side=TOP)

button3.bind('<Button-3>', easterEgg)

button4 = Button(buttonFrame, text='Quitter', bg='#C0C0C0',
                 fg='#22427C', command=window.quit)
button4.pack(fill=X, side=BOTTOM)

vitesse = IntVar()

scale3 = Scale(buttonFrame, orient=HORIZONTAL,
               fg='#22427C', from_=2, to=20, variable=vitesse)
scale3.pack(side=BOTTOM)

text3 = Label(buttonFrame, text='Vitesse', fg='#22427C')
text3.pack(side=BOTTOM)

pcVie = IntVar()

scale2 = Scale(buttonFrame, orient=HORIZONTAL,
               fg='#22427C', from_=10, to=90, variable=pcVie)
scale2.pack(side=BOTTOM)

text2 = Label(buttonFrame, text='% de Vie', fg='#22427C')
text2.pack(side=BOTTOM)

taille = IntVar()

scale1 = Scale(buttonFrame, orient=HORIZONTAL,
               fg='#22427C', from_=10, to=100, variable=taille)
scale1.pack(side=BOTTOM)

text1 = Label(buttonFrame, text='Taille de la grille', fg='#22427C')
text1.pack(side=BOTTOM)


window.mainloop()
