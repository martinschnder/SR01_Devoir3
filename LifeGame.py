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
                grid.create_rectangle(i * sizeBtwn, j * sizeBtwn, (i + 1) * sizeBtwn, (j + 1) * sizeBtwn, fill = 'red', tag = 'square')
                

def initMatrice(rows, lifeProportion):
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


def nombreVoisins(matrice, x, y, rows):
    result = matrice[(x - 1 + rows) % rows][(y - 1 + rows) % rows] + matrice[(x - 1 + rows) % rows][(y + rows) % rows] + \
        matrice[(x - 1 + rows) % rows][(y + 1 + rows) % rows] + matrice[(x + rows) % rows][(y + 1 + rows) % rows] + \
            matrice[(x + 1 + rows) % rows][(y + 1 + rows) % rows] + matrice[(x + 1 + rows) % rows][(y + rows) % rows] +\
                matrice[(x + 1 + rows) % rows][(y - 1 + rows) % rows] + matrice[(x + rows) % rows][(y - 1 + rows) % rows]
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


def initialise():
    matrice = initMatrice(scale1.get(), scale2.get())
    myGrid = drawGrid(600, rows, surface)
    fillGrid(matrice, myGrid)


windowWidth = 800
windowHeight = 600
rows = 20
window = Tk()
window.title('SR01 Jeu de la vie')
window.geometry(f"{windowWidth}x{windowHeight}")

gridFrame = Frame(window)
gridFrame.pack(side=LEFT)

rightFrame = Frame(window, width=200, height=600, bg='#DCDCDC')
rightFrame.pack_propagate(False)
rightFrame.pack(side=RIGHT)

buttonFrame = Frame(rightFrame, width=200, bg='#DCDCDC')
buttonFrame.pack_propagate(False)
buttonFrame.pack(side=TOP)

textFrame = Frame(rightFrame, width=200, bg='#DCDCDC')
textFrame.pack_propagate(False)
textFrame.pack(side=BOTTOM)

text1 = Label(textFrame, text='Taille de la grille', fg='#22427C')
text1.pack()
text1.grid(row=0)

scale1 = Scale(textFrame, orient=HORIZONTAL,
                fg='#22427C', from_=10, to=100)
scale1.pack()
scale1.grid(row=1)

text2 = Label(textFrame, text='% de Vie', fg='#22427C')
text2.pack()
text2.grid(row=2)

scale2 = Scale(textFrame, orient=HORIZONTAL,
                fg='#22427C', from_=0, to=100)
scale2.pack()
scale2.grid(row=3)

text3 = Label(textFrame, text='Vitesse', fg='#22427C')
text3.pack()
text3.grid(row=4)

vitesse = IntVar()

scale3 = Scale(textFrame, orient=HORIZONTAL,
                fg='#22427C', from_=2, to=20, variable=vitesse)
scale3.pack()
scale3.grid(row=5)

button4 = Button(textFrame, text='Quitter', bg='#C0C0C0',
                    fg='#22427C', command=window.quit)
button4.pack(fill=X)
button4.grid(row=6, sticky='nesw')

button1 = Button(buttonFrame, text='Lancer', bg='#C0C0C0', fg='#22427C')
button1.pack(fill=X)
button1.grid(row=0)

button2 = Button(buttonFrame, text='Arreter', bg='#C0C0C0', fg='#22427C')
button2.pack(fill=X)
button2.grid(row=1)

button3 = Button(buttonFrame, text='Initialiser',
                    bg='#C0C0C0', fg='#22427C', command=initialise)
button3.pack(fill=X)
button3.grid(row=2)

window.mainloop()
