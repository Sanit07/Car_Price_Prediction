from flask import Flask,request,jsonify,render_template
import pickle
import requests
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler 

app=Flask(__name__)
model=pickle.load(open('random_forest_regression_model_1.pkl', 'rb'))


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        
        year=int(request.form['Year'])
        year=2020-year
        km_driven=int(request.form['Kms_Driven'])
        present_price=int(request.form['present_price'])
        
        owner=request.form['Owner']
        if owner =='First Owner':
            owner_Fourth_Above_Owner=0
            owner_Second_Owner=0
            owner_Test_Drive_Car=0
            owner_Third_Owner=0
        elif owner =='Second Owner':
            owner_Fourth_Above_Owner=0
            owner_Second_Owner=1
            owner_Test_Drive_Car=0
            owner_Third_Owner=0
        elif owner =='Third Owner':
            owner_Fourth_Above_Owner=0
            owner_Second_Owner=0
            owner_Test_Drive_Car=0
            owner_Third_Owner=1
        elif owner =='Fourth & Above Owner':
            owner_Fourth_Above_Owner=1
            owner_Second_Owner=0
            owner_Test_Drive_Car=0
            owner_Third_Owner=0
        else:
            owner_Fourth_Above_Owner=0
            owner_Second_Owner=0
            owner_Test_Drive_Car=1
            owner_Third_Owner=0
            
        fuel=request.form['Fuel_Type_Petrol']
        if fuel == 'Petrol':
            fuel_Diesel	=0
            fuel_Electric=0
            fuel_LPG=0
            fuel_Petrol=1
        elif fuel == 'Diesel':
            fuel_Diesel	=1
            fuel_Electric=0
            fuel_LPG=0
            fuel_Petrol=0
        elif fuel == 'LPG':
            fuel_Diesel	=0
            fuel_Electric=0
            fuel_LPG=1
            fuel_Petrol=0
        elif fuel == 'Electric':
            fuel_Diesel	=0
            fuel_Electric=1
            fuel_LPG=0
            fuel_Petrol=0
        else:
            fuel_Diesel	=0
            fuel_Electric=0
            fuel_LPG=0
            fuel_Petrol=0
        seller=request.form['Seller_Type_Individual']
        if seller == 'Individual':
            seller_type_Individual=1
            seller_type_Trustmark_Dealer=0
        elif seller == 'Trust Mark Dealer':
            seller_type_Individual=0
            seller_type_Trustmark_Dealer=1
        else:
            seller_type_Individual=0
            seller_type_Trustmark_Dealer=0
        transmission_Manual = int(request.form['Transmission_Manual'])
        
        prediction=model.predict([[year,km_driven,present_price,fuel_Diesel,fuel_Electric,fuel_LPG,fuel_Petrol,seller_type_Individual,seller_type_Trustmark_Dealer,transmission_Manual,owner_Fourth_Above_Owner,owner_Second_Owner,owner_Test_Drive_Car,owner_Third_Owner]])
        
        output=round(prediction[0],2)  
        
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at RS. {}".format(output))
            
            
            
    else:
        return render_template('index.html')
        
            
        

if __name__=='__main__':
    app.run(debug=True)