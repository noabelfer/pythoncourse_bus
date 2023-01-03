import csv
import json

def json2csv(file_path_json, file_path_csv):
    data = {}
    with open(file_path_json,'r') as file:
        data = json.load(file)

    #     reader = csv.reader(file)
    #     data = [{k: v for k, v in row.items()} for row in reader]
    with open(file_path_csv, "w") as f:
        writer = csv.writer(f)
        print(data)
        for key, value in data.items():
            # print(key, value)
            writer.writerow((key, value))
    # print(data)

a = json2csv("/Users/noabelfer/Downloads/sample2.json", 'D6files')