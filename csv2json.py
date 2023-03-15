import csv
import json

# csv文件转json文件
# TODO: 异常处理
def csv2json(csv_file, json_file):
    with open(csv_file, 'r', newline='',encoding='utf-8') as f:
        reader = csv.reader(f)
        if reader == None:
            return False
        json_data = {}
        for row in reader:
            json_data[row[0]] = row[1]
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        return True

if __name__ == '__main__':
    csv2json('words.csv', 'words.json')