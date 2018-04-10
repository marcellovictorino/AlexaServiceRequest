import logging
from random import randint
import urllib3
from send_email import sendEmail

from flask import Flask, render_template
from flask_ask import Ask, request, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

#################################################################
## Invocation name: report a concern to the city of sugar land ##
#################################################################

@ask.launch
def launch():
    welcome_msg = render_template('welcome')
    reprompt_text = render_template('welcome_long')
    return question(welcome_msg).reprompt(reprompt_text)

@ask.intent("AMAZON.StopIntent")
@ask.intent("AMAZON.CancelIntent")
@ask.intent("AMAZON.NoIntent")
def goodbye():
    msg = render_template('goodbye')
    return statement(msg)

@ask.intent("AMAZON.YesIntent")
def reportIssue():  
    location_question = render_template('location_question')
    return question(location_question)


@ask.intent("LocationIntent") #, convert={'first': int, 'second': int, 'third': int})
#def location(location):
def location(direction, intersection):

    if direction is not None:
        session.attributes['location'] = "heading " + direction + " on " + intersection
    elif intersection is not None:
         session.attributes['location'] = intersection

    SRcategories = ['Traffic Sign', 'Traffic Signal', 'Drainage', 'Water', 'Pothole', 'or Streets']

    problem_type = render_template('problem_type', SRcategories = SRcategories)
    problem_type_examples = render_template('problem_type_examples', SRcategories = SRcategories)

    return question(problem_type).reprompt(problem_type_examples) # prepare to ask the next question. If Utterance match, the respective Intent will be identified

@ask.intent("ProblemTypeIntent")
def problemType(problem_type):
    if problem_type is not None:
        session.attributes['category'] = problem_type
    
    problem_detail = render_template('problem_detail')
    problem_detail_repromt = render_template('problem_detail_reprompt')

    return question(problem_detail).reprompt(problem_detail_repromt)

@ask.intent("ProblemDetailIntent")
def problemDetail(problem_detail):
    if problem_detail is not None:
        session.attributes['description'] = problem_detail
    
    resident_info = render_template('resident_info')
    return question(resident_info)

@ask.intent("ResidentInfoIntent")
def residentInfo(name, phone_number):
    if name is None:
        name = 'Anonymous'
    
    if phone_number is None:
        phone_number = 'Not provided'
    
    session.attributes['residentName'] = name
    session.attributes['residentPhoneNumber'] = phone_number
    
    location = session.attributes['location']
    concernCategory = session.attributes['category']
    description = session.attributes['description']

    try:
        sendEmail(location, concernCategory, description, name, phone_number)
        final_msg = render_template('success_msg')
    
    except:
        final_msg = render_template('failure_msg')
        
    return statement(final_msg)

if __name__ == '__main__':

    app.run(debug=True)