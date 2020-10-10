from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np


print('starting hosting.....')
print('Model loaded. Check http://127.0.0.1:5000/')

app = Flask(__name__)
model = pickle.load(open("bank-deposit-pred.pkl", "rb"))
@app.route('/', methods=['POST','GET']) # for calling the API from Postman #/via_postman
                    
def bank_deposit_prediction_via_postman():
    if (request.method=='POST'):
                    
        age =int(request.json['age'])
#        balance = int(request.json['balance'])
#        day = int(request.json['day'])
        print(type(age))
        
        job= str(request.json['job'])#for job mapping
        job_dict ={0:"admin", 1:"blue-collar", 2:"entreprenuer",3:"housemaid",4:"management",5:"retired",6:"self-employed",7:"services",8:"student",9:"technician",
                      10:"unemployed",11:"unknown"}
        key_list = list(job_dict.keys()) 
        val_list = list(job_dict.values())
        job = list(job_dict.keys())[list(job_dict.values()).index(job)]
        print(job)
        print(type(job))
 
        marital = str(request.json['marital'])
        mar_dict ={0:"divorced", 1:"married", 2:"single"}
        key_list = list(mar_dict.keys()) 
        val_list = list(mar_dict.values())
        marital = list(mar_dict.keys())[list(mar_dict.values()).index(marital)]
        print(marital)
        print(type(marital))

        education= str(request.json['education'])
        edu_dict ={0:"primary", 1:"secondary", 2:"tertiary",3:"unknown"}
        key_list = list(edu_dict.keys()) 
        val_list = list(edu_dict.values())
        education = list(edu_dict.keys())[list(edu_dict.values()).index(education)]

        default= str(request.json['default'])
        de_dict ={0:"no", 1:"yes"}
        key_list = list(de_dict.keys()) 
        val_list = list(de_dict.values())
        default = list(de_dict.keys())[list(de_dict.values()).index(default)]

        balance= int(request.json['balance'])

        housing= str(request.json['housing'])
        ho_dict ={0:"no", 1:"yes"}
        key_list = list(ho_dict.keys()) 
        val_list = list(ho_dict.values())
        housing = list(ho_dict.keys())[list(ho_dict.values()).index(housing)]

        loan= str(request.json['loan'])
        lo_dict ={0:"no", 1:"yes"}
        key_list = list(lo_dict.keys()) 
        val_list = list(lo_dict.values())
        loan = list(lo_dict.keys())[list(lo_dict.values()).index(loan)]

        contact= str(request.json['contact'])
        co_dict ={0:"cellular", 1:"telephone",2:"unknown"}
        key_list = list(co_dict.keys()) 
        val_list = list(co_dict.values())
        contact = list(co_dict.keys())[list(co_dict.values()).index(contact)]

        day= int(request.json['day'])

        month= str(request.json['month'])#for job mapping
        mon_dict ={0:"apr", 1:"aug", 2:"dec",3:"feb",4:"jan",5:"jul",6:"jun",7:"mar",8:"may",9:"nov",
                      10:"oct",11:"sep"}
        key_list = list(mon_dict.keys()) 
        val_list = list(mon_dict.values())
        month = list(mon_dict.keys())[list(mon_dict.values()).index(month)]

        duration= int(request.json['duration'])
        campaign= int(request.json['campaign'])
        pdays= int(request.json['pdays'])
        previous= int(request.json['previous'])

        poutcome= str(request.json['poutcome'])
        po_dict ={0:"failure", 1:"success",2:"other",3:"unknown"}
        key_list = list(po_dict.keys()) 
        val_list = list(po_dict.values())
        poutcome = list(po_dict.keys())[list(po_dict.values()).index(poutcome)]
        
        data = [age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome]
        print(data)
        data = [np.array(data)]            
        prediction = model.predict(data) #prediction
        output=str(round(prediction[0],2))
        binary_output = ("The client will subscribed a term deposit:",output)

        if(output=="0"):            
            result="NO the client will not subscribed a term deposit"
        elif(output=="1"):
            result="YES the client will subscribed a term deposit"
        else:
            pass        
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='localhost', debug=True, port='5000')
