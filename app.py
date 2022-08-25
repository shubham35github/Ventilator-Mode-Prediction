import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('vent_rf.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        
        tvi = float(request.form['tvi'])
        etime = float(request.form['e-time'])
        itime = float(request.form['i-time'])
        tve = float(request.form['tve'])
        eiratio = float(request.form['eiratio'])
        minP = float(request.form['minP'])
        PEEP = float(request.form['PEEP'])
        
        
        """ mode_encodings = {
            }
        team_encode_dict = {
                    'mode': mode_encodings
                    }"""
     
        
        
        inp = [tvi, etime, itime, tve, eiratio, minP, PEEP]
        inp = np.array(inp).reshape((1, -1))
        prediction = model.predict(inp)
                
        #output = list(team_encodings.keys())[list(mode_encode_dict['mode'].values()).index(prediction)]
        str1 = " "
        output = str1.join(prediction)
        #if prediction
        """if team1 == team2:
            return render_template('index.html', prediction_text="Are you kidding me!!")
        elif toss_winner != team1 and toss_winner != team2:
            return render_template('index.html', prediction_text="Dude! Enough of making fun!!")
        elif output != team2 and output != team1:
           return render_template('index.html', prediction_text="Cannot Predict the winner")
        elif toss_decision != 0 and toss_decision != 1:
           return render_template('index.html', prediction_text="There is only Batting and Fielding")
        else:
            return render_template('index.html', prediction_text="The Winner would be:" + output)"""
        
    return render_template('index.html', prediction_text="The best mode for the given parameters would be:" + output)


if __name__ == "__main__":
    app.run(debug=True)