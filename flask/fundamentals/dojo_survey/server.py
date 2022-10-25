from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'Ravioli Ravioli, give me the formuoli'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    session['inlineRadioOptions'] = request.form['inlineRadioOptions']
    session['book'] = request.form['book']
    print(request.form)
    return redirect('/results')

@app.route('/results')         
def show_info():
    return render_template("results.html")

if __name__=="__main__":
    app.run(debug=True)