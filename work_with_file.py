import json
import yaml


class Work_with_file:

    def __init__(self) -> None:
        pass

    def read_json_txt(self, filename):
        with open(filename, "r") as f:
            tmp = json.load(f)
            return tmp

    def write_json_txt(self, filename, collection: list) -> None:
        with open(filename, 'w') as f:
            json.dump(collection, f, default_flow_style=False)

    def read_yaml(self, filename):
        with open(filename, "r") as f:
            return yaml.safe_load(f)

    def write_yaml(self, filename, collection: list) -> None:
        with open(filename, "w") as f:
            yaml.dump(collection, f, default_flow_style=False)

    def print_collection(cls, list: list, count):
        for i in range(count):
            for key, value in list[i].items():
                print('{:15s}'.format(key), ':', value)
            print("------------------------------------------------------------------------")

    def merge_sort_data(self, data: list, parameter: int):
        self.merge_sort(data, 0, len(data), parameter)

    def merge_sort(self, data: list, start: int, end: int, parameter: int):
        if end - start > 1:
            mid = (start + end) // 2
            self.merge_sort(data, start, mid, parameter)
            self.merge_sort(data, mid, end, parameter)
            self.merge_list(data, start, mid, end, parameter)

    def merge_list(self,data, start, mid, end, parameter):
        left = data[start:mid]
        right = data[mid:end]
        k = start
        i, j = 0, 0
        while start + i < mid and mid + j < end:
            lhs = left[i]
            rhs = right[j]
            if lhs.get(parameter) <= rhs.get(parameter):
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += + 1
        if start + i < mid:
            while k < end:
                data[k] = left[i]
                i += 1
                k += 1
        else:
            while k < end:
                data[k] = right[j]
                j += 1
                k += 1