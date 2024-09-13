import sys


def check_input(n: int, m: int) -> bool:
    if isinstance(n, int) and isinstance(m, int):
        if n > 0 and 1 < m <= n:
            return True
        else:
            return False
    else:
        return False


def refactor_list(lst: list, start_from: int) -> list:
    index = lst.index(start_from)
    lst = lst[index:] + lst[0:index]
    return lst


def check_intervals_result(result: list) -> bool:
    if result:
        if str(result[0])[0] == str(result[-1])[-1]:
            return False
        else:
            return True
    return True


def get_result(intervals_list: list) -> int:
    result = ''
    for i in intervals_list:
        result += i[0]
    return int(result)


def get_intervals_list(max_num: int, step: int) -> list:
    circle = [i for i in range(1, max_num + 1)]
    interval = ''
    intervals_list = []
    while check_intervals_result(intervals_list):
        for i in range(step):
            interval += str(circle[i])
            if i + 1 == step:
                intervals_list.append(interval)
                interval = ''
                circle = refactor_list(lst=circle, start_from=circle[i])
    return intervals_list


def main(n: int, m: int) -> None:
    if check_input(n, m):
        intervals_list = get_intervals_list(max_num=n, step=m)
        print(get_result(intervals_list))
    else:
        print('Введен неверный формат данных')


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
