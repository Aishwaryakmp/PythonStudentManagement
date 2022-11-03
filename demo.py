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
   data['id']= uuid.uuid4()
   students.append(data)
   return "",201

@app.route("/students",methods = ["GET"])
def get():
   return students , 200
 
@app.route("/students/<studentId>",methods= ["PUT"])
def put(studentId):
   args = studentId
#  queryParams = request.args.get("test")
   data=request.get_json()
   for i in range (0, len(students)):    
      if studentId == str(students[i]["id"]):
             students[i]['name'] = data['name']
   return students, 200
    
    
    
   return "", 200  
if __name__=='__main__':
   app.run()
