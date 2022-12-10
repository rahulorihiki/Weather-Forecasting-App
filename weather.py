# Importing all the required files
from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weathercwh.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Creating our tables in our database
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer, nullable=False)
    pressure = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    city = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str: 
        return f"{self.sno} - {self.temperature} - {self.pressure} - {self.humidity} - {self.city}"

@app.route('/', methods = ['GET','POST'])
def index():
  if request.method == 'POST':
    temperature1 = request.form['tempe']
    pressure1 = request.form['press']
    humidity1 = request.form['humid']
    city1 = request.form['cityl']
    todo = Todo(temperature = temperature1 , pressure = pressure1 , humidity = humidity1 , city = city1 )
    db.session.add(todo)
    db.session.commit()

  allTodo = Todo.query.all()
  return render_template('admin.html', allTodo = allTodo)

# Creating the functionality for the delete part of the CRUD
@app.route('/delete/<int:sno>')
def delete(sno):
  todo = Todo.query.filter_by(sno = sno).first()
  db.session.delete(todo)
  db.session.commit()
  return redirect("/")

@app.route('/update/<int:sno>', methods = ['GET','POST'])
def update(sno):
  if request.method == 'POST':
    temperature1 = request.form['tempe']
    pressure1 = request.form['press']
    humidity1 = request.form['humid']
    city1 = request.form['cityl']
    todo = Todo.query.filter_by(sno = sno).first()
    # db.session.add(todo) No need to add the todo into the database while updating as we are just replacing the existing values
    todo.temperature = temperature1
    todo.pressure = pressure1
    todo.humidity = humidity1
    todo.city = city1
    db.session.add(todo)
    db.session.commit()
    return redirect("/")

  todo = Todo.query.filter_by(sno = sno).first()
  return render_template('update.html', todo = todo)
  

if __name__ == "__main__":
  app.run(debug=True)
