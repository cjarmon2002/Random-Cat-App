from flask import Flask
from flask import render_template
from flask import request
from urllib2 import urlopen
import os
import urllib2
import random

app = Flask(__name__)

def get_cat():
	height = random.randint(100, 500)
	width = random.randint(100,700)
	url = ("http://placekitten.com/%d/%d") % (width, height)
	cat = urlopen(url)
	f = open ("static/cat.jpg", "wb")
	f.write(cat.read())
	f.close()

@app.route("/")
def welcome():
	response = render_template("welcome.html")
	return response

@app.route("/cat1", methods=['POST'])
def cat1():
	get_cat()
	response = render_template("cat1.html")
	return response

# @app.route("/cat2", methods=['POST'])
# def cat2():
# 	get_cat()
# 	response = render_template("cat2.html")
# 	return response

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)