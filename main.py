from tkinter import *
from tkinter import ttk


def input_process(enter):
    def insert_number():
        # Stockage temporaire

        dumper = input_process.number
        # Si nombre entré int sinon nombre float
        try:
            input_process.number = int(input_process.number)
        except ValueError:
            input_process.number = float(input_process.number)
        # Si nombre négatif
        if input_process.sign == "-":
            # Convertion du nombre en str pour la variable expression
            negative = str(input_process.number)
            # Si ce n'est pas le premier nombre de l'opération alors parenthèses
            if input_process.expression != "":
                negative = "(-" + negative + ")"
            # Si le nombre est le premier alors celui ci ne prendra pas de parentèses
            else:
                negative = "-" + negative
            # On fait passer le nombre qui est encore en int ou float en nombre négatif
            input_process.number = input_process.number * -1
            # On ajoute aussi
            input_process.expression = input_process.expression + negative + enter
            input_process.sign = "+"
        else:

            input_process.expression = input_process.expression + dumper + enter
        value.set(input_process.expression)
        input_process.storage.append(input_process.number)

    def egal(operation):
        def add_sou(operator):
            if operator == "+":
                result = operation[0] + operation[2]
            else:
                result = operation[0] - operation[2]
            del operation[0:2]
            operation[0] = result

        def multi_div_square_percent(op, location):
            if op == "X":
                result = operation[location - 1] * operation[location + 1]
            elif op == "/":
                try:
                    result = operation[location - 1] / operation[location + 1]
                # Si l'operation est une division par 0 on arrète le programme pour afficher un code erreur
                except ZeroDivisionError:
                    return 1
            elif op == "%":
                result=operation[location -1] * operation[location + 1] / 100.0
            #Racine carré
            else:
                operation[location] = operation[location + 1] ** (1 / 2)
                del operation[location + 1]
                return 0
            operation[location - 1] = result
            del operation[location:location + 2]

        insert_number()
        i = 0
        while (len(operation) >= 2) and (i < len(operation)):
            if operation[i] == "√":
                multi_div_square_percent("√", i)
                i = 0
            i += 1

        i = 0
        while (len(operation) >= 2) and (i < len(operation)):
            match operation[i]:
                case "X":
                    multi_div_square_percent("X", i)
                    i = 0
                case "/":
                    if multi_div_square_percent("/", i) == 1:
                        return "zero"
                    i = 0
                case "%":
                    multi_div_square_percent("%",i)
                    i =0
            i += 1
            lenth = len(operation)

        i = 0
        while len(operation) >= 2:

            match operation[1]:
                case "+":
                    add_sou("+")
                case "-":
                    add_sou("-")
                case "=":
                    del operation[1]
                    break
        return operation[0]



    try:
        input_process.storage

    except AttributeError:
        input_process.storage = []
        input_process.number = ""
        input_process.expression = ""
        input_process.sign = "+"

        # Si l'entrée est un nombre
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
        result = egal(input_process.storage)
        if result == "zero":
            input_process.expression = "div zero, redémarrage"
            input_process.number = ""
            value.set(input_process.expression)
            current_number.set(input_process.number)
            input_process.storage = []
            input_process.expression = ""
            current_number.set(input_process.number)


        else:
            historique.set(historique.get() +input_process.expression + str(result) + "\n")


            current_number.set(result)
            input_process.expression = ""
            input_process.number = result
            input_process.storage = []
            input_process.number = str(input_process.number)

    # Si l'entrée est "CE"
    elif enter == "CE":
        # Remise à 0 de la variable expression,number et storage et définition des variable d'affichage
        # pour que celle ci prennent la valeur de ces variables
        input_process.expression = ""
        input_process.number = ""
        value.set(input_process.expression)
        current_number.set(input_process.number)
        input_process.storage = []
    elif enter =="H":
        historique.set("")
        return 0
    elif enter == "C":
        input_process.number = ""
        current_number.set(input_process.number)
    # Si l'entrée est une chaine de caractère autre que testé précédemment, cet entrée correspont a un opérateur

    elif isinstance(enter, str):
        # Le nombre entrer est complet nous pouvont donc le convertir en int ou en float si le int retourne une erreur a cause de la virgule
        n=0
        if input_process.number != "":
            insert_number()
            sign.set("")
            current_number.set(input_process.number)
            input_process.number = ""
            n=1

        if (enter == "+" or enter == "-" or enter == "X" or enter == "/" or enter != "√") \
                and not isinstance(input_process.storage[-1], str):
            current_number.set("")
        else:
            if n==0 and enter == "√" and input_process.number=="":
                input_process.expression = input_process.expression+"√"
                current_number.set("√")
            else: return 0
        if input_process.number != "":
            insert_number()
            sign.set("")
            current_number.set(input_process.number)
            input_process.number = ""
            n=1
        input_process.storage.append(enter)


