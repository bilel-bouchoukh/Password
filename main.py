import hashlib

def condition():

    caracteres_speciaux = "!@#$%^&*"


    while True:
        mot_de_passe = input("Entrez un mot de passe : ")
        
        if len(mot_de_passe) < 8:
            print("Erreur : Le mot de passe doit contenir au moins 8 caractères.")

        if not any(lettre.isupper() for lettre in mot_de_passe):
            print("Le mot de passe doit contenir au moins une lettre majuscule.")

        if not any(lettre.islower() for lettre in mot_de_passe):
            print("Le mot de passe doit contenir au moins une lettre minuscule.")

        if not any(lettre.isdigit() for lettre in mot_de_passe):
            print("Le mot de passe doit contenir au moins un chiffre.")

        if not any(lettre in caracteres_speciaux for lettre in mot_de_passe):
            print("Le mot de passe doit contenir au moins un caractère spécial",caracteres_speciaux,".")

        print("Le mot de passe rentrer est valide")

        return mot_de_passe

def hachage():
    hachage = hashlib.sha256()
    hachage.update(condition().encode('utf-8'))

    hash_hex = hachage.hexdigest()

    print("Hachage SHA-256 :",hash_hex)

hachage()
