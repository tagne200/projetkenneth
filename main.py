def demander_age():
    age = 0
    while age == 0:
        age_str = input("quel est votre age ? ")

        try:
            age= int(age_str) 
        except:
            print("ERREUR: entre les chiffres mon frere")  
    return age


nom = ""
while nom == "":
    nom = input("quel est ton nom ? ")
    

age = demander_age()
print("je mappelle " + nom + "," , "vous avez " + str(age) + "ans.")
print("l'annee prochaine tu aura " + str(age+1) + " ans.")


# password = ""
# while not password == "toto":
#     password= input("  saisi le mot de passe")

# print("bienvenue toto")
