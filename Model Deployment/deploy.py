from flask import Flask,render_template,request
import pickle
 
app = Flask(__name__)

#load the model

model = pickle.load(open('moviecollectionmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('movie_predcition_FE.html',**locals())

@app.route('/predict', methods=['POST','GET'])
def predict():
    ME = float(request.form['ME'])
    PE = float(request.form['PE'])
    Budg = float(request.form['Budg'])
    ML = float(request.form['ML'])
    ACT_r = float(request.form['ACT_r'])
    ACS_r = float(request.form['ACS_r'])
    DR = float(request.form['DR'])
    PR = float(request.form['PR'])
    CR = float(request.form['CR'])
    TV = float(request.form['TV'])
    TH = float(request.form['TH'])
    AVG_ACT = float(request.form['AVG_ACT'])
    TD = float(request.form['TD'])
    Genre = request.form['Genre']
    if (Genre == "action"):
        ga = 1
        gc = 0
        gt = 0
        gd = 0
    elif (Genre == "comdey"):
        ga = 0
        gc = 1
        gt = 0
        gd = 0
    elif (Genre == "drama"):
        ga = 0
        gc = 0
        gt = 1
        gd = 1
    else:
        ga = 0
        gc = 0
        gt = 1
        gd = 0
    result = model.predict([[ME,PE,Budg,ML,ACT_r,ACS_r,DR,PR,CR,TV,TH,AVG_ACT,TD,ga,gc,gd,gt]])[0]
    return render_template('movie_predcition_FE.html',**locals())

if __name__ == '__main__':
    app.run(debug=True)    
