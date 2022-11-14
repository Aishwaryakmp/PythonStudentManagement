# importing Flask and other modules
from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import uuid
import json
import collections

from sqlalchemy import table

# Flask constructor
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'demo'
mysql = MySQL(app)


students = []
# jsonStr = json.dumps(students)
# print(jsonStr)
# A decorator used to tell the application
# which URL is associated function


@app.route('/students', methods=["POST"])
def post():
	data = request.get_json()  # getting the json data from the postman
	data['id'] = uuid.uuid4()  # used to auto generate id
	students.append(data)  # storing the datas received from json in students
	return "", 201


@app.route("/students", methods=["GET"]) # list all std names connected to db
def list():
		cur = mysql.connection.cursor()
		cur.execute("SELECT * from student")
		rv = cur.fetchall()
		result = []
		for student in rv:
			d = collections.OrderedDict()
			d['id'] = student[0]
			d['f_name'] = student[1]
			d['l_name'] = student[2]
			d['dept_id']= student[3]
			result.append(d)
		jsonStr = json.dumps(result)
		return str(jsonStr), 200

@app.route("/students/<studentId>", methods=["GET"]) #getting only selected id connected to db
def get(studentId):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM student WHERE id = %s" % (studentId))
	rv = cur.fetchone()
	if rv:
		d = {};
		d["name"] = rv[1]
		jsonStr = json.dumps(d)
		cur.close()
		return str(jsonStr), 200
	else:
		return "", 404


@app.route("/students/<studentId>", methods=["PUT"])
def put(studentId):
	args = studentId
#  queryParams = request.args.get("test")
	data = request.get_json()  # getting json data from postman
	# for loop for checking if the id given and comparing ids are same
	for i in range(0, len(students)):
		if studentId == str(students[i]["id"]):
			students[i]['name'] = data['name']
	return "", 200


# @app.route("/students/<studentId>", methods=["DELETE"]) # normal way to delete a data when not connected to db
# def delete(studentId):
# 	args = studentId
# 	for i in range(0, len(students)):
# 		if studentId == str(students[i]["id"]):
# 			students.pop(i)
# 	return "", 202

@app.route('/students/<studentId>', methods = ["DELETE"] )
def delete(studentId):
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM student WHERE id = %s" % (studentId))
	mysql.connection.commit()
	cur.close()
	return "", 202
   
if __name__ == '__main__':
	app.run()


