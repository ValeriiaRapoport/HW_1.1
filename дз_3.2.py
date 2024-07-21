import json
def sum_sales(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            data = json.load(infile)

        total_sales = {}    # Словарь для хранения суммарных продаж

        for store, products in data.items():
            for product, quantity in products.items():
                if product in total_sales:
                    total_sales[product] += quantity
                else:
                    total_sales[product] = quantity

        with open(output_filename, 'w') as outfile:
            json.dump(total_sales, outfile, indent=4)
            print(f"Обработка произошла успешно. Список продуктов и их количество записаны в файл {output_filename}. ")

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_filename} не найден.")
    except json.JSONDecodeError:
        print("Ошибка: Не удалось прочитать данные из файла. Проверьте формат.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

sum_sales('input.txt', 'output.txt')
