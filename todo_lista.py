tasks = []

def show_tasks():
    if not tasks:
        print("Lista je prazna.")
    else:
        print("\nLista zadataka:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Unesi novi zadatak: ")
    tasks.append(task)
    print(f"Zadatak '{task}' dodat!")

def remove_task():
    show_tasks()
    index = int(input("Koji broj zadatka želiš da obrišeš? "))
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        print(f"Zadatak '{removed}' obrisan!")
    else:
        print("Pogrešan broj.")

while True:
    print("\nOpcije: [1] Prikazi [2] Dodaj [3] Obrisi [4] Izadji")
    choice = input("Izaberi opciju: ")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Izlaz iz To-Do liste.")
        break
    else:
        print("Nepoznata opcija.")
