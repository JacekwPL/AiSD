class Star:
    def __init__(self, name: str, position: tuple):
        self.__name = name
        self.__pos = position

    def __str__(self):
        return f'{self.__name} {self.__pos}'

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getPosition(self):
        return self.__pos

    def setPosition(self, position: tuple):
        self.__pos = position


class ListOfStars:
    def __init__(self):
        self.Lista = {}

    def __len__(self):
        return len(self.Lista)

    def __str__(self) -> str:
        xpp = ""
        for key in self.Lista.keys():
            xpp += f'Nazwa gwiazdy: {key}, pozycja: {self.Lista[key]}'

        return xpp

    def importFromFile(self, path):
        pass

    def add(self, star: Star):
        pass

    def __removeStar(self, star: Star):
        pass

    def __removeIndex(self, index: int):
        pass

    def remove(self, arg):
        if isinstance(arg, int):
            self.__removeIndex(arg)
        elif isinstance(arg, Star):
            self.__removeStar(arg)
        else:
            raise ValueError('remove() only can be usage with class: Star or int: integer')

    def exportToFile(self, path):
        with open(path, 'w+', encoding='UTF-8') as f:

            print(str(self), file=f)

            f.close()


if __name__ == '__main__':
    d = {'Siema': 'bili'}

    d.items()

    d['elo'] = "też bili"

    print(len(d))
