from tkinter import *
from random import choices

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
                grid.create_rectangle(i * sizeBtwn, j * sizeBtwn, (i + 1) * sizeBtwn, (j + 1) * sizeBtwn, fill = 'red')

def initMatrice(rows, lifeProportion):
    values = [0, 1]
    weights = [1 - lifeProportion, lifeProportion]
    matrice = [[0 for _ in range(rows)] for _ in range(rows)]
    for i in range(rows):
        for j in range(rows):
            matrice[i][j] = choices(values, weights)[0]
            print(matrice[i][j])
    return matrice


def main():
    windowWidth = 800
    windowHeight = 600
    window = Tk()
    window.title('Window with canvas')
    window.geometry(f"{windowWidth}x{windowHeight}")
    gridFrame = Frame(window)
    gridFrame.pack(side = LEFT)
    currentGrid = drawGrid(windowHeight, 20, gridFrame)
    currentMatrice = initMatrice(20, 0.9)
    fillGrid(currentMatrice, currentGrid)
    window.mainloop()

if __name__ == '__main__':
    main()