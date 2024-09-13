import sys
import json

from pathlib import Path


def parse_json(filename_or_path: str) -> dict:
    path = Path(filename_or_path)
    with path.open('r') as f:
        data = json.load(f)
    return data


def write_report_json(data: dict, path: str) -> None:
    path = Path(path)
    with path.open('w') as f:
        json.dump(data, f)


def insert_values_into_tests(tests: dict, values: dict) -> dict:
    for i in tests['tests']:
        if not i['value']:
            for j in values['values']:
                if i['id'] == j['id']:
                    i['value'] = j['value']
        if 'values' in i.keys():
            insert_values_into_nested_data(values_field=i['values'], values_json=values)
    return tests


def insert_values_into_nested_data(values_field: list[dict], values_json: dict) -> None:
    # рекурсивная функция, проваливается в поле 'values' и проставляет значение в поле 'value', если оно присутствует
    # если ключа 'values' нет, рекурсия останавливается
    for i in values_field:
        if 'value' in i.keys() and 'values' in i.keys():
            if not i['value']:
                for j in values_json['values']:
                    if i['id'] == j['id']:
                        i['value'] = j['value']
            insert_values_into_nested_data(i['values'], values_json)

        elif 'value' in i.keys() and 'values' not in i.keys():
            if not i['value']:
                for j in values_json['values']:
                    if i['id'] == j['id']:
                        i['value'] = j['value']

        elif 'value' not in i.keys() and 'values' in i.keys():
            insert_values_into_nested_data(i['values'], values_json)

        else:
            return None


def main(filename_or_path_tests_json: str,
         filename_or_path_values_json: str,
         filename_or_path_report_json: str) -> None:

    tests = parse_json(filename_or_path_tests_json)
    values = parse_json(filename_or_path_values_json)
    report_file = filename_or_path_report_json

    result = insert_values_into_tests(tests=tests, values=values)
    write_report_json(result, report_file)


if __name__ == '__main__':
    main(filename_or_path_tests_json=sys.argv[1],
         filename_or_path_values_json=sys.argv[2],
         filename_or_path_report_json=sys.argv[3])
