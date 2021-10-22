from flask import Flask, render_template, redirect, request
from surveys import satisfaction_survey as survey


app = Flask(__name__)

# initialize respinses as an empty list
responses = []

@app.route('/home')
def home_page():
    responses = []
    return render_template('home_page.html')

@app.route('/')
def survey_page():
    
    return render_template('survey_page.html', survey=survey)

@app.route('/start', methods=["POST"])
def start_survey():
    return redirect('/questions/0')


@app.route('/questions/<int:number>')
def question_page(number):
    # responses = []
    if (len(responses) == len(survey.questions)):
        return redirect('/complete')
    if (len(responses) is None):
        return redirect('/')
    if (len(responses) != number):
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[number]
    return render_template("question.html", question_num=number, question=question)

@app.route('/answer', methods=["POST"])
def answer_page():
    # responses = []
    # get the choice from customer
    choice = request.form['answer']
    responses.append(choice)

    if (len(responses) == len(survey.questions)):
        return redirect('/complete')
    if (len(responses) != len(survey.questions)):
        return redirect(f"/questions/{len(responses)}")


@app.route('/complete')
def complete():
    return render_template('complete.html')
