# creating the the server

from flask import Flask, jsonify, request, render_template

from urllib.parse import quote_plus

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# password = quote_plus("manish")
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost/world'

# adding config for database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# create models

# create table user(id int primary key,name varchar(100),email varchar)
# USER MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


@app.route('/get_data')
def get_data():
    users=User.query.all()
    results=[]
    for user in users:
        results.append({
            "id":user.id,
            "name":user.name,
            "email":user.email
        })
    return jsonify(results)



@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # adding the data in database
        # creating the instance of user model
        user = User(name=name, email=email)
        db.session.add(user)  # adding the new object in orm session
        db.session.commit()  # it will reflect the changes in the table
        return jsonify({"message": "data added"})
    return render_template('user_form.html')

@app.route('/view_data')
def view_data():
    users = User.query.all()
    return render_template('view_data.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(
        debug=True
    )