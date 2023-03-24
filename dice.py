import random 
while True:     
     print(''' 1. lancez le dé             2. Quitter     ''')    
     user = int(input("Selectionner une option \n"))     
     if user==1:         

# Générer un nombre aléatoire entre 1 et 12
        nombre_secret = random.randint(1, 12)

# Demander à l'utilisateur de deviner le nombre
        nombre_devine = int(input("Devinez un nombre entre 1 et 12 : "))

# Tant que l'utilisateur n'a pas deviné le nombre secret, continuer à demander des propositions
        while nombre_devine != nombre_secret:
            if nombre_devine < nombre_secret:
                  print("Le nombre secret est plus grand.")
            else:
                print("Le nombre secret est plus petit.")
    # Demander une nouvelle proposition à l'utilisateur
            nombre_devine = int(input("Devinez un nombre entre 1 et 12 : "))

# Si l'utilisateur a deviné le nombre secret, afficher un message de victoire
        print("Bravo, vous avez deviné le nombre secret ! Le nombre était", nombre_secret)
     
     else:         
        break