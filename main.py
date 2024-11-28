import hashlib
import json

def condition(mot_de_passe):

    caracteres_speciaux = "!@#$%^&*"

        
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
        
    else:
        return ("Mot de passe valide")

while True:
    mot_de_passe = input("Entrez un mot de passe : ")
    resultat=condition(mot_de_passe)

    if resultat == "Mot de passe valide":
        print("Mot de passe valide")
        break
    else:
        print(resultat)

    

def hachage(mot_de_passe):
    hachage = hashlib.sha256()
    hachage.update(mot_de_passe.encode('utf-8'))

    hash_hex = hachage.hexdigest()

    print("Hachage SHA-256 :",hash_hex)

    return hash_hex

def fichier_json(mot_de_passe, mdp_hachee, filename='id.json'):
    new_data = {
        "Mot de passe: ":mot_de_passe,
        "Mot de passe haché:": mdp_hachee
    }
    
    with open(filename, 'r') as file:
        file_data = json.load(file)
        for user_id, data in file_data.items():
            if data == new_data:
                return "Les données sont déja présente"
    user_id = f"user_{len(file_data)+1}"
    file_data[user_id] = new_data

    with open (filename,'w') as file:
        json.dump(file_data, file, indent=4)
        print("Ecruture réussi")

    with open(filename, 'r') as file:
        file_data = json.load(file)
        print("Contenu du fichier Json")
        print(file_data)

mdp_hachee=hachage(mot_de_passe)


fichier_json(mot_de_passe, mdp_hachee)

