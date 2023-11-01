from flask import Flask
from flask import render_template

from datetime import datetime
import random

app=Flask(__name__)
def current_time():
    rightNow = datetime.now()
    time = rightNow.strftime("%I:%M%p")
    time = time.lstrip('0')
    time = time.lower()
    day = rightNow.strftime("%A")

    return  time + " " + day

def light_level():
    r=random.choice(range(0,1001))
    return r


measurementsList=[]


    

@app.route('/')
def calculate():
    currentTimeMeasurement=current_time()
    lightLevelMeasurement=light_level()
    currMeasure=[currentTimeMeasurement,lightLevelMeasurement]
    measurementsList.append(currMeasure)
    if len(measurementsList)>10:
        measurementsList.pop(0)
    return render_template('index.html',
                           currentTime=currentTimeMeasurement,
                           lightLevel=lightLevelMeasurement,
                           
                           len=len(measurementsList),
                           measurements=measurementsList)


app.run()