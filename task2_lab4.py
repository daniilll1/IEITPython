# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    inp = open(INPUT_FILENAME, "r")
    outp = open(OUTPUT_FILENAME, "w")

    reader = csv.DictReader(inp)
    arr = []
    for i in reader: arr.append(i)
    ...  # TODO Сериализовать в файл с отступами равными 4
    json.dump(arr, outp, indent = 4)
    outp.close()
    inp.close()

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
