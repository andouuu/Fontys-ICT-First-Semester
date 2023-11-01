
from flask import Flask
from flask import render_template

from datetime import datetime
import random
def current_time():
    rightNow = datetime.now()
    time = rightNow.strftime("%I:%M%p")
    time = time.lstrip('0')
    time = time.lower()
    day = rightNow.strftime("%A")

    return "It is " + time + " on " + day + "."

def light_level():
    r=random.choice(range(0,1001))
    return r

@app.route('/')
def calculate():
    return render_template('index.html',
                           currentTime=current_time(),
                           lightLevel=light_level())


app.run()