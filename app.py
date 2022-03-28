from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from scholarly import scholarly
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///professors.db'
# Initialize database
db = SQLAlchemy(app)

# Create DB model


class Professors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hindex = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Return a string when adding to DB
    def __repr__(self):
        return f"Professors('{self.name}','{self.hindex}')"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registrants")
def registrants():
    professors = Professors.query.order_by(Professors.date_created)
    return render_template("registered.html", professors=professors)


@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    if not name:
        return render_template("failure.html")

    # Google Scholar API
    search_query = scholarly.search_author(name)
    author = next(search_query)
    indices_list = (scholarly.fill(author, sections=['indices']))
    # Passed variables to DB
    new_professor = Professors(name=name, hindex=indices_list['hindex'])

    db.session.add(new_professor)
    db.session.commit()
    return redirect("/registrants")
