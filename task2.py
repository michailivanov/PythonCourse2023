import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # считать содержимое csv файла
    with open(INPUT_FILENAME) as f:
        reader = csv.DictReader(f)
        json_data = [row for row in reader]

    # Сериализация в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(json_data, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
