from flask import Flask, render_template,redirect, url_for, request, session
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import hashlib
import time

import mysql.connector
app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="dz67"
    )
@app.route('/')
@app.route('/index')




@app.route('/index')
def index():

	tv = mydb.cursor()
	tv.execute("SELECT * FROM raspored")
	res = tv.fetchall()

	profesori = mydb.cursor()
	profesori.execute("SELECT DISTINCT nastavnik FROM raspored")
	resProfesori = profesori.fetchall()

	ucionica = mydb.cursor()
	ucionica.execute("SELECT DISTINCT vreme FROM raspored")
	resUcionica = ucionica.fetchall()

	return render_template('index.html', raspored = res,profesori=resProfesori, ucionica=resUcionica)



if __name__ == '__main__':
	app.run(debug=True)