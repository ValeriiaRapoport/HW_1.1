def calculate_average(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total_score = 0
        student_count = 0
        student_scores = []

        for line in lines:
            if ',' in line:
                name, score_str = line.strip().split(',')
                try:
                    score = float(score_str)
                    total_score += score
                    student_count += 1
                    student_scores.append((name, score))
                except ValueError:
                    print(f"Некорректный формат оценки для студента {name}.")
            else:
                print(f"Некорректный формат строки: {line.strip()}.")
        if student_count == 0:
            print("Файл пуст или не содержит корректных данных.")
            return

        average_score = total_score / student_count

        with open(output_file, 'w', encoding='utf-8') as file:
            for name, score in student_scores:
                if score > average_score:
                    file.write(f"{name}\n")

        print(f"Средняя оценка: {average_score:.2f}")
        print(f"Имена студентов с оценкой выше средней записаны в {output_file}")

    except FileNotFoundError:
        print("Ошибка: файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

input_file = 'input.txt'
output_file = 'output.txt'
calculate_average(input_file, output_file)

