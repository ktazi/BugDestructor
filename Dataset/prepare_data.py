from Dataset import file_sashimi
from Dataset import stringify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
import pandas as pd

def code_to_lex(txt):
    return stringify.to_ascii(stringify.findType(file_sashimi.sashimi_str(txt)))

def return_prediction_moy(txt):
    model = load_model('../Machine_Learning/modeles/model_moyenne')
    df = pd.DataFrame([{"answer":code_to_lex(txt)}])
    tok = Tokenizer(char_level=True)
    tok.fit_on_texts(df.answer)
    X = tok.texts_to_sequences(df["answer"])
    X = sequence.pad_sequences(X, maxlen=265)
    pre = model.predict(X)[0][0]
    return ("Nous estimons que le programme ne compile pas "if pre < 0.5 else "Nous estimons que le programme compile") + "\n\nSur une échelle de 0 à 1 (ou 0 = certitude que cela ne compile pas, 1= certitude que cela compile), notre modèle lui a donné une note de "+str(pre)

#return_prediction_moy("float average(float values[], int n_vals){int i;float res=0;for(i=0;i<n_vals;i++)res+=values[i];return (res/n_values);")