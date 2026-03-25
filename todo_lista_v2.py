from datetime import datetime

tasks = []

def show_tasks():
    if not tasks:
        print("Lista je prazna.")
    else:
        print("\nLista zadataka:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['name']} [{status}] ({task['date']})")

def add_task():
    name = input("Unesi zadatak: ")
    tasks.append({"name": name, "done": False, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
    print(f"Zadatak '{name}' dodat!")

def mark_done():
    show_tasks()
    index = int(input("Koji broj zadatka da oznacim kao uradjen? "))
    if 0 < index <= len(tasks):
        tasks[index-1]["done"] = True
        print(f"Zadatak '{tasks[index-1]['name']}' je uradjen!")
    else:
        print("Pogresan broj.")

def remove_task():
    show_tasks()
    index = int(input("Koji broj zadatka obrisati? "))
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        print(f"Zadatak '{removed['name']}' obrisan!")
    else:
        print("Pogresan broj.")

while True:
    print("\nOpcije: [1] Prikazi [2] Dodaj [3] Oznaci uradjen [4] Obrisi [5] Izadji")
    choice = input("Izaberi opciju: ")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        break
    else:
        print("Nepoznata opcija")
