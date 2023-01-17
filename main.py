from tkinter import *
from tkinter import ttk


def input_process(enter):

    def insert_number():
        dumper = input_process.number
        try:
            input_process.number = int(input_process.number)
        except Exception:
            input_process.number = float(input_process.number)

        if input_process.sign == "-":
            negative = str(input_process.number)
            # Si le nombre est le premier alors celui ci ne prendra pas de parentèses
            if input_process.expression != "":
                negative = "(-" + negative + ")"
            else:
                negative = "-" + negative
            input_process.number = input_process.number * -1
            print(input_process.expression)
            input_process.expression = input_process.expression + negative + enter
            input_process.sign = "+"
        else:

            input_process.expression = input_process.expression + dumper + enter
        value.set(input_process.expression)
        input_process.storage.append(input_process.number)
    def egal(operation):
        def add_sou(operator):
            if operator =="+":
                result=operation[0] + operation[2]
            else:
                result = operation[0] - operation[2]
            del operation[0:2]
            operation[0]=result
            print(operation)
        def multi_div(op,location):
            if op == "X":
                result = operation[location - 1] * operation[location + 1]
            else:
                try:
                    result = operation[location - 1] / operation[location + 1]
                except ZeroDivisionError:
                    return 1

            operation[location - 1] = result
            print (operation)
            del operation[location:location+2]
            print(operation)



        insert_number()
        i=0
        lenth = len(operation)
        while (lenth >= 2) and (i<lenth):
            match operation[i]:
                case "X":
                    multi_div("X",i)
                    i =0
                case "/":
                    if multi_div("/",i)==1:
                        d0=1
                        return "zero"
                    i = 0
            i+=1
            print(i)
            lenth=len(operation)
            print (lenth)
        i=0
        while len(operation) >= 2:

            match operation[1]:
                case "+":
                    add_sou("+")
                case "-":
                    add_sou("-")
                case "=":
                    del operation[1]
                    break

        e=1
        return operation[0]



    try:
        input_process.storage

    except Exception:
        input_process.storage = []
        input_process.number = ""
        input_process.expression = ""
        input_process.result = 0
        input_process.count = 0
        input_process.sign = "+"
        e=1
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
        result=egal(input_process.storage)
        if result=="zero":
            input_process.expression = "div zero, redémarrage"

            input_process.number = ""
            value.set(input_process.expression)
            current_number.set(input_process.number)
            input_process.storage = []
            import time
            time.sleep(5)
            input_process.expression=""
            current_number.set(input_process.number)


        else:
            current_number.set(result)
    # Si l'entrée est "CE"
    elif enter == "CE":
        input_process.expression = ""
        input_process.number = ""
        value.set(input_process.expression)
        current_number.set(input_process.number)
        input_process.storage = []

    # Si l'entrée est une chaine de caractère autre que testé précédemment, cet entrée correspont a un opérateur
    elif isinstance(enter, str):
        #Le nombre entrer est complet nous pouvont donc le convertir en int ou en float si le int retourne une erreur a cause de la virgule
        insert_number()
        sign.set("")
        current_number.set(input_process.number)
        input_process.number = ""

        input_process.storage.append(enter)




#Déclaration de notre cadre parent permettant l'affichage des cadres enfants
calc = Tk()
calc.title("Calculatrice")
calc.resizable(False, False)
# Création des trois cadres enfants utilisés dans notre calculatrice

# Affichage de l'operation et du nombre actuellement entrée
display = ttk.Frame(calc, padding="10 10 5 5")
display.grid(column=0, row=0, sticky=("N", "E"))
display.columnconfigure(0, weight=1)
display.rowconfigure(0, weight=1)

# Affichage des boutons
boutons = ttk.Frame(calc, padding="1 1 1 1")
boutons.grid(column=0, row=1, sticky=(W, E, S))
boutons.columnconfigure(0, weight=1)
boutons.rowconfigure(0, weight=1)
#Déclaration de variable utile a l'affichage
value = StringVar()
sign = StringVar()
current_number = StringVar()
#Déclaration de zones de texte pour l'affichage
ttk.Label(display, textvariable=sign).grid(column=0, row=1)
ttk.Label(display, textvariable=value,font=12).grid(column=0, row=0)
ttk.Label(display, textvariable=current_number).grid(column=1, row=1)
#Déclaration des boutons
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
ttk.Button(boutons, text="", command=lambda: input_process("CE")).grid(column=4, row=0)

calc.mainloop()