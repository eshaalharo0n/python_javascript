from flask import Flask, request
from flasgger import Swagger

from student_manager import read , read_by_id , add , update , delete

app = Flask(__name__)
Swagger(app)
"""
multi
line
comment

"""


# School Portal
# -- Resources
#         Teachers, Students, Course, Campuse, etc
# -- Verb
#         read -> get, add -> post, update -> put, delete-> delete

#resource/verb


# read/get
@app.route("/")
def home():
    """
    Home API
    ---
    responses:
      200:
        description: Ok
      404:
        description: Page not 
        
    """
    return "Welcome to APIs"
#read by id
@app.route("/student/<int:id>", methods=["GET"])
def get_student_by_id(id):
    """
    Returns Student Record Against provided Id
    ---
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: id
    responses:
      200:
        description: Ok
      404:
        description: Student not found
        
    """
    student = read_by_id(id)
    return student
#add/post
@app.route("/student", methods =["POST"])
def add_student():
    """
    Add a student
    ---
    parameters:
      - in: body
        name: student
        required: true
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            age:
              type: integer
            address:
              type: string
            city:
              type: string
    responses:
      200:
        description: Student added successfully
    """
    student = request.get_json()
    add(student)
    return "Student added successfully!"
@app.route('/student/<int:id>',methods =["PUT"])
def update_student(id):
  """
  Update a student
  ---
  parameters:
    - in: path
      name: id
      required: true
      type: integer
      description: id
        
    - in: body
      name: student
      required: true
      schema:
        type: object
        properties:
          id:
            type: integer
          name:
            type: string
          age:
            type: integer
          address:
            type: string
          city:
            type: string
  responses:
    200:
      description: Student added successfully
    404:
        description: Student not found  
  """
  student = request.get_json()
  update(id, student)
  return "Student updated successfully!"

@app.route("/student/<int:id>", methods=["delete"])
def remove_student(id):
  
  """
    Delete a Student Record Against provided Id
    ---
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: id
    responses:
      200:
        description: Ok
      404:
        description: Student not found
  """
  delete(id)
  
  return "student deleted successfully!"

app.run(debug=True)