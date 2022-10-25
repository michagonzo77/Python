from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key = 'Ravioli Ravioli, give me the formuoli'

@app.route('/')         
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
    if "amount" not in session:
        session["amount"] = 0
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def create_user():
    if "amount" in session:
        session["amount"] += 1
    else:
        session["amount"] = 1
    guessed = int(request.form['guessednumber'])
    if guessed == session["number"]:
        session["answer"] = "correct"
        print("You got it right!")
    elif guessed > session["number"]:
        session["answer"] = "too high"
        print("Too High")
    else:
        session["answer"] = "too low"
        print("Too Low")
    return redirect('/')

@app.route('/play_again')
def play_again():
        session.clear()
        return redirect ('/')

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"

if __name__=="__main__":   
    app.run(debug=True)    