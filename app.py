import flask
import pandas as pd
from joblib import dump, load


with open(f'model/bostonhousing.joblib', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))

    if flask.request.method == 'POST':
        rm = flask.request.form['RM']
        ptratio = flask.request.form['PTRATIO']
        lstat = flask.request.form['LSTAT']
       

        input_variables = pd.DataFrame([[rm, ptratio, lstat]],
                                       columns=['RM', 'PTRATIO', 'LSTAT'],
                                       dtype='float',
                                       index=['input'])

        predictions = model.predict(input_variables)[0]
        print(predictions)

        return flask.render_template('index.html', original_input={'RM': rm, 'PTRATIO': ptratio, 'LSTAT': lstat},
                                     result=predictions)


if __name__ == '__main__':
    app.run(debug=True)