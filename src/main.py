import json
import csv

def read_json(file_path_json):
    with open (file_path_json, "r", encoding="utf-8") as f:

        data = json.load(f)

    return clean_str(data)

def read_csv(file_path_csv):
    with open(file_path_csv, "r", encoding="utf-8") as f:

        reader = csv.DictReader(f)
        result = []
        for i in reader:
            result.append(i)
    return clean_str(result)

def clean_str(array):
    for dictionary in array:
        dictionary['id'] = str(dictionary['id']).strip()
        
        dictionary['text'] = str(dictionary['text']).strip()
        if dictionary['id'] == '' or dictionary['text'] == '':
            raise ValueError()
    return array

def read_file(file):
    file_low = file.lower()

    if file_low.endswith('.json'):
        return read_json(file)
    if file_low.endswith('.csv'):
        return read_csv(file)
    raise ValueError()
    
