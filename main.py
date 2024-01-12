from StarLogic import *

if __name__ == '__main__':
    import random, string

    dt = {random.choice(string.ascii_letters): random.randint(0, 15000) for _ in range(50)}

    print(dt)

    lista = ListOfStars()
    lista.importFromFile('gwiazdy.txt')
    print(str(lista))