from flask import Flask, render_template, request, redirect, session # added request and redirect
app = Flask(__name__)
app.secret_key = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    print(request.form)
    print(request.form['name'])
    name = request.form['name']
    email = request.form['email']
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])



if __name__ == "__main__":
    app.run(debug=True)

