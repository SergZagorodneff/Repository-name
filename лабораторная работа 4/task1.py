# TODO решите задачу
import json
def task() -> float:
    with open('input.json', 'r') as f:
        data = json.load(f)
    sum_ = 0
    for item in data:
        if 'score' in item and 'weight' in item:
            product = item['score'] * item['weight']
            sum_ += product
    return round(sum_, 3)

print(task())
