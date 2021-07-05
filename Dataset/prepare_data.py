from Dataset import file_sashimi
from Dataset import stringify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
import pandas as pd

def code_to_lex(txt):
    return stringify.to_ascii(stringify.findType(file_sashimi.sashimi_str(txt)))

def return_prediction_moy(txt):
    model = load_model('Machine_Learning/modeles/model_moyenne')
    df = pd.DataFrame([{"answer":code_to_lex(txt)}])
    tok = Tokenizer(char_level=True)
    tok.fit_on_texts(df.answer)
    X = tok.texts_to_sequences(df["answer"])
    X = sequence.pad_sequences(X, maxlen=265)
    print(model.predict(X))



return_prediction_moy("float average(float values[], int n_vals){int i;float res=0;for(i=0;i<n_vals;i++)res+=values[i];return (res/n_values);")