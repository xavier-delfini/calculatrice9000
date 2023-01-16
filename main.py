from tkinter import *
from tkinter import ttk

def addition():
    value1 = float(num1.get())
    value2 = float(num2.get())
    resultat.set(float(value1 + value2))

calc = Tk()
calc.title("Calculatrice") # Titre de notre fenêtre

mainframe = ttk.Frame(calc, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
calc.columnconfigure(0, weight=1)
calc.rowconfigure(0, weight=1)

#Zone d'entrée de texte 1
num1 = StringVar()
feet_entry = ttk.Entry(mainframe, width=7,textvariable=num1)  # Zone d'entrée de text qui prendre la valeur entrée et qui la met dans la variable feet
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="+").grid(column=3, row=1, sticky=W)

num2 = StringVar()
feet_entry = ttk.Entry(mainframe, width=7,textvariable=num2)  # Zone d'entrée de text qui prendre la valeur entrée et qui la met dans la variable feet
feet_entry.grid(column=4, row=1, sticky=(W, E))


ttk.Label(mainframe, text="=").grid(column=2, row=2, sticky=W)


resultat = StringVar()
ttk.Label(mainframe, textvariable=resultat).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Calculer", command=addition).grid(column=3, row=3, sticky=W)
calc.mainloop()