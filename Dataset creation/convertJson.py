import json
import pandas as pd

with open("answers_1000.json", "r") as read_file:
    data = json.load(read_file)

json_string = json.dumps(data)

df = pd.read_json(json_string)
print(df['answer'])
print(df['is_right'])