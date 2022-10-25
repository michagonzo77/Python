from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'Ravioli Ravioli, give me the formuoli'

@app.route('/')
def index():
    if "visits" in session:
        session["visits"] += 1
    else:
        session["visits"] = 1
        session["fake"] = 0
    return render_template("index.html")

@app.route('/double')
def double():
    session["fake"] += 2
    return redirect('/')

@app.route('/destroy_session')
def destroy_sesh():
    session.clear()
    return redirect('/')

@app.route('/custom', methods=['POST'])
def custom_count():
    customcount = request.form['customcount']
    session["fake"] = session["fake"] + (int(customcount))
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)