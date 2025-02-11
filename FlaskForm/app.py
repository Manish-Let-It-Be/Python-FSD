# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/', methods=['POST', 'GET'])
# def home():
#     if request.method == 'POST':
#         # Get form data
#         name = request.form.get('name')
#         email = request.form.get('email')
#         password = request.form.get('password')

#         # Print the received data (you can save it to a database here)
#         print(f"Name: {name}, Email: {email}, Password: {password}")

#         # Redirect to success page with name and email
#         return render_template('success.html', name=name, email=email)

#     # Render the registration form when the page is first visited
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

import json
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash

app1 = Flask(__name__)

@app1.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        hashed_password = generate_password_hash(password)

        # Create an empty data list if the JSON file doesn't exist
        try:
            with open('user.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        # Append the new user data
        data.append({
            "name": name,
            "email": email,
            "password": hashed_password
        })

        # Save the updated data back to the file
        with open('user.json', 'w') as file:
            json.dump(data, file, indent=4)

        return render_template('success.html', name=name, email=email)


    return render_template('index.html')


if __name__ == '__main__':
    app1.run(debug=True)
