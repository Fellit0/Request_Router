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
    
def normalize_text(dictionary):
    dictionary['text'] = dictionary['text'].lower().replace('ё', 'е')
    return dictionary

def category(dictionary):
    record = normalize_text(dictionary)
    words_access = ['войти', 'пароль', 'нет доступа']
    words_billing = ['оплата', 'счет', 'тариф', 'спис']
    words_bug = ['ошибка', 'не работает', 'падает', 'недоступен']
    if any(word in record['text'] for word in words_access):
        return 'access'
    if any(word in record['text'] for word in words_billing):
        return 'billing'
    if any(word in record['text'] for word in words_bug):
        return 'bug'
    return 'other'

def priority(dictionary):
    record = normalize_text(dictionary)
    words_high = ['срочно', 'критично', 'недоступен всем']
    current_category = category(record)
    if any(word in record['text'] for word in words_high):
        return 'high'
    if current_category == 'access' or current_category == 'bug': 
        return 'medium'
    return 'low'

def routing(dictionary):
    new_dict = {'id' : dictionary['id'],
                 'category' : category(dictionary),
                   'priority' : priority(dictionary)}
    return new_dict

def result_record(file):
    results = []
    for step in read_file(file):
        results.append(routing(step))
    return results
