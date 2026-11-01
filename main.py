AGE_MINIMUM = 1
AGE_MAXIMUM = 130


def lire_age(saisie):
    """Convertit une saisie en age, ou retourne None si elle est invalide."""
    try:
        age = int(saisie)
    except ValueError:
        return None
    if AGE_MINIMUM <= age <= AGE_MAXIMUM:
        return age
    return None


def demander_nom():
    nom = ""
    while nom == "":
        nom = input("quel est ton nom ? ").strip()
    return nom


def demander_age():
    while True:
        age = lire_age(input("quel est votre age ? "))
        if age is not None:
            return age
        print(f"ERREUR: entre un nombre entre {AGE_MINIMUM} et {AGE_MAXIMUM}")


def creer_message(nom, age):
    return (
        f"je m'appelle {nom}, vous avez {age} ans.\n"
        f"l'annee prochaine tu auras {age + 1} ans."
    )


def main():
    nom = demander_nom()
    age = demander_age()
    print(creer_message(nom, age))


if __name__ == "__main__":
    main()
