from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def render_lists():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template('index.html', people = users)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"


if __name__=="__main__":
    app.run(debug=True) 
    # app.run(debug=True, host="0.0.0.0") 