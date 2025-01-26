from flask import Flask,render_template,url_for
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
import statistics
import time
import os
print(os.getcwd()) 
app=Flask(__name__)
@app.route('/')
def index():
     return render_template("index.html",data=volt,data1=lux,data2=alt)
@app.route('/first')
def firstPage():
    return render_template("team.html")
@app.route('/second')
def secondPage():
    return render_template("Contact_us.html")
@app.route('/third')
def thirdPage():
    return render_template("primary.html")
@app.route('/fourth')
def fourthPage():
    return render_template("secondary.html")
data = pd.read_csv("test_data1.csv")
volt = np.array(data["Voltage"])
lux = np.array(data["Lux"])
alt = np.array(data["Altitude"])
volt=volt.tolist()
lux=lux.tolist()
alt=alt.tolist()
def mean(array):
    return sum(array)/len(array)
    #lux.extend([statistics.median(lux),round(statistics.pstdev(lux),3),round(mean(lux),2)])
    #alt.extend([statistics.median(alt),round(statistics.pstdev(alt),3),round(mean(alt),2)])
if __name__ in "__main__":
    app.run(debug=True)