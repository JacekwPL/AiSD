from StarLogic import *

if __name__ == '__main__':
    mainLista = ListOfStars()
    mainLista.importFromFile('gwiazdy.txt')

    while True:
        print("\nJaką chcesz wykonać operację?")
        print("Wybierz operację pisząc odpowiednią liczbę")
        print("1. Wypisz wszystkie zapisane gwiazdy")
        print("2. Dodaj gwiazdę do systemu")
        print("3. Usuń gwiazdę z systemu")
        print("4. Posortuj gwiazdy względem odległości od ziemi")
        print("5. Zaimportuj gwiazdy z pliku")
        print("6. Exportuj gwiazdy do pliku")
        print("7. Zakończ działanie programu")
        print("")
        operacja = input("Wprowadź liczbę by rozpocząć: ")

        match operacja:
            case '1':
                if mainLista.__len__() == 0:
                    print("Lista gwiazd jest pusta!")

                print(str(mainLista))

            case '2':
                dane = input("Podaj oddzielone pojedyńczymi spacjami:\nNazwę gwiazdy,"
                             " kąt w pionie, kąt w poziomie, odległość od ziemi w latach świetlnych\n")
                dane = dane.split()
                if len(dane) == 4:
                    try:
                        star = Star(dane[0], tuple(float(dane[i]) for i in range(1, 4)))
                        mainLista.add(star)
                        del star
                    except Exception as e:
                        print(f'Wystąpił błąd podczas dodawania obiektu!, {e}')
                else: print("Zła ilość parametrów!")

            case '3':
                if mainLista.__len__() == 0:
                    print("Lista gwiazd jest pusta!")
                else:
                    zm = input(f'Którą gwiazdę chcesz usunąć?\n{str(mainLista)}\nNapisz liczbę lub nazwę gwiazdy: ')
                    if zm.isnumeric():
                        zm = int(zm)
                    mainLista.remove(zm)

            case '4':
                mainLista.sort()
                print(str(mainLista))

            case '5':
                zm = input("Podaj ścieżkę pliku wejściowego: ")
                try:
                    mainLista.importFromFile(zm)
                except Exception as e:
                    print(f'Wystąpił błąd podczas wczytywania pliku! {e}')

            case '6':
                zm = input("Podaj ścieżkę pliku wyjściowego: ")
                try:
                    mainLista.exportToFile(zm)
                except Exception as e:
                    print(f'Wystąpił błąd podczas eksportowania pliku! {e}')

            case '7':
                mainLista.exportToFile('gwiazdy.txt')
                exit()

            case '8':
                if 'y' == input('Czy jesteś pewny że chcesz usunąć wszystkie gwiazdy z pliku?\ny/n'):
                    mainLista.clear()

            case _:
                print("Nieprawidłowa instrukcja!")
