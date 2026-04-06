def salaire_mensuel (salaire_annuel):
    salaire_mensuel = salaire_annuel / 12
    return salaire_mensuel

def salaire_hebdomadaire (salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel / 4
    return salaire_hebdomadaire

def salaire_horaire (salaire_hebdomadaire, heures_travail):
    salaire_horaire = salaire_hebdomadaire / heures_travail
    return salaire_horaire 

salaire_annuel = float(input("Entres votre salaire annuel : "))
heures_travail = float(input("Entres le nombre d'heures de travail par semaine : "))

mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, heures_travail)

print("votre salaire mensuel est de : ", mensuel)
print("votre salaire hebdomadaire est de : ", hebdomadaire)
print("votre salaire horaire est de : ", horaire)# Ecrivez votre code ici
