import sys

from pathlib import Path


def get_circle(filename_or_path: str) -> tuple:
    # Можно вводить числа через пробелы, запятые, запятые с пробелом, \n
    path = Path(filename_or_path)
    circle = []
    with path.open(mode='r') as f:
        for i in f:
            i = i.replace(',', ' ')
            i = i.replace(', ', ' ')
            temp_list = i.split()
            for j in range(len(temp_list)):
                try:
                    circle.append(int(temp_list[j]))
                except:
                    continue
    if len(circle) == 3:
        center, radius = tuple(circle[0:2]), circle[2]
        return center, radius
    raise Exception('Неверный формат данных центра окружности и радиуса')


def get_points_coordinates(filename_or_path: str) -> tuple:
    # Можно вводить числа через пробелы, запятые, запятые с пробелом, \n
    path = Path(filename_or_path)
    coords = []
    temp_coord = []
    with path.open(mode='r') as f:
        for i in f:
            i = i.replace(',', ' ')
            i = i.replace(', ', ' ')
            temp_list = i.split()
            for j in range(len(temp_list)):
                try:
                    temp_coord.append(int(temp_list[j]))
                    if len(temp_coord) == 2:
                        coords.append(tuple(temp_coord))
                        temp_coord.clear()
                except:
                    continue
    if temp_coord:
        # Если в цикле не очистили этот список, значит, не хватило данных для заполнения, т.е. не хватает координаты
        raise Exception('Неверный формат данных координат точки (нечетное количество координат)')
    if 1 <= len(coords) <= 100:
        return tuple(coords)
    raise Exception('Неверный формат данных координат точки или дано более 100 точек')


def get_result(circle_coords: tuple[tuple[int] | int], points_coords: tuple[tuple[int]]) -> str:

    # Если точка лежит на заданной окружности, то координаты этой точки удовлетворяют уравнению
    # (x - a)**2 + (y - b)**2 == r**2, где x, y - коорданты точки, a,b - координаты центра окружности,
    # r - радиус окружности

    result = ''
    a = circle_coords[0][0]
    b = circle_coords[0][1]
    r = circle_coords[1]
    for i in points_coords:
        if (i[0] - a)**2 + (i[1] - b)**2 == r**2:
            result += '0\n'
        if (i[0] - a)**2 + (i[1] - b)**2 < r**2:
            result += '1\n'
        if (i[0] - a)**2 + (i[1] - b)**2 > r**2:
            result += '2\n'
    return result.rstrip('\n')


def main(circle_filename_or_path: str, points_filename_or_path) -> None:
    circle = get_circle(circle_filename_or_path)
    points = get_points_coordinates(points_filename_or_path)
    result = get_result(circle_coords=circle, points_coords=points)
    print(result)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

