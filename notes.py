filename = "moje_bilješke.txt"

def load_notes():
    try:
        with open(filename, "r") as f:
            notes = f.readlines()
        return [note.strip() for note in notes]
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(filename, "w") as f:
        for note in notes:
            f.write(note + "\n")

def show_notes(notes):
    if not notes:
        print("Nema bilješki.")
    else:
        print("\n--- bilješke ---")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

def add_note(notes):
    note = input("Unesi novu bilješku: ")
    notes.append(note)
    save_notes(notes)
    print("Bilješka dodata!")

def delete_note(notes):
    show_notes(notes)
    try:
        index = int(input("Koji broj bilješke želiš da obrišeš? "))
        if 0 < index <= len(notes):
            removed = notes.pop(index-1)
            save_notes(notes)
            print(f"bilješka '{removed}' obrisana!")
        else:
            print("Pogrešan broj.")
    except ValueError:
        print("Unesi validan broj.")

def search_notes(notes):
    keyword = input("Unesi ključnu reč za pretragu: ").lower()
    results = [note for note in notes if keyword in note.lower()]
    if results:
        print("\nPronađene bilješke:")
        for i, note in enumerate(results, 1):
            print(f"{i}. {note}")
    else:
        print("Nije pronađena nijedna bilješka.")

# Glavni meni
notes = load_notes()
while True:
    print("\nOpcije: [1] Prikazi [2] Dodaj [3] Obrisi [4] Pretrazi [5] Izadji")
    choice = input("Izaberi opciju: ")
    if choice == "1":
        show_notes(notes)
    elif choice == "2":
        add_note(notes)
    elif choice == "3":
        delete_note(notes)
    elif choice == "4":
        search_notes(notes)
    elif choice == "5":
        break
    else:
        print("Nepoznata opcija.")
