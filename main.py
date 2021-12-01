from typing import List

from work_with_file import Work_with_file


# чтение txt -> сортировка -> запись yaml -> чтение yaml -> вывод данных 
filename_txt = "result.txt"
filename_yaml = "result.yaml"
file = Work_with_file()
data = file.read_json_txt(filename_txt)
parameters: list[str] = ["age", "passport_number"]
file.merge_sort_data(data,  parameters[0])
file.write_yaml(filename_yaml, data)
tmp = file.read_yaml(filename_yaml)
file.print_collection(tmp, 10)

