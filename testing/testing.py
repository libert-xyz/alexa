from flask import Flask
from flask_ask import question, Ask, statement
import logging

app = Flask(__name__)
ask = Ask(app, '/')

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


### REQUEST ###

@ask.launch
def launch():
    return statement('Welcome to Libert testing demo')

@ask.intent('HelloIntent')
def hello():
    return statement('Catch Me Outside, How Bout That')

@ask.intent('QuestionIntent')
def quest():
    return question('How was your day?')

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement('Stopping')

@ask.session_ended
def session_ended():
    log.debug('Session Ended')
    return "", 200

### RESPONSE ###

@ask.intent('MyNameIsIntent')
def my_name_is(firstname):
    msg = 'Your name is {}'.format(firstname)
    return statement(msg)

@ask.intent('WhatIsMyNameIntent')
def what_my_name():
    return question('What is your name?').reprompt('May I please have your name')

if __name__ == '__main__':
    app.run(debug=True)
