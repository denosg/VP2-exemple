# Funcție pentru afișarea meniului
def display_menu():
    print("Meniu:")
    print("1. Căutare angajat")
    print("2. Adăugare angajat")
    print("3. Modificare angajat")
    print("4. Ștergere angajat")
    print("5. Ieșire din program")

# Funcție pentru căutarea unui angajat în dicționar
def search_employee(dictionary):
    id_number = input("Introduceți numărul ID al angajatului: ")
    if id_number in dictionary:
        employee = dictionary[id_number]
        print("Angajatul a fost găsit:")
        print("Nume:", employee["name"])
        print("Număr ID:", employee["id_number"])
        print("Departament:", employee["department"])
        print("Titlu job:", employee["job_title"])
    else:
        print("Angajatul nu a fost găsit.")

# Funcție pentru adăugarea unui nou angajat în dicționar
def add_employee(dictionary):
    name = input("Introduceți numele angajatului: ")
    id_number = input("Introduceți numărul ID al angajatului: ")
    department = input("Introduceți departamentul angajatului: ")
    job_title = input("Introduceți titlul jobului angajatului: ")

    employee = {
        "name": name,
        "id_number": id_number,
        "department": department,
        "job_title": job_title
    }

    dictionary[id_number] = employee
    print("Angajatul a fost adăugat.")

# Funcție pentru modificarea datelor unui angajat existent în dicționar
def modify_employee(dictionary):
    id_number = input("Introduceți numărul ID al angajatului: ")
    if id_number in dictionary:
        employee = dictionary[id_number]
        print("Angajatul găsit:")
        print("Nume:", employee["name"])
        print("Număr ID:", employee["id_number"])
        print("Departament:", employee["department"])
        print("Titlu job:", employee["job_title"])
        print("Introduceți noile date pentru angajat:")

        name = input("Nume: ")
        department = input("Departament: ")
        job_title = input("Titlu job: ")

        employee["name"] = name
        employee["department"] = department
        employee["job_title"] = job_title

        print("Angajatul a fost modificat.")
    else:
        print("Angajatul nu a fost găsit.")

# Funcție pentru ștergerea unui angajat din dicționar
def delete_employee(dictionary):
    id_number = input("Introduceți numărul ID al angajatului: ")
    if id_number in dictionary:
        del dictionary[id_number]
        print("Angajatul a fost șters.")
    else:
        print("Angajatul nu a fost găsit.")

# Funcție pentru salvarea dicționarului într-un fișier
def save_dictionary(dictionary):
    f = open("employees.txt", "w") 
    for id_number, employee in dictionary.items():
        f.write(employee.int(['id_number']),employee.str(['name']))


def main():
    # Încărcarea dicționarului din fișier (dacă există) sau crearea unui dicționar gol
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
            dictionary = {}
            for line in lines:
                id_number, name, department, job_title = line.strip().split(",")
                employee = {
                    "name": name,
                    "id_number": id_number,
                    "department": department,
                    "job_title": job_title
                }
                dictionary[id_number] = employee
    except FileNotFoundError:
        dictionary = {}

    # Executarea programului
    while True:
        display_menu()
        option = input("Introduceți opțiunea dorită: ")

        if option == "1":
            search_employee(dictionary)
        elif option == "2":
            add_employee(dictionary)
        elif option == "3":
            modify_employee(dictionary)
        elif option == "4":
            delete_employee(dictionary)
        elif option == "5":
            # Salvarea dicționarului în fișier înainte de ieșirea din program
            with open("employees.txt", "w") as file:
                for id_number, employee in dictionary.items():
                    file.write(f"{id_number},{employee['name']},{employee['department']},{employee['job_title']}\n")
            print("Programul a fost încheiat.")
            break
        else:
            print("Opțiune invalidă. Vă rugăm să reintroduceți.")

if __name__ == "__main__":
    main()