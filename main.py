from tkinter import *
from tkinter import ttk


def input_process(enter):
    try:
        input_process.storage

    except Exception:
        input_process.storage = []
        input_process.number = ""
        input_process.expression = ""
        input_process.result = 0
        input_process.count = 0
        input_process.sign = "+"
        #Si l'entrée est un nombre
    if isinstance(enter, int) or enter == "," or enter == "+/-":
        enter = str(enter)
        if enter == ",": enter = "."
        if enter == "+/-":
            if input_process.sign == "+":
                input_process.sign = "-"
                sign.set("-")
            else:
                sign.set("")
                input_process.sign = "+"
        else:
            input_process.number = input_process.number + enter
            current_number.set(input_process.number)

    # Si l'entrée est "="
    elif enter == "=":
        pass

    # Si l'entrée est "CE"
    elif enter == "CE":
        input_process.expression = ""
        input_process.number = ""
        value.set(input_process.expression)
        current_number.set(input_process.number)
        input_process.storage = []

    # Si l'entrée est une chaine de caractère autre que testé précédemment, ces entrée correspondent a un opérateur
    elif isinstance(enter, str):
        #Le nombre entrer est complet nous pouvont donc le convertir en int ou en float si le int retourne une erreur a cause de la virgule
        dumper=input_process.number
        try:
            input_process.number = int(input_process.number)
        except Exception:
            input_process.number = float(input_process.number)

        if input_process.sign == "-" :
            negative = str(input_process.number)
            #Si le nombre est le premier alors celui ci ne prendra pas de parentèses
            if input_process.expression !="": negative = "(-"+negative+")"
            else: negative = "-"+negative
            input_process.number = input_process.number * -1
            print(input_process.expression)
            input_process.expression = input_process.expression + negative + enter
            input_process.sign = "+"
        else:

            input_process.expression = input_process.expression+ dumper + enter

        input_process.storage.append(input_process.number)
        sign.set("")

        input_process.number = ""
        current_number.set(input_process.number)
        input_process.storage.append(enter)
        print(input_process.storage)
        print(input_process.expression)
        value.set(input_process.expression)
        print(value.get())

def egal(operation):
    calculs=True
    while calculs=True:

calc = Tk()
calc.title("Calculatrice")

# Création des trois cadres utilisés dans notre calculatrice

# Cadre display permettant l'affichage de l'opération
display = ttk.Frame(calc, padding="10 10 5 5")
display.grid(column=0, row=0, sticky=("N", "E"))
display.columnconfigure(0, weight=1)
display.rowconfigure(0, weight=1)



boutons = ttk.Frame(calc, padding="1 1 1 1")
boutons.grid(column=0, row=1, sticky=(W, E, S))
calc.columnconfigure(0, weight=1)
calc.rowconfigure(0, weight=1)
value = StringVar()
sign = StringVar()
current_number = StringVar()
ttk.Label(display, textvariable=sign).grid(column=0, row=1)
ttk.Label(display, textvariable=value,font=12).grid(column=0, row=0)
ttk.Label(display, textvariable=current_number).grid(column=1, row=1)
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
ttk.Button(boutons, text="CE", command=lambda: input_process("CE")).grid(column=4, row=0)

calc.mainloop()
