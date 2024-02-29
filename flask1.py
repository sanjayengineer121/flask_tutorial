from flask import Flask, render_template,jsonify,request
import json
app = Flask(__name__)

@app.route('/')
def home():
    return "hello"


def readdata():
    with open('a.json','r') as f:
        return json.load(f)

datax=readdata()
print(datax)
def adddata(data1):
    with open('a.json','w') as f:
        json.dump(data1,f,indent=2)
 
 
       
@app.route('/data' , methods=['POST'])
def post1():
    data=request.get_json()

    new={
        'x':data['a'],
        'y':data['b'],
    }
    datax.append(new)
    adddata(datax)
    return jsonify({"sum of numbers":(data['a']+data['b'])})

@app.route('/mul' , methods=['POST'])
def post2():
    data=request.get_json()

    new={
        'x':data['a'],
        'y':data['b'],
    }
    datax.append(new)
    adddata(datax)
    
    return jsonify({"multiply of numbers":(data['a']*data['b'])})

@app.route('/div' , methods=['POST'])
def post3():
    data=request.get_json()

    new={
        'x':data['a'],
        'y':data['b'],
    }
    
    datax.append(new)
    adddata(datax)

    return jsonify({"multiply of numbers":(data['a']/data['b'])})


app.run()