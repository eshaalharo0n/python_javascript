import json

data_file = "students.json"

def read():
    file = open(data_file, "r")
    students = json.load(file)
    file.close()
    
    return students
    
def read_by_id(id):
    students = read()
    student_result = None
    for student in students:
        if student["id"] == id:
            student_result = student
            break
    
    return student_result
    
def add(student):
    students = read()
    students.append(student)

    file = open(data_file,"w")
    json.dump(students, file)
    file.close()
def update(student_id, student):
    students = read()
    
    for st in students:
        if st["id"] == student_id:
            st["name"] = student["name"]
            st["age"] = student["age"]
            st["city"] = student["city"]
            st["address"] = student["address"]
            break
    
    file = open(data_file,"w")
    json.dump(students, file)
    file.close() 

def delete(student_id):
    students = read()
    
    for st in students:
        if st["id"] == student_id:
            students.remove(st)
            break
        
    file = open(data_file,"w")
    json.dump(students, file)
    file.close()