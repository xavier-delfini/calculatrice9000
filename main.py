from tkinter import *
from tkinter import ttk

def input_process(enter):
    try:
        input_process.storage
        input_process.number
        input_process.expression
        input_process.result
        input_process.count
        input_process.modulo

    except Exception:
        input_process.storage=[]
        input_process.number=""
        input_process.expression=""
        input_process.result=0
        input_process.count=0
        input_process.modulo="+"
    if isinstance(enter, int) or enter == "," or enter == "+/-":
        enter=str(enter)
        if enter == ",": enter = "."
        if enter == "+/-":
            if input_process.modulo == "+": modulo.set("-")
            else:
                modulo.set("")
        else:
            input_process.number = input_process.number + enter
            input_process.expression = input_process.expression + enter
            value.set(input_process.expression)

    elif enter == "=":
        pass
    elif isinstance(enter, str):
        #Stockage du nombre dans la liste storage
        input_process.number=int(input_process.number)
        test=modulo.get
        print(test)
        if modulo.get =="-":
            input_process.number=input_process.number * -1
        input_process.storage.append(input_process.number)
        input_process.number=""
        input_process.storage.append(enter)
        print(input_process.storage)
        input_process.expression= input_process.expression + enter
        print (input_process.expression)
        value.set(input_process.expression)


calc = Tk()
calc.title("Calculatrice")

# Création des deux cadres utilisé dans notre calculatrice
#Cadre affichage permettant l'affichage du résultat ou de l'opération
affichage = ttk.Frame(calc, padding="10 10 5 5")
affichage.grid(column=0, row=0, sticky=(N, E))
affichage.columnconfigure(0, weight=1)
affichage.rowconfigure(0, weight=1)

boutons = ttk.Frame(calc, padding="1 1 1 1")
boutons.grid(column=0, row=1, sticky=(W, E, S))
calc.columnconfigure(0, weight=1)
calc.rowconfigure(0, weight=1)
value = StringVar()
modulo = StringVar()

ttk.Label(affichage, textvariable=modulo).grid(column=0, row=0)
ttk.Label(affichage, textvariable=value).grid(column=1, row=0)
ttk.Button(boutons, text="7", command=lambda: input_process(7)).grid(column=0, row=0)
ttk.Button(boutons, text="8", command=lambda: input_process(8)).grid(column=1, row=0)
ttk.Button(boutons, text="9", command=lambda: input_process(9)).grid(column=2, row=0)
ttk.Button(boutons, text="÷", command=lambda: input_process("/")).grid(column=3, row=0)
ttk.Button(boutons, text="6", command=lambda: input_process(6)).grid(column=0, row=1)
ttk.Button(boutons, text="5", command=lambda: input_process(5)).grid(column=1, row=1)
ttk.Button(boutons, text="4", command=lambda: input_process(4)).grid(column=2, row=1)
ttk.Button(boutons, text="X", command=lambda: input_process("X")).grid(column=3, row=1)
ttk.Button(boutons, text="3", command=lambda: input_process(3)).grid(column=0, row=2)
ttk.Button(boutons, text="2", command=lambda: input_process(2)).grid(column=1, row=2)
ttk.Button(boutons, text="1", command=lambda: input_process(1)).grid(column=2, row=2)
ttk.Button(boutons, text="-", command=lambda: input_process("-")).grid(column=3, row=2)
ttk.Button(boutons, text="+/-", command=lambda: input_process("+/-")).grid(column=0, row=3)
ttk.Button(boutons, text="0", command=lambda: input_process(0)).grid(column=1, row=3)
ttk.Button(boutons, text=",", command=lambda: input_process(",")).grid(column=2, row=3)
ttk.Button(boutons, text="+", command=lambda: input_process("+")).grid(column=3, row=3)
ttk.Button(boutons, text="=", command=lambda: input_process("=")).grid(column=4, row=4)
calc.mainloop()