from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import json
import uuid
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = 'manish'  

DATA_FILE = 'data/user_data.json'

os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'divisions': {}}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def generate_student_id():
    return f"stu{uuid.uuid4().hex[:5]}"

@app.route('/')
def home():
    data = load_data()
    divisions = data['divisions']
    return render_template('add_division.html', divisions=divisions)

@app.route('/add_division', methods=['POST'])
def add_division():
    division_name = request.form['division_name']
    data = load_data()
    
    if division_name not in data['divisions']:
        data['divisions'][division_name] = []
        save_data(data)
        flash(f'Division "{division_name}" added successfully!', 'success')
    else:
        flash(f'Division "{division_name}" already exists!', 'error')

    return redirect(url_for('home'))

@app.route('/delete_division/<division_name>', methods=['POST'])
def delete_division(division_name):
    data = load_data()
    if division_name in data['divisions']:
        del data['divisions'][division_name]
        save_data(data)
        flash(f'Division "{division_name}" deleted successfully!', 'success')
    else:
        flash(f'Division "{division_name}" does not exist!', 'error')

    return redirect(url_for('home'))

@app.route('/choose_division/<division_name>')
def choose_division(division_name):
    data = load_data()
    students = data['divisions'].get(division_name, [])
    return render_template('display_students.html', students=students, division_name=division_name)

@app.route('/add_student/<division_name>', methods=['GET', 'POST'])
def add_student(division_name):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        student_id = generate_student_id()

        new_student = {
            'id': student_id,
            'name': name,
            'email': email,
            'phone': phone
        }

        data = load_data()
        data['divisions'][division_name].append(new_student)
        save_data(data)

        flash('Student added successfully!', 'success')
        return redirect(url_for('choose_division', division_name=division_name))

    return render_template('add_student.html', division_name=division_name)

@app.route('/update_student/<division_name>/<student_id>', methods=['GET', 'POST'])
def update_student(division_name, student_id):
    data = load_data()
    student = next((s for s in data['divisions'][division_name] if s['id'] == student_id), None)

    if request.method == 'POST':
        student['name'] = request.form['name']
        student['email'] = request.form['email']
        student['phone'] = request.form['phone']

        save_data(data)
        flash('Student updated successfully!', 'success')
        return redirect(url_for('choose_division', division_name=division_name))

    return render_template('update_student.html', student=student)

@app.route('/delete_student/<division_name>/<student_id>', methods=['POST'])
def delete_student(division_name, student_id):
    data = load_data()
    data['divisions'][division_name] = [s for s in data['divisions'][division_name] if s['id'] != student_id]
    save_data(data)
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('choose_division', division_name=division_name))

@app.route('/export/<division_name>')
def export_to_excel(division_name):
    data = load_data()
    students = data['divisions'].get(division_name, [])
    
    for student in students:
        student['division'] = division_name
    
    df = pd.DataFrame(students)
    excel_file = f'{division_name}_students.xlsx'
    df.to_excel(excel_file, index=False)

    return send_file(excel_file, as_attachment=True)


@app.route('/export/all_students')
def export_all_students():
    data = load_data()
    all_students = []
    
    for division_name, students in data['divisions'].items():
        for student in students:
            student['division'] = division_name  
            all_students.append(student)

    df = pd.DataFrame(all_students)
    excel_file = 'All_Students.xlsx'
    df.to_excel(excel_file, index=False)

    return send_file(excel_file, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
