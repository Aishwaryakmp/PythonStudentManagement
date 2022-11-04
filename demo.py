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
   data = request.get_json() # getting the json data from the postman 
   data['id']= uuid.uuid4() #used to auto generate id 
   students.append(data) #storing the datas received from json in students
   return "",201

@app.route("/students",methods = ["GET"])
def get():
   return students , 200
 
@app.route("/students/<studentId>",methods= ["PUT"])
def put(studentId):
   args = studentId
#  queryParams = request.args.get("test")
   data=request.get_json() # getting json data from postman 
   for i in range (0, len(students)):    # for loop for checking if the id given and comparing ids are same 
      if studentId == str(students[i]["id"]):
             students[i]['name'] = data['name']
   return "", 200

@app.route("/students/<studentId>",methods=["DELETE"])
def delete(studentId):
       args=studentId
       for i in range (0, len(students)):
              if studentId == str(students[i]["id"]):
                  students.pop(i)
       return "",202  
if __name__=='__main__':
   app.run()
