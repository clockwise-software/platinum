# CLOCKWISE-BOOTCAMP SimpleServer.py
# Based on Server from Dr. Ian Cooper @ Cardiff
# Updated by Dr. Mike Borowczak @ UWyo March 2021

import secrets
import sqlite3

from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bootcamp.db"

# Generate a safe secret key on the fly
app.secret_key = secrets.token_urlsafe(32)

# Load the database
db = SQLAlchemy(app)


class Employee(db.Model):
    """Database Model"""

    __tablename__ = "EmployeeList"
    __table_args = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column("firstName", db.Text)
    last_name = db.Column("lastName", db.Text)
    hours = db.Column("FT/PT/.75?", db.Text)
    business_unit = db.Column("Business Unit", db.Text)
    city = db.Column("City", db.Text)
    state = db.Column("State/Province", db.Text)
    career_matrix = db.Column("Career Matrix Title", db.Text)
    total_years = db.Column("Total years", db.Text)
    licenses = db.Column("Registered Licenses", db.Text)
    skill = db.Column("Skill", db.Text)
    skill_level = db.Column("Skill Level", db.Text)


@app.route("/")
def root():
    """Dump all the employees to a table."""
    # TODO: Make this dynamically load
    # TODO: Make this prettier
    data = Employee.query.all()
    return render_template("Employee.html", data=data)


@app.route("/Employee/AddEmployee", methods=["GET", "POST"])
def studentAddDetails():
    if request.method == "GET":
        return render_template("EmployeeData.html")

    # If a field is left empty do nothing
    # TODO: Implement a pretty way of telling the user
    if "" in request.form.values():
        return ("", 204)

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")

    # Check if the employee already exists
    employee = Employee.query.filter_by(
        first_name=first_name, last_name=last_name
    ).first()

    # Update if the employee exists
    # TODO: Show some pretty confirmation
    if employee is not None:
        employee.first_name = request.form.get("first_name")
        employee.last_name = request.form.get("last_name")
        employee.business_unit = request.form.get("business_unit")
        employee.state = request.form.get("state")
    else:
        employee = Employee(**request.form)
        print(employee.first_name)
        db.session.add(employee)

    db.session.commit()
    return render_template("EmployeeData.html")


@app.route("/Employee/Search", methods=["GET", "POST"])
def surnameSearch():
    if request.method == "GET":
        return render_template("EmployeeSearch.html")
    try:
        lastName = request.form.get(
            "lastName", default="Error"
        )  # rem: args for get form for post
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM 'EmployeeList' WHERE LastName=?", [lastName])
        data = cur.fetchall()
        print(data)
    except Exception as e:
        print("there was an error", e, data)
        conn.close()
    finally:
        conn.close()
        # return str(data)
        return render_template("Employee.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
