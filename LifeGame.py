from tkinter import *
from random import choices
import time


def drawGrid(width, rows, surface):
    sizeBtwn = width // rows
    x, y = 0, 0

    grid = Canvas(surface, width=width, height=width, background='white')
    for l in range(rows):
        x += sizeBtwn
        y += sizeBtwn
        grid.create_line(x, 0, x, width)
        grid.create_line(0, y, width, y)

    grid.pack()
    return grid


def fillGrid(matrice, grid):
    sizeBtwn = 600 // len(matrice[0])
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 1:
                grid.create_rectangle(i * sizeBtwn, j * sizeBtwn, (i + 1)
                                      * sizeBtwn, (j + 1) * sizeBtwn, fill='red', tag='square')


def initMatrice(rows, pcVie):
    lifeProportion = pcVie/100
    values = [0, 1]
    weights = [1 - lifeProportion, lifeProportion]
    matrice = [[0 for _ in range(rows)] for _ in range(rows)]
    for i in range(rows):
        for j in range(rows):
            matrice[i][j] = choices(values, weights)[0]
    return matrice


def refreshGrid(grid, newMatrice, rows, surface):
    grid.delete('square')
    fillGrid(newMatrice, grid)


def initialise():
    matrice = initMatrice(taille.get(), pcVie.get())
    myGrid = drawGrid(600, taille.get(), gridFrame)
    fillGrid(matrice, myGrid)


def nombreVoisins(matrice, x, y, rows):
    result = matrice[(x - 1 + rows) % rows][(y - 1 + rows) % rows] + matrice[(x - 1 + rows) % rows][(y + rows) % rows] + \
        matrice[(x - 1 + rows) % rows][(y + 1 + rows) % rows] + matrice[(x + rows) % rows][(y + 1 + rows) % rows] + \
        matrice[(x + 1 + rows) % rows][(y + 1 + rows) % rows] + matrice[(x + 1 + rows) % rows][(y + rows) % rows] +\
        matrice[(x + 1 + rows) % rows][(y - 1 + rows) % rows] + \
        matrice[(x + rows) % rows][(y - 1 + rows) % rows]
    return result


def newGeneration(matrice, rows):
    newMatrice = matrice
    for i in range(rows):
        for j in range(rows):
            if (matrice[i][j] == 1):
                if (nombreVoisins(matrice, i, j, rows) >= 4):
                    newMatrice[i][j] = 0
                elif (nombreVoisins(matrice, i, j) <= 1):
                    newMatrice[i][j] = 0
                else:
                    newMatrice[i][j] = 1
            else:
                if (nombreVoisins(matrice, i, j) == 3):
                    newMatrice[i][j] = 1
                else:
                    newMatrice[i][j] = 0
    return newMatrice


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

button1 = Button(buttonFrame, text='Lancer', bg='#C0C0C0', fg='#22427C')
button1.pack(fill=X, side=TOP)

button2 = Button(buttonFrame, text='Arreter', bg='#C0C0C0', fg='#22427C')
button2.pack(fill=X, side=TOP)

button3 = Button(buttonFrame, text='Initialiser',
                 bg='#C0C0C0', fg='#22427C', command=initialise)
button3.pack(fill=X, side=TOP)

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
               fg='#22427C', from_=0, to=100, variable=pcVie)
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
