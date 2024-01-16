from StarLogic import *

if __name__ == '__main__':
    mainLista = ListOfStars()
    mainLista.importFromFile('gwiazdy.txt')

    print("Jaką chcesz wykonać operację?")
    print("Wybierz operację pisząc odpowiednią liczbę")
    print("1. Wypisz wszystkie zapisane gwiazdy")
    print("2. Dodaj gwiazdę do systemu")
    print("3. Usuń gwiazdę z systemu")
    print("4. Posortuj gwiazdy względem odległości od ziemi")
    print("5. Zaimportuj gwiazdy z pliku")
    print("6. Exportuj gwiazdy do pliku")
    print("7. Zakończ działanie programu")
    print("\n")
    operacja = input("Wprowadź liczbę by rozpocząć: ")

    match operacja:
        case 1:
            print(str(mainLista))
        case 2:
            dane = input("Podaj oddzielone pojedyńczymi spacjami:\nNazwę gwiazdy,"
                         " kąt w pionie, kąt w poziomie, odległość od ziemi w latach świetlnych")
            dane = dane.split()
            if len(dane) == 4:
                try:
                    star = Star(dane[0], tuple(int(dane[i]) for i in range(1, 4)))

                except Exception as e:
                    print(e)
                    