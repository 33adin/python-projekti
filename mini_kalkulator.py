import math

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def power(a, b):
    return a ** b
def root(a):
    return math.sqrt(a)

while True:
    print("\nOpcije: +, -, *, /, ^ (stepen), sqrt (koren), exit")
    op = input("Izaberi operaciju: ")
    if op == "exit":
        break
    if op == "sqrt":
        x = float(input("Unesi broj: "))
        print("Rezultat:", root(x))
    else:
        x = float(input("Unesi prvi broj: "))
        y = float(input("Unesi drugi broj: "))
        if op == "+": print("Rezultat:", add(x,y))
        elif op == "-": print("Rezultat:", sub(x,y))
        elif op == "*": print("Rezultat:", mul(x,y))
        elif op == "/": print("Rezultat:", div(x,y))
        elif op == "^": print("Rezultat:", power(x,y))
        else: print("Nepoznata operacija")
