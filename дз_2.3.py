def merge_files_lexicographically(input1, input2, output):
    def read_lines(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            lines = [line.rstrip() + '\n' for line in lines if line.strip()]
            return lines
        except FileNotFoundError:
            print(f"Ошибка: {filename} не найден.")
            return None

    lines1 = read_lines(input1)
    if lines1 is None:
        return
    lines2 = read_lines(input2)
    if lines2 is None:
        return

    combined_lines = sorted(lines1 + lines2)

    with open(output, 'w', encoding='utf-8') as output_file:
        output_file.writelines(combined_lines)
    print(f"Обработка завершена. Результат записан в output.txt.")

merge_files_lexicographically('input1.txt', 'input2.txt', 'output.txt')
