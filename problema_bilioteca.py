import pickle

class Carte:
    def __init__(self, titlu, autor):
        self.titlu = titlu
        self.autor = autor
        self.imprumutata_la = None
        self.lista_asteptare = []

    def adauga_client_asteptare(self, nume_client):
        self.lista_asteptare.append(nume_client)

    def elimina_client_asteptare(self, nume_client):
        self.lista_asteptare.remove(nume_client)

    def textString(self):
        return f"Titlu: {self.titlu}\nAutor: {self.autor}\nImprumutata la: {self.imprumutata_la}\nLista asteptare: {', '.join(self.lista_asteptare)}"


class Client:
    def __init__(self, nume):
        self.nume = nume
        self.numar_carti_imprumutate = 0

    def textString(self):
        return f"Nume: {self.nume}\nNumar carti imprumutate: {self.numar_carti_imprumutate}"


class Biblioteca:
    def __init__(self):
        self.carti = []
        self.clienti = []

    def cautare_carte(self, titlu):
        for carte in self.carti:
            if carte.titlu == titlu:
                return carte
        return None

    def adauga_carte(self, carte):
        self.carti.append(carte)

    def modificare_carte(self, titlu, autor_nou):
        carte = self.cautare_carte(titlu)
        if carte:
            carte.autor = autor_nou
            print("Informatii actualizate cu succes!")
        else:
            print("Cartea nu exista in biblioteca.")

    def sterge_carte(self, titlu):
        carte = self.cautare_carte(titlu)
        if carte:
            if carte.imprumutata_la:
                print("Cartea este imprumutata si nu poate fi stearsa.")
            else:
                self.carti.remove(carte)
                print("Cartea a fost stearsa cu succes!")
        else:
            print("Cartea nu exista in biblioteca.")

    def imprumuta_carte(self, nume_client, titlu):
        carte = self.cautare_carte(titlu)
        if not carte:
            print("Cartea nu exista in biblioteca.")
            return

        client = self.cautare_client(nume_client)
        if not client:
            client = Client(nume_client)
            self.clienti.append(client)

        if client.numar_carti_imprumutate >= 3:
            print("Clientul a atins numarul maxim de carti imprumutate.")
            return

        if not carte.imprumutata_la:
            carte.imprumutata_la = client.nume
            client.numar_carti_imprumutate += 1
            print("Carte imprumutata cu succes!")
        else:
            carte.adauga_client_asteptare(nume_client)
            print("Cartea este deja imprumutata. Clientul a fost adaugat la lista de asteptare.")

    def returneaza_carte(self, nume_client, titlu):
        carte = self.cautare_carte(titlu)
        if not carte:
            print("Cartea nu exista in biblioteca.")
            return

        client = self.cautare_client(nume_client)
        if not client:
            print("Clientul nu exista.")
            return

        if carte.imprumutata_la == nume_client:
            carte.imprumutata_la = None
            client.numar_carti_imprumutate -= 1
            print("Carte returnata cu succes!")

            if carte.lista_asteptare:
                urmatorul_client = self.cautare_client(carte.lista_asteptare[0])
                carte.lista_asteptare.pop(0)
                self.imprumuta_carte(urmatorul_client.nume, carte.titlu)
        else:
            print("Cartea nu este imprumutata de acest client.")

    def cautare_client(self, nume_client):
        for client in self.clienti:
            if client.nume == nume_client:
                return client
        return None

    def afisare_carte(self, titlu):
        carte = self.cautare_carte(titlu)
        if carte:
            print(carte.textString())
        else:
            print("Cartea nu exista in biblioteca.")

    def afisare_client(self, nume_client):
        client = self.cautare_client(nume_client)
        if client:
            print(client.textString())
        else:
            print("Clientul nu exista.")

    def afisare_biblioteca(self):
        if self.carti:
            for carte in self.carti:
                print(carte.textString())
                print("------------------------")
        else:
            print("Biblioteca este goala.")

    def salveaza_date(self):
        try:
            with open("salvate.txt", "wb") as file:
                pickle.dump(self, file)
            print("Datele au fost salvate cu succes!")
        except:
            print("Eroare la salvarea datelor.")

    def incarca_date(self):
        try:
            with open("salvate.txt", "rb") as file:
                biblioteca = pickle.load(file)
            print("Datele au fost incarcate cu succes!")
            return biblioteca
        except FileNotFoundError:
            print("Fisierul salvate.txt nu exista. Se creeaza unul nou.")
            return Biblioteca()


biblioteca = Biblioteca().incarca_date()

while True:
    print("\n========= MENIU =========")
    print("1. Cautare carte")
    print("2. Adaugare carte")
    print("3. Modificare informatii carte")
    print("4. Stergere carte")
    print("5. Returnare carte")
    print("6. Iesire si salvare date")
    print("=========================")

    optiune = input("Selectati o optiune: ")

    if optiune == "1":
        titlu = input("Introduceti titlul cartii: ")
        biblioteca.afisare_carte(titlu)
    elif optiune == "2":
        titlu = input("Introduceti titlul cartii: ")
        autor = input("Introduceti autorul cartii: ")
        carte = Carte(titlu, autor)
        biblioteca.adauga_carte(carte)
        print("Carte adaugata cu succes!")
    elif optiune == "3":
        titlu = input("Introduceti titlul cartii: ")
        autor_nou = input("Introduceti noul autor: ")
        biblioteca.modificare_carte(titlu, autor_nou)
    elif optiune == "4":
        titlu = input("Introduceti titlul cartii: ")
        biblioteca.sterge_carte(titlu)
    elif optiune == "5":
        nume_client = input("Introduceti numele clientului: ")
        titlu = input("Introduceti titlul cartii: ")
        biblioteca.returneaza_carte(nume_client, titlu)
    elif optiune == "6":
        biblioteca.salveaza_date()
        break
    else:
        print("Optiune invalida! Va rugam selectati o optiune valida.")
