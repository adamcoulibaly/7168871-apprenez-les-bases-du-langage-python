numero_1 = input("Entrez un nombre : ")
numero_2 = input("Entrez un autre nombre : ")

if not numero_1.isnumeric() or not numero_2.isnumeric():
    print("Veuillez entrer des nombres valides.")
    raise ValueError("Fin du programme.")

nombre_1 = int(numero_1)  
nombre_2 = int(numero_2)

operation = input("Entrez une opération (+, -, *, /) : ")

if operation not in ["+", "-", "*", "/"]:
    print("Opération non valide. Veuillez entrer +, -, *, ou /.")
    raise ValueError("Fin du programme.")

if operation == "+":
    resultat = nombre_1 + nombre_2
elif operation == "-":
    resultat = nombre_1 - nombre_2
elif operation == "*":
    resultat = nombre_1 * nombre_2
elif operation == "/":  
    if nombre_2 == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    resultat = round(nombre_1 / nombre_2, 2) 
else:
    raise ValueError("Opération non valide. Veuillez entrer +, -, *, ou /.")

print(f"Le résultat de l'operation est : {round(resultat, 2)}")


