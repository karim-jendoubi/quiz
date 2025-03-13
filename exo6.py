# Initialisation du dictionnaire des réponses et du score
rep = {}
resultat = 0

# Question 1
print("Quelle est la capitale du Brésil? \n1. Brasilia\n2. Rio de Janeiro\n3. Marseille")
prep = int(input("Votre réponse (1, 2, 3) : "))
rep["rep"] = prep
if rep["rep"] == 1:
    print("Bonne réponse !")
    resultat += 1
else:
    print("Mauvaise réponse. La bonne réponse était : Brasilia.")

# Question 2
print("\nQuelle est la capitale de l'Espagne? \n1. Salamanca\n2. Madrid\n3. Barcelone")
prep = int(input("Votre réponse (1, 2, 3) : "))
rep["repo"] = prep
if rep["repo"] == 2:
    print("Bonne réponse !")
    resultat += 1
else:
    print("Mauvaise réponse. La bonne réponse était : Madrid.")

# Question 3
print("\nQuelle est la capitale du Mexique? \n1. Mexico\n2. Guadalajara\n3. Monterrey")
prep = int(input("Votre réponse (1, 2, 3) : "))
rep["repon"] = prep
if rep["repon"] == 1:
    print("Bonne réponse !")
    resultat += 1
else:
    print("Mauvaise réponse. La bonne réponse était : Mexico.")

# Résultat final
print(f"\nVotre score final est de {resultat}/3.")
if resultat == 3:
    print("Excellent travail ! Vous avez tout juste.")
elif resultat == 2:
    print("Pas mal, mais vous pouvez faire mieux.")
else:
    print("Révisez un peu et réessayez !")
