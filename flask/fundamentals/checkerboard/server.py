from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/play/')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<int:y>/')
@app.route('/play/<int:x>/<int:y>/<string:color1>/<string:color2>')
# Default Values Set To 8 and 8 With Default Colors
def box_extra_colors(x = 8, y = 8, color1 = "rgb(85,107,47)", color2 = "rgb(255,255,224)"):
    return render_template('index.html', x = x, y = y, color1 = color1, color2 = color2)

# Routed to separate HTML for 4x8 checkerboard
@app.route('/play/4/')
def eight_by_four():
    return render_template('index4.html')
    
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"

if __name__=="__main__":
    app.run(debug=True) 
    # app.run(debug=True, host="0.0.0.0") 


