from tkinter import *
from random import randrange

window = Tk()
window.geometry('800x600')
window.title('SR01 Jeu de la vie')

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

window.mainloop()