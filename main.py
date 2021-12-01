import yaml
from tqdm import tqdm

class Read_file_yaml:
    _filename: str
    _array: list = []

    def __init__(self, filename: str) -> None:
        self._filename = filename
        data = yaml.safe_load(open(self._filename))
        for i in data:
            self._array.append(i)

    def array_list(self) -> list:
        return self._array.copy()


class Data:
    _collection: list

    def __init__(self, data: list):
        self._collection = data


class Write_file:
    _filename: str

    def __init__(self, filename) -> None:
        self._filename = filename

    def write_file(self, collection: list) -> None:

        tmp = []
        for i in tqdm(range(collection.get_count_of_profile()), desc="Запись корректных данных в файл: ", ncols=100):
            if collection.check_valid_information(i):
                tmp.append(collection.get_profile(i))
        yaml.dump(tmp, open(self._filename, "w", encoding="windows-1251"), ensure_ascii=False, sort_keys=False, indent=4)

import argparse


parser = argparse.ArgumentParser("Input & output path")
parser.add_argument("-read", type=str, default="result.txt", help="read file")
parser.add_argument("-write", type=str, default="result.yaml", help="write file")
pars = parser.parse_args()
lines = Read_file_yaml(pars.read)
data = Data(lines.array_list())
write = Write_file(pars.write)
write.write_file(data)