from tkinter import *
from tkinter import ttk


"""def addition():
    value1 = float(num1.get())
    value2 = float(num2.get())
    result.set(float(value1 + value2))
"""

calc = Tk()
calc.title("Calculatrice")

# Parent et cadre principal de notre interface
affichage = ttk.Frame(calc, padding="10 10 5 5")
affichage.grid(column=0, row=0, sticky=(W, E, S))
calc.columnconfigure(0, weight=1)
calc.rowconfigure(0, weight=1)

boutons = ttk.Frame(calc, padding="1 1 1 1")
boutons.grid(column=0, row=1, sticky=(W, E, S))
calc.columnconfigure(0, weight=1)
calc.rowconfigure(0, weight=1)
value = 12
ttk.Label(affichage,text=value).grid(column=0, row=0)
ttk.Button(boutons, text="7").grid(column=0, row=0)
ttk.Button(boutons, text="8").grid(column=1, row=0)
ttk.Button(boutons, text="9").grid(column=2, row=0)
ttk.Button(boutons, text="÷").grid(column=3, row=0)
ttk.Button(boutons, text="6").grid(column=0, row=1)
ttk.Button(boutons, text="5").grid(column=1, row=1)
ttk.Button(boutons, text="4").grid(column=2, row=1)
ttk.Button(boutons, text="X").grid(column=3, row=1)
ttk.Button(boutons, text="3").grid(column=0, row=2)
ttk.Button(boutons, text="2").grid(column=1, row=2)
ttk.Button(boutons, text="1").grid(column=2, row=2)
ttk.Button(boutons, text="-").grid(column=3, row=2)
ttk.Button(boutons, text="+/-").grid(column=0, row=3)
ttk.Button(boutons, text="0").grid(column=1, row=3)
ttk.Button(boutons, text=",").grid(column=2, row=3)
ttk.Button(boutons, text="+").grid(column=3, row=3)
calc.mainloop()