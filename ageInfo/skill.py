import logging
import os
import time
from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement, context
from witlingo import analytics

app = Flask(__name__)
ask = Ask(app, "/")

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

wit = {}

@ask.launch
def launch():
    wit["start_time"] = time.time()
    wit["skill_id"] = 2
    wit["skill_user_id"] = str(session.user.userId)
    wit["skill_session_id"] = str(session.sessionId)
    wit["locale"] = str(request.locale)
    wit["requests"] = [
                        {
                            "request_id": str(request.requestId),
                            "request_type": str(request.type) ,
                            "timestamp" : time.time(),
                            "locale" : str(request.locale),
                            "category": "None",
                            "action": "regular"
                            }]

    #['request_id'] = str(request.requestId)

    #wit["request_id"] = str(request.requestId)

    return question('Hi age info, anything else?')

@ask.intent('AgenInfoIntent')
def order():
    # wit = {
    # log.info("start_time: {}".format(request.timestamp))
    # log.info("skill_user_id: {}".format(session.user.userId))
    # log.info("skill_session_id: {}".format(session.sessionId))
    # log.info("Locale: {}".format(request.locale))
    # log.info("request_id: {}".format(request.requestId))
    # log.info("request_type: {}".format(request.type))
    # log.info("timestamp: {}".format(request.timestamp))
    # }
    # wit["start_time"] = format(request.timestamp)
    # wit["skill_user_id"] = str(session.user.userId)
    # wit["skill_session_id"] = str(session.sessionId)
    # wit["locale"] = str(request.locale)
    # wit["request_id"] = str(request.requestId)

    return question('You are 100 years old, anything else?')


@ask.intent('NameInfoIntent')
def name():
    return question('Your name is Libert, anything else?')


@ask.intent('YesIntent')
def yes_respond():
    return question('ok, what else?')


@ask.intent('NoIntent')
def no_respond():

    wit["end_time"] = time.time()
    wit["duration"] = wit["end_time"] - wit["start_time"]
    print (wit)
    analytics(wit)

    return statement('ok Bye')

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement('')


if __name__ == '__main__':
    app.run(debug=True)
