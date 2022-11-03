# importing Flask and other modules
from flask import Flask, request, render_template
import uuid
 
# Flask constructor
app = Flask(__name__)  
 


students = []
# A decorator used to tell the application
# which URL is associated function
@app.route('/students', methods =["POST"])
def post():
    data = request.get_json()
    data['id']= uuid.uuid1()
    students.append(data)
    return "",201

@app.route("/students",methods = ["GET"])
def get():
    return students , 200

# @app.route("/std",methods= ["PUT"])
# def put():
#     insertData = request.get_json()
#     print(insertData)
#     return students, 201 

@app.route("/std", methods=['PUT'])
def put():
    request.method == 'PUT'
    return "PUT\n"

@app.route('/students', methods = ["DELETE"])
def DEL():
    deleteData = request.get_json()
    print(deleteData)
    return "",200

# @app.route('/students', methods = ["PUT"])
# def put():
if __name__=='__main__':
    app.run()