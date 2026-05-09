import json

def incarca_useri():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}

def salveaza_useri(useri):
    with open("users.json", "w") as f:
        json.dump(useri, f, indent=4)


def este_parola_buna(parola):
    if len(parola) < 6: 
        return False
    for c in parola:
        if c.isdigit():
            return True
    return False

def inregistrare(baza_date):
    nume_cont=input("Username nou: ")
    if nume_cont in baza_date:
        print(f"Username-ul {nume_cont} este inregistrat!")
    else:           
        cere_parola=input("Password: ")
       
        if este_parola_buna(cere_parola): 
            baza_date[nume_cont] = cere_parola
            salveaza_useri(baza_date) 
            print(f"Inregistrare numelui {nume_cont} a fost realizata!")
        else:
            print("Parola trebuie sa aiba minim 6 caractere si cel putin o cifra!")

def login(baza_date):
        nume=input("Username: ")
        parola=input("Password: ")
        if nume in baza_date and baza_date[nume] == parola:
            print(f"Bine ai venit {nume}!")
            return True
        else:
            print("Login esuat!")
        return False


useri = incarca_useri()

while True:
    print("\n1. Login | 2. Inregistrare | 3. Iesire")
        
    optiune=input("Alege optiunea: ")

    if optiune == "1":
        login(useri)
    elif optiune =="2":
        inregistrare(useri)
    elif optiune=="3":
        print("Stop...")
        break
    else:
        print("Opțiune invalidă!")
    
