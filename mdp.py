import json
import hashlib
import os

def hash_password(password):
    # Hash le mot de passe avec l'algorithme SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def create_password():
    # Demande à l'utilisateur de créer un mot de passe et vérifie s'il est valide
    while True:
        password = input("Entrez un mot de passe : ")
        if len(password) < 8:
            print("\033[1;41m Le mot de passe doit contenir au moins 8 caractères. \033[0m")
        elif not any(char.isupper() for char in password):
            print("\033[1;41m Le mot de passe doit contenir au moins une lettre majuscule.\033[0m")
        elif not any(char.islower() for char in password):
            print("\033[1;41m Le mot de passe doit contenir au moins une lettre minuscule.\033[0m")
        elif not any(char.isdigit() for char in password):
            print("\033[1;41m Le mot de passe doit contenir au moins un chiffre.\033[0m")
        elif not any(char in "!@#$%^&*" for char in password):
            print("\033[1;41m Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).\033[0m")
        else:
            return password

def add_password():
    # Ajoute un mot de passe au fichier
    filename = "passwords.json"
    if not os.path.isfile(filename):
        # Si le fichier n'existe pas, on le crée en initialisant avec une liste vide
        with open(filename, "w") as f:
            json.dump([], f)
    with open(filename, "r") as f:
        passwords = json.load(f)
    password = create_password()
    hashed_password = hash_password(password)
    # Parcour les mots de passe haché dans le ficher passwords.json
    if any(pw[0] == hashed_password for pw in passwords):
        print("\033[1;41mCe mot de passe est déjà enregistré.\033[0m")
    else:
        passwords.append([hashed_password, password])
        with open(filename, "w") as f:
            json.dump(passwords, f)
        print("\033[1;32m\nMot de passe ajouté avec succès.\033[0m")

def display_passwords():
    # Affiche tous les mots de passe enregistrés dans le fichier
    filename = "passwords.json"
    if not os.path.isfile(filename):
        # Si le fichier n'existe pas, on affiche un message et on sort
        print("\033[1;41m Le fichier de mots de passe n'existe pas.\033[0m")
        return
    with open(filename, "r") as f:
        passwords = json.load(f)
        # check les données dans le ficher
    if len(passwords) == 0:
        print("\033[1;41m Aucun mot de passe enregistré.\033[0m")
    else:
        print("\033[1;36m Mot de passe : Mot de passe crypté\033[0m")
        for hashed_password, password in passwords:
            print(password + " : " + hashed_password)

def main():
    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Ajouter un mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")
        choice = input("Entrez votre choix (1-3) : ")
        if choice == "1":
            add_password()
        elif choice == "2":
            display_passwords()
        elif choice == "3":
            print("\nAu revoir !")
            break
        else:
            print("\033[1;41m Choix invalide. Veuillez réessayer.\033[0m")

if __name__ == "__main__":
    main()