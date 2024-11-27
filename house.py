class House:
    def __init__(self, name, number_of_floors):
        """
        Инициализация объекта дома.
        :param name: Название дома.
        :param number_of_floors: Количество этажей в доме.
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """
        Перемещение на заданный этаж.
        :param new_floor: Номер этажа, на который нужно попасть.
        """
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        """
        Возвращает количество этажей здания.
        :return: Количество этажей (int).
        """
        return self.number_of_floors

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        :return: Строка с названием и количеством этажей.
        """
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Ожидается: "Название: ЖК Эльбрус, кол-во этажей: 10"
print(h2)  # Ожидается: "Название: ЖК Акация, кол-во этажей: 20"

print(len(h1))  # Ожидается: 10
print(len(h2))  # Ожидается: 20

