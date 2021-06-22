import pandas as pd

def createDataFrame(liste, boolean):
    df = pd.DataFrame(liste, columns =['Content'])
    df['Validity'] = boolean
    print(df)

liste = ["abcerdf", "djziq", "jdopqdqad", "dzqopdpq"]
boolean = True
createDataFrame(liste, boolean)