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
            xpp += f'Nazwa gwiazdy: {key}, pozycja: {self.Lista[key]}\n'

        return xpp

    def sort(self, sl: dict = None) -> dict:
        war = False
        if sl is None:
            sl = self.Lista
            war = True

        if len(sl) == 0:
            return {}
        if len(sl) == 1:
            return sl
        dt1 = {}
        dt2 = {}
        basic = sl[list(sl.keys())[0]][2]
        keys = list(sl.keys())
        for key in keys[1::]:
            if sl[key][2] <= basic:
                dt1[key] = sl[key]
            else:
                dt2[key] = sl[key]

        if war:
            self.Lista = self.sort(dt1) | {keys[0]: sl[keys[0]]} | self.sort(dt2)
        return self.sort(dt1) | {keys[0]: sl[keys[0]]} | self.sort(dt2)

    def add(self, star: Star):
        for key in self.Lista.keys():
            if star.getPosition() == self.Lista[key]:
                raise ValueError('Two stars can\'t have same position!')
            if star.getName() == key:
                raise ValueError('Two stars can\'t have same name!')
        self.Lista[star.getName()] = star.getPosition()

    def __removeStar(self, star: Star):
        self.Lista.pop(star.getName())

    def __removeIndex(self, index: int):
        if index >= len(self.Lista) or index < 0:
            raise ValueError('invalid index')

        self.Lista.pop(list(self.Lista.keys())[index])

    def remove(self, arg):
        if isinstance(arg, int):
            self.__removeIndex(arg)
        elif isinstance(arg, Star):
            self.__removeStar(arg)
        else:
            raise ValueError('remove() only can be usage with class: Star or int: integer')

    def importFromFile(self, path):
        with open(path, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                line = line.split()
                star = Star(line[0], (float(line[1]), float(line[2]), float(line[3])))  # or tuple(line[1])
                self.add(star)

    def exportToFile(self, path):
        with open(path, 'w+', encoding='UTF-8') as f:

            for key in self.Lista.keys():
                print(f'{key} {self.Lista[key][0]} {self.Lista[key][1]} {self.Lista[key][2]}', file=f, end='\n')

            f.close()


if __name__ == '__main__':
    import random, string
    stars = [Star(random.choice(string.ascii_letters), tuple(random.randint(0, 100) for _ in range(3))) for _ in range(50)]
    lista = ListOfStars()
    for elem in stars:
        # print(str(elem))
        try:
            lista.add(elem)

        except ValueError:
            print(elem, "się dubluje")

    print(lista.__str__(), lista.__len__())
    lista.sort()
    print(lista.__str__(), lista.__len__())

    lista.exportToFile('gwiazdy.txt')

