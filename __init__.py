from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', template_folder='templates')

# <name>

@app.route('/')
def homepage():
	return "Welcome to the homepage";

@app.route('/<string:name>')
def namepage(name):
	return "Welcome to " + name + "'s website"

@app.route('/<int:number>')
def numberpage(number):
	response = "<h1>" + str(number) + "</h1><p> YES </p>"
	return response


@app.route('/template')
def templatepage():
	return render_template('test.html')

if __name__ == "__main__":
    app.debug = True
    app.run(port=3000)











