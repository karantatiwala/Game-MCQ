from flask import Flask, render_template
from random import shuffle

app = Flask(__name__)


a = ["python", "c", "c++"]

submit = False
check = False
val = ""

@app.route('/')
def index():
	return render_template("base.html", a=a)

@app.route('/answer')
def answer(a, submit, check):

	if(submit == True & check == True):
		shuffle(a)
		answer = a[0]
	else:
		return render_template("404.html")


	return render_template("answer.html")



if __name__ == "__main__" :
	app.run(debug = True)






