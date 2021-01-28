"""
Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
И получить объект: словарь из предыдущего задания.
"""
import pickle
import json

with open('group.pickle', 'rb') as f:
    result_1 = pickle.load(f)

with open('group.json', 'r', encoding='utf-8') as f:
    result = json.load(f)

print(result)
print(type(result))

print(result_1)
print(type(result_1))




