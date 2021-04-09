## CLOCKWISE-BOOTCAMP SimpleServer.py 
## Based on Server from Dr. Ian Cooper @ Cardiff
## Updated by Dr. Mike Borowczak @ UWyo March 2021

import os
from flask import Flask, redirect, request, render_template
import sqlite3

DATABASE = 'bootcamp.db'

app = Flask(__name__)

@app.route("/")
def basic():
    return render_template('Employee.html')

@app.route("/Employee/AddEmployee", methods = ['POST','GET'])
def studentAddDetails():
	if request.method =='GET':
		return render_template('EmployeeData.html')
	if request.method =='POST':
		firstName = request.form.get('firstName', default="Error") 
		lastName = request.form.get('lastName', default="Error")
		businessunit = request.form.get('bu', default="Error")
		state = request.form.get('state', default="Error")
		print("inserting employee"+firstName)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO EmployeeList ('FirstName', 'LastName', 'Business Unit', 'State/Province')\
						VALUES (?,?,?,?)",(firstName, lastName, businessunit, state ) )

			conn.commit()
			msg = "Record successfully added"
		except:
			conn.rollback()
			msg = "error in insert operation"
		finally:
			conn.close()
			return msg

@app.route("/Employee/Search", methods = ['GET','POST'])
def surnameSearch():
	if request.method =='GET':
		return render_template('EmployeeSearch.html')
	if request.method =='POST':
		try:
			lastName = request.form.get('lastName', default="Error") #rem: args for get form for post
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("SELECT * FROM 'EmployeeList' WHERE LastName=?", [lastName])
			data = cur.fetchall()
			print(data)
		except:
			print('there was an error', data)
			conn.close()
		finally:
			conn.close()
			#return str(data)
			return render_template('Employee.html', data = data)



# The name says it...
@app.route("/Employee/VulnerableSearch", methods = ['GET','POST'])
def surnameInjectionSearch():
	if request.method =='GET':
		return render_template('EmployeeSQLInjection.html')
	if request.method =='POST':
		lastName = request.form.get('lastName', default="Error") #rem: args for get form for post
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		
		# VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD
		query = "SELECT * FROM EmployeeList WHERE lastname= '%s' " % (lastName,)
		print (query)
		cur.execute(query)
		# VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD VERY BAD
		
		data = cur.fetchall()
		print (data)
		print (lastName)
		conn.close()
		return render_template('Employee.html', data = data)


if __name__ == "__main__":
	app.run(debug=True)
	app.run(host='0.0.0.0', port=5000)
