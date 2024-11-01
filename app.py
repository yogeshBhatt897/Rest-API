from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for students
students = {}

# GET /students: Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values())), 200

# GET /students/<id>: Retrieve a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = students.get(id)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

# POST /students: Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    student_id = data.get("id")
    if student_id in students:
        return jsonify({"error": "Student with this ID already exists"}), 400
    students[student_id] = data
    return jsonify(data), 201

# PUT /students/<id>: Update an existing student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    if id not in students:
        return jsonify({"error": "Student not found"}), 404
    data = request.json
    students[id].update(data)
    return jsonify(students[id]), 200

# DELETE /students/<id>: Delete a student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    if id in students:
        del students[id]
        return jsonify({"message": "Student deleted"}), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
