#  Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#  Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#  Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#  Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#  Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

import pickle

# 1. Определяем базовые классы
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен подклассами")

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} чирик.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} рррррр.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шшшшшш.")

# 2. Создаем классы для сотрудников
class Employee:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# 3. Используем композицию для создания класса `Zoo`
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} был добавлен в зоопарк.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} был добавлен в качестве сотрудника зоопарка.")

    def show_all_animals(self):
        for animal in self.animals:
            print(f"Animal: {animal.name}, Age: {animal.age}, Sound: ", end="")
            animal.make_sound()

    def show_all_employees(self):
        for employee in self.employees:
            print(f"Employee: {employee.name}, Role: {employee.__class__.__name__}")

# 4. Определяем функции для сохранения и загрузки данных
def save_zoo(zoo, filename):
    with open(filename, 'wb') as f:
        pickle.dump(zoo, f)
    print("Zoo data has been saved.")

def load_zoo(filename):
    with open(filename, 'rb') as f:
        zoo = pickle.load(f)
    print("Zoo data has been loaded.")
    return zoo

# 5. Создаем зоопарк и добавляем данные
zoo = Zoo()
zoo.add_animal(Bird("Попугай", 2))
zoo.add_animal(Mammal("Слон", 10))
zoo.add_employee(ZooKeeper("Иван"))
zoo.add_employee(Veterinarian("Алиса"))

# 6. Показ всех животных и сотрудников
zoo.show_all_animals()
zoo.show_all_employees()

# 7. Взаимодействие сотрудников с животными
zoo.employees[0].feed_animal(zoo.animals[0])
zoo.employees[1].heal_animal(zoo.animals[1])

# 8. Сохранение зоопарка в файл
save_zoo(zoo, 'zoo_data.pkl')

# 9. Загрузка зоопарка из файла
loaded_zoo = load_zoo('zoo_data.pkl')
loaded_zoo.show_all_animals()


