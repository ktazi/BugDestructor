from flask import Flask, request, render_template

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
    text += "tamêrelapute"
    pouet = text

    return render_template('Interface/Index.html', pouet=pouet, fudge=fudge)



if __name__ == '__main__':
    app.run()
