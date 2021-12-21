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

def fillGrid(matrice, grid) :
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

def main():
    windowWidth = 800
    windowHeight = 600
    rows = 20
    window = Tk()
    window.title('SR01 Jeu de la vie')
    window.geometry(f"{windowWidth}x{windowHeight}")

    framebutton = Frame(window, width=200, height=600, bg='#DCDCDC')
    framebutton.pack_propagate(False)
    framebutton.pack(side = RIGHT)

    button1 = Button(framebutton, text='Lancer', bg='#C0C0C0', fg='#22427C')
    button1.pack(side = TOP, fill = X)

    button2 = Button(framebutton, text='Arreter', bg='#C0C0C0', fg='#22427C')
    button2.pack(side = TOP, fill = X)

    button3 = Button(framebutton, text='Initialiser', bg='#C0C0C0', fg='#22427C')
    button3.pack(side = TOP, fill = X)

    button4 = Button(framebutton, text='Quitter', bg='#C0C0C0', fg='#22427C')
    button4.pack(side = BOTTOM, fill = X)

    scale3 = Scale(framebutton, orient=HORIZONTAL, fg='#22427C', from_=2, to=20)
    scale3.pack(side = BOTTOM)

    text3 = Label(framebutton, text='Vitesse', fg='#22427C')
    text3.pack(side = BOTTOM)

    scale2 = Scale(framebutton, orient=HORIZONTAL, fg='#22427C', from_=0, to=100)
    scale2.pack(side = BOTTOM)

    text2 = Label(framebutton, text='% de Vie', fg='#22427C')
    text2.pack(side = BOTTOM)

    scale1 = Scale(framebutton, orient=HORIZONTAL, fg='#22427C', from_=10, to=100)
    scale1.pack(side = BOTTOM)

    text1 = Label(framebutton, text='Taille de la grille', fg='#22427C')
    text1.pack(side = BOTTOM)
    
    gridFrame = Frame(window)
    gridFrame.pack(side = LEFT)

    matrice = initMatrice(20, 0.3)
    mygrid = drawGrid(600, rows, gridFrame)
    fillGrid(matrice, mygrid)
    newMatrice = initMatrice(20, 0.7)
    refreshGrid(mygrid, newMatrice, 20, gridFrame)
    window.mainloop()

if __name__ == '__main__':
    main()