from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:num>/<string:message>')
def repeat(num, message):
    output = ""

    for i in range (0,num):
        output += f"<p>{message}</p>"
    return output

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"

if __name__=="__main__":
    app.run(debug=True) 