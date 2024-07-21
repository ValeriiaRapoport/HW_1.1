def filter_cities_by_population(threshold):
    input_file = 'cities.txt'
    output_file = 'filtered_cities.txt'

    cities = []

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                city, population = line.strip().split(':')
                population = int(population)
                if population > threshold:
                    cities.append((city, population))
    except FileNotFoundError:
        print(f'Файл {input_file} не найден. Пожалуйста, убедитесь, что файл существует и попробуйте снова.')
        return
    cities.sort()

    with open(output_file, 'w', encoding='utf-8') as file:
        for city, population in cities:
            file.write(f'{city}:{population}\n')

try:
    threshold = int(input("Введите число: "))
except ValueError:
    print('Пожалуйста, введите допустимое число.')
else:
    filter_cities_by_population(threshold)
    print(f'Города с населением больше {threshold} записаны в файл filtered_cities.txt')
