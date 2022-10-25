from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:times>/')
@app.route('/<int:times>/<string:color>')
@app.route('/play/')
@app.route('/play/<int:times>/')
@app.route('/play/<int:times>/<string:color>')
def box_extra_color(times = 3, color = "lightblue"):
    return render_template('index.html', num = times, color = color)


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"

if __name__=="__main__":
    app.run(debug=True) 