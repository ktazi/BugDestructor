from Dataset import file_sashimi
from Dataset import stringify
from tensorflow.keras.models import load_model
from tensorflow import expand_dims
import numpy as np

def code_to_lex(txt):
    return stringify.to_ascii(stringify.findType(file_sashimi.sashimi_str(txt)))

def return_prediction_moy(txt):
    model = load_model('Machine_Learning/modeles/model_moyenne')
    print(model.summary())
    #print(model.predict(code_to_lex(txt), batch_size=1))


return_prediction_moy("float average(float values[], int n_vals){int i;float res=0;for(i=0;i<n_vals;i++)res+=values[i];return (res/n_values);")