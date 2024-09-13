import sys

from pathlib import Path


def get_data_from_file(file_path: Path) -> list:
    # Можно вводить числа через пробелы, запятые, запятые с пробелом, \n
    data_list = []
    with file_path.open(mode='r') as f:
        for i in f:
            i = i.replace(',', ' ')
            i = i.replace(', ', ' ')
            temp_list = i.split()
            for j in range(len(temp_list)):
                try:
                    data_list.append(int(temp_list[j]))
                except:
                    continue
    return data_list


def get_target_num(num_list: list) -> int:
    # Убираем дубликаты
    num_list = set(num_list)
    num_list = list(num_list)
    target_num = num_list[len(num_list)//2]
    return target_num


def count_min_steps(num_list: list) -> int:
    target_num = get_target_num(num_list)
    counter = 0
    for i in num_list:
        while i != target_num:
            if i > target_num:
                i -= 1
                counter += 1
            if i < target_num:
                i += 1
                counter += 1
    return counter


def main(file_name_or_path: str) -> None:
    try:
        file_path = Path(file_name_or_path)
        num_list = get_data_from_file(file_path)
        print(count_min_steps(num_list))
    except:
        print('Проверьте правильность ввода пути или имени файла')


if __name__ == '__main__':
    main(sys.argv[1])
