def somar():
    print(f'Esta função vai somar valores')

def multiplicar():
    print(f'Esta função vai multiplicar')

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return 0