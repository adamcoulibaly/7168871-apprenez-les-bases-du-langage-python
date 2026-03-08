# dictionnaire de fruits
fruits = {
    "pomme" : "rouge",
    "banane" : "jaune",
    "orange" : "orange"
}

# ajout de kiwi au dictionnaire
fruits['kiwi'] = "verts"
print(fruits)

# modifier la couleur de la pomme
fruits['pomme'] = "vert"
print(fruits)

# supprimer la banane du dictionnaire
del fruits['banane']
print(fruits)

# afficher les valeurs du dictionnaire
print(fruits.keys())
print(fruits.values())
