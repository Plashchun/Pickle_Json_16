#1
import pickle

key_slovo = {'key1': 'slovo1', 'key2': 'slovo2'}, {'key3': 'slovo3', 'key4': 'slovo4'}

with open('key_slovo.pickle', 'wb') as file:
    pickle.dump(key_slovo, file)

#2
import json

A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}

C = A.copy()
for key, money in B.items():
    if key in C:
        my_value = C[key]
        if isinstance(my_value, list):
            my_value.append(money)
        else:
            C[key] = [my_value, money]
    else:
        C[key] = money

with open('result.json', 'w') as file:
    json.dump(C, file)