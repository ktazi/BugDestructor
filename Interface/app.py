from flask import Flask, request, render_template
from Dataset.prepare_data import return_prediction_moy
app = Flask(__name__)

pouet = ""
fudge = ""

@app.route('/')
def index():

    return render_template('Interface/Index.html', pouet=pouet)


@app.route('/', methods=['POST'])
def submit():
    text = request.form['text']
    fudge = text
    text = return_prediction_moy(text)
    pouet = text
    return render_template('Interface/Index.html', pouet=pouet, fudge=fudge)



if __name__ == '__main__':
    app.run()
