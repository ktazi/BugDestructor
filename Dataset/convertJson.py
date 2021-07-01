import json
import pandas as pd
from Dataset import file_sashimi
from Dataset import stringify

with open("answers_1000.json", "r") as read_file:
    data = json.load(read_file)

json_string = json.dumps(data)

df = pd.read_json(json_string)
# cut each answers in the dataframe into units (lexems)
tab = file_sashimi.sashimi_df(df)
# convert the lexems in chars
tab = stringify.lex_to_str(tab)
# put it in the dataframe
df["answers"] = pd.array(tab)
