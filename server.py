from flask import Flask, render_template, request
from random import shuffle

app = Flask(__name__)




@app.route('/')
def index():
	a = ["python", "c", "c++"]
	print a
	return render_template("base.html", a=a)



@app.route('/answer', methods=['GET', 'POST'])			# transition frm post->get->post->get->post
def answer():
	a = ["python", "c", "c++"]
	shuffle(a)
	print a
	answer = a[0]

	print answer

	if request.method == "POST":
		val = request.form['ans']
		print val
		return render_template("answer.html", val=val, answer=answer)



if __name__ == "__main__" :
	app.run(debug = True)






