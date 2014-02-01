from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def beginning():
	return render_template('opening.html')

@app.route("/textbook/seller")
def hello():
    return render_template("seller.html")

archive = []

@app.route("/textbook/new", methods=["POST"])
def addTextbook():
	price = int(request.form['price'])
	cNum = request.form['courseNum']
	email = request.form['email']
	name = request.form['textName']
	new = Book(price, cNum, email, name)
	archive.append(new)
	archive.sort(key = lambda x: x.price)
	return render_template('saleposted.html')
    
@app.route("/textbook/buyer")
def allTextbooks():
	return render_template('buyer.html')

@app.route("/textbook/search", methods=["POST"])
def searchTextbooks():
	return render_template('textbooks.html', textbooks=archive, course=request.form['course'])

class Book:
	def __init__(self, price, course_no,email, name):
		self.price = price
		self.courseNum = course_no
		self.email = email
		self.name = name

if __name__ == "__main__":
	app.run(debug=True)