# Déclaration de notre cadre parent permettant l'affichage des cadres enfants
main = Tk()
main.title("Calculatrice")
main.resizable(False, False)
# Création des trois cadres enfants utilisés dans notre calculatrice
calc = ttk.Frame(main, borderwidth=2, relief="ridge", padding="10 10 5 5")
calc.grid(column=0, row=0, sticky=("N","S","W"))
calc.columnconfigure(0, weight=1)
calc.rowconfigure(0, weight=1)
# Affichage de l'operation et du nombre actuellement entrée
display = ttk.Frame(calc, borderwidth=5, relief="ridge", padding="10 10 5 5")
display.grid(column=0, row=0, sticky=("N", "E" ,"W"))
display.columnconfigure(0, weight=1)
display.rowconfigure(0, weight=1)

# Affichage des boutons
boutons = ttk.Frame(calc, padding="1 1 1 1")
boutons.grid(column=0, row=1, sticky=("W","E", ))
boutons.columnconfigure(0, weight=1)
boutons.rowconfigure(0, weight=1)

histo = ttk.Frame(main, padding="1 1 1 1")
histo.grid(column=1, row=0, sticky=("E","N"))
histo["padding"]=20
# Déclaration de variable utile a l'affichage
value = StringVar()
sign = StringVar()
current_number = StringVar()
historique=StringVar()
# Déclaration de zones de texte pour l'affichage
ttk.Label(display, textvariable=sign).grid(column=0, row=1)
ttk.Label(display, textvariable=value).grid(column=0, row=0)
ttk.Label(display, textvariable=current_number).grid(column=1, row=1)
# Déclaration des boutons
ttk.Button(boutons, text="7", command=lambda: input_process(7)).grid(column=0, row=0)
ttk.Button(boutons, text="8", command=lambda: input_process(8)).grid(column=1, row=0)
ttk.Button(boutons, text="9", command=lambda: input_process(9)).grid(column=2, row=0)
ttk.Button(boutons, text="6", command=lambda: input_process(6)).grid(column=0, row=1)
ttk.Button(boutons, text="5", command=lambda: input_process(5)).grid(column=1, row=1)
ttk.Button(boutons, text="4", command=lambda: input_process(4)).grid(column=2, row=1)
ttk.Button(boutons, text="3", command=lambda: input_process(3)).grid(column=0, row=2)
ttk.Button(boutons, text="2", command=lambda: input_process(2)).grid(column=1, row=2)
ttk.Button(boutons, text="1", command=lambda: input_process(1)).grid(column=2, row=2)
ttk.Button(boutons, text="+/-", command=lambda: input_process("+/-")).grid(column=0, row=3)
ttk.Button(boutons, text="0", command=lambda: input_process(0)).grid(column=1, row=3)
ttk.Button(boutons, text=",", command=lambda: input_process(",")).grid(column=2, row=3)
ttk.Button(boutons, text="+", command=lambda: input_process("+")).grid(column=0, row=4)
ttk.Button(boutons, text="-", command=lambda: input_process("-")).grid(column=1, row=4)
ttk.Button(boutons, text="%", command=lambda: input_process("%")).grid(column=2, row=4)
ttk.Button(boutons, text="X", command=lambda: input_process("X")).grid(column=0, row=5)
ttk.Button(boutons, text="÷", command=lambda: input_process("/")).grid(column=1, row=5)
ttk.Button(boutons, text="√", command=lambda: input_process("√")).grid(column=2, row=5)
ttk.Button(boutons, text="CE", command=lambda: input_process("CE")).grid(column=0, row=6)
ttk.Button(boutons, text="C", command=lambda: input_process("C")).grid(column=1, row=6)
ttk.Button(boutons, text="=", command=lambda: input_process("=")).grid(column=2, row=6)

ttk.Label(histo, text="Historique:", font=12).grid(column=0, row=0)
ttk.Label(histo, textvariable=historique, font=12).grid(column=0, row=1)
ttk.Button(histo, text="Reset", command=lambda: input_process("H")).grid(column=0, row=2)

main.mainloop()
