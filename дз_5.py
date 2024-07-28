import random
import threading
import time

class Animal:
    def __init__(self, name, size, diet, habitat, lifespan):
        self.name = name
        self.size = size
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan
        self.individuals = []

    def add_individual(self, age, satiety, sex):
        self.individuals.append({
            'age': age,
            'satiety': satiety,
            'sex': sex
        })

    def reproduce(self):
        if self.habitat == 'вода':
            condition = lambda ind: ind['satiety'] > 50
            new_satiety = 23
            offspring_count = 10
        elif self.habitat == 'воздух':
            condition = lambda ind: ind['satiety'] > 42 and ind['age'] > 3
            new_satiety = 64
            offspring_count = 4
        elif self.habitat == 'земля':
            condition = lambda ind: ind['satiety'] > 20 and ind['age'] > 5
            new_satiety = 73
            offspring_count = 2
        else:
            return

        for ind in self.individuals:
            if condition(ind):
                for _ in range(offspring_count):
                    self.add_individual(0, new_satiety, random.choice(['мужской', 'женский']))

    def manual_reproduce(self):
        if self.habitat == 'вода':
            condition = lambda ind: ind['satiety'] > 50
            new_satiety = 23
            offspring_count = 10
        elif self.habitat == 'воздух':
            condition = lambda ind: ind['satiety'] > 42 and ind['age'] > 3
            new_satiety = 64
            offspring_count = 4
        elif self.habitat == 'земля':
            condition = lambda ind: ind['satiety'] > 20 and ind['age'] > 5
            new_satiety = 73
            offspring_count = 2
        else:
            return False

        male_count = sum(1 for ind in self.individuals if ind['sex'] == 'мужской' and condition(ind))
        female_count = sum(1 for ind in self.individuals if ind['sex'] == 'женский' and condition(ind))

        if male_count > 0 and female_count > 0:
            for _ in range(offspring_count):
                self.add_individual(0, new_satiety, random.choice(['мужской', 'женский']))
            return True
        return False

    def age_and_feed(self, plant_food):
        events = []
        for ind in self.individuals[:]:
            ind['age'] += 1
            if ind['age'] >= self.lifespan:
                plant_food += self.size
                self.individuals.remove(ind)
                events.append(f"{self.name} умер от старости.")
            elif ind['satiety'] < 10:
                plant_food += self.size
                self.individuals.remove(ind)
                events.append(f"{self.name} умер от голода.")
            else:
                if self.diet == 'травоядное':
                    if plant_food > 0:
                        plant_food -= 1
                        ind['satiety'] += 26
                        events.append(f"{self.name} поел растительную пищу.")
                    else:
                        ind['satiety'] -= 9
                        events.append(f"{self.name} не нашел растительную пищу и потерял сытость.")
                elif self.diet == 'хищник':
                    if random.random() < 0.5:
                        ind['satiety'] += 53
                        events.append(f"{self.name} успешно охотился.")
                    else:
                        ind['satiety'] -= 16
                        events.append(f"{self.name} неудачно охотился и потерял сытость.")
                else:
                    ind['satiety'] -= 9
                    events.append(f"{self.name} не нашел пищу и потерял сытость.")
                ind['satiety'] = max(0, ind['satiety'])
        return plant_food, events


class Ecosystem:
    def __init__(self):
        self.animals = []
        self.plant_food = 0

    def add_animal_species(self, name, size, diet, habitat, lifespan):
        animal = Animal(name, size, diet, habitat, lifespan)
        self.animals.append(animal)
        # Создание случайных особей для каждого вида
        for _ in range(random.randint(5, 15)):
            age = random.randint(0, lifespan)
            satiety = random.randint(10, 100)
            sex = random.choice(['мужской', 'женский'])
            animal.add_individual(age, satiety, sex)

    def add_individual(self, species_name, age, satiety, sex):
        for animal in self.animals:
            if animal.name == species_name:
                animal.add_individual(age, satiety, sex)

    def increase_plant_food(self, amount):
        self.plant_food += amount

    def view_individuals(self):
        for animal in self.animals:
            print(f"Вид: {animal.name} (Количество: {len(animal.individuals)})")
            for ind in animal.individuals:
                print(f"  Возраст: {ind['age']}, Сытость: {ind['satiety']}%, Пол: {ind['sex']}")

    def simulate_time_step(self):
        events = []
        for animal in self.animals:
            self.plant_food, new_events = animal.age_and_feed(self.plant_food)
            animal.reproduce()
            events.extend(new_events)
        return events


def time_step(ecosystem, interval):
    while True:
        time.sleep(interval)
        events = ecosystem.simulate_time_step()
        print("\n--- События шага времени ---")
        for event in events:
            print(event)


def main():
    ecosystem = Ecosystem()

    # Определение 12 видов животных
    ecosystem.add_animal_species("Акула", 500, "хищник", "вода", 30)
    ecosystem.add_animal_species("Лосось", 5, "травоядное", "вода", 5)
    ecosystem.add_animal_species("Орёл", 6, "хищник", "воздух", 15)
    ecosystem.add_animal_species("Попугай", 1, "травоядное", "воздух", 50)
    ecosystem.add_animal_species("Лев", 190, "хищник", "земля", 20)
    ecosystem.add_animal_species("Слон", 6000, "травоядное", "земля", 70)
    ecosystem.add_animal_species("Крокодил", 1000, "хищник", "вода", 70)
    ecosystem.add_animal_species("Лягушка", 0.2, "травоядное", "вода", 10)
    ecosystem.add_animal_species("Ястреб", 1, "хищник", "воздух", 20)
    ecosystem.add_animal_species("Кролик", 2, "травоядное", "земля", 9)
    ecosystem.add_animal_species("Тигр", 220, "хищник", "земля", 25)
    ecosystem.add_animal_species("Жираф", 800, "травоядное", "земля", 25)

    # Установка начального интервала обновления в 1 минуту (60 секунд)
    interval = 60

    # Запуск потока временного шага
    thread = threading.Thread(target=time_step, args=(ecosystem, interval))
    thread.daemon = True
    thread.start()

    while True:
        print("\n--- Управление экосистемой ---")
        print("1. Добавить особь")
        print("2. Увеличить количество растительной пищи")
        print("3. Просмотр всех особей")
        print("4. Установить интервал обновления")
        print("5. Смоделировать размножение")
        print("6. Продолжить")
        print("7. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            species_name = input("Введите название вида: ")
            age = int(input("Введите возраст: "))
            satiety = int(input("Введите сытость (0-100): "))
            sex = input("Введите пол (мужской/женский): ")
            ecosystem.add_individual(species_name, age, satiety, sex)
        elif choice == "2":
            amount = int(input("Введите количество растительной пищи для добавления: "))
            ecosystem.increase_plant_food(amount)
        elif choice == "3":
            ecosystem.view_individuals()
        elif choice == "4":
            interval = int(input("Введите новый интервал обновления в секундах: "))
            thread = threading.Thread(target=time_step, args=(ecosystem, interval))
            thread.daemon = True
            thread.start()
        elif choice == "5":
            species_name = input("Введите название вида для размножения: ")
            for animal in ecosystem.animals:
                if animal.name == species_name:
                    if animal.manual_reproduce():
                        print(f"{species_name} успешно размножился.")
                    else:
                        print(f"Размножение {species_name} не удалось.")
        elif choice == "6":
            continue
        elif choice == "7":
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()