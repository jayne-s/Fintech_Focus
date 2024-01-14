# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
# from flask import render_template
from flask import request
from flask import render_template

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
  
@app.route('/fitness')
def exercise():
    return render_template('fitness.html')
  
@app.route('/nutrition')
def food():
    return render_template('nutrition.html')

@app.route('/mhealth')
def mental():
    return render_template('mentalhealth.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/FAQ')
def question():
    return render_template('FAQ.html')
  
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/quizAction', methods=['GET', 'POST'])
def quizResults():
  form  = request.form
  print(form)
  scoreLow = 0
  scoreMed = 0
  scoreHigh = 0
  question1 = form.getlist("set1")
  print(question1)
  question2 = form.getlist("set2")
  print(question2)
  question3 = form.getlist("set3")
  print(question3)
  question4 = form.getlist("set4")
  print(question4)
  question5 = form.getlist("set5")
  print(question5)
  if request.method == 'POST':
    
    if question1 == ["30"]:
      scoreLow+=1
    elif question1 == ["60"]:
      scoreMed+=1
    else:
      scoreHigh+=1
      
    if question2 == ["30"]:
      scoreLow+=1
    elif question2 == ["60"]:
      scoreMed+=1
    else:
      scoreHigh+=1
      
    if question3 == ["30"]:
      scoreLow+=1
    elif question3 == ["60"]:
      scoreMed+=1
    else:
      scoreHigh+=1
      
    if question4 == ["30"]:
      scoreLow+=1
    elif question4 == ["60"]:
      scoreMed+=1
    else:
      scoreHigh+=1
      
    if question5 == ["30"]:
      scoreLow+=1
    elif question5 == ["60"]:
      scoreMed+=1
    else:
      scoreHigh+=1
    print(scoreHigh)
    print(scoreLow)
    print(scoreMed)
    if(scoreLow > scoreMed and scoreLow > scoreHigh):
      return render_template('scoreLow.html')
    elif(scoreMed > scoreLow and scoreMed > scoreHigh):
      return render_template('scoreMed.html')
    elif(scoreHigh > scoreMed and scoreHigh > scoreLow):
      return render_template('scoreHigh.html')
  else:
    return "You're getting this page."
    
    
    # return "<h4>Results: </h4>"

# @app.route('/sendWorkout', methods=['GET', 'POST'])
# def workout():
#   form = request.form
#   workoutType = form['exercise']
#   if request.method == 'GET':
#     return "Your getting the workouts"
#   else:
    
#     if workoutType.lower() == "chest and triceps":
#       return render_template('workout1.html')
#     elif workoutType.lower() == "back and biceps":
#       return render_template('workout2.html')
#     elif workoutType.lower() == "legs and shoulders":
#       return render_template('workout3.html')
    
@app.route('/workout1')
def triceps():
  return render_template('workout1.html')
@app.route('/workout2')
def biceps():
  return render_template('workout2.html')
@app.route('/workout3')
def legs():
  return render_template('workout3.html')
app.run(host='0.0.0.0', port=81, debug=True)
