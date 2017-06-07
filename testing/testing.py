from flask import Flask
from flask_ask import question, Ask, statement, convert_errors
import logging
from datetime import date, timedelta

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


## Mapping Intent Slots ##
@ask.intent('SayHelloIntent')
def say_hello(firstname):
    return statement('Hi {} , nice to meet you'.format(firstname))

@ask.intent('SayAgeIntent', default={'firstname':'anonymous'})
def say_age(firstname,age):
    return statement('Hi {}. you are {} years old'.format(firstname,age))

## Slot Conversions ##

@ask.intent('AddIntent', convert={'first':int, 'second':int})
def add(first,second):
    thesum = first + second
    return statement('{} plus {} is {}'.format(first,second,thesum))

def preference2bool(preference):
    if preference == 'do':
        return True
    elif preference == 'do not':
        return False
    else:
        raise ValueError("must be 'do' or 'do not'")

@ask.intent("LikesIntent", convert={'preference': preference2bool})
def likes(preference):
    if convert_errors:
        return statement('I heard you say {}'.format(preference))
    if preference == True:
        return statement('You like pizza')
    elif preference == False:
        return statement("You don't like pizza")
    raise Exception()


## Slot Conversions Helpers ##

@ask.intent("DayCountIntent", convert={'thedate': 'date'})
def day_count(thedate):
    delta = thedate - date.today()
    days = delta.days
    return statement("It is {} days from now".format(days))

@ask.intent("ReverseDayCountIntent", convert={'delta': 'timedelta'})
def reverse_day(delta):
    futuredate = date.today() + delta
    return statement("is the day {}".format(futuredate))

if __name__ == '__main__':
    app.run(debug=True)
