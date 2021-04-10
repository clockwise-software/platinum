# CLOCKWISE-BOOTCAMP SimpleServer.py
# Based on Server from Dr. Ian Cooper @ Cardiff
# Updated by Dr. Mike Borowczak @ UWyo March 2021


import csv
import secrets
from datetime import datetime
from io import StringIO

from flask import (
    Flask,
    make_response,
    render_template,
    request,
    session,
    redirect,
    url_for,
)
from sqlalchemy import and_

from flask_sqlalchemy import SQLAlchemy

DATABASE = "bootcamp.db"
SESSION_TYPE = "memcached"

app = Flask(__name__)

# DB connector
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

    column_names = [
        "first_name",
        "last_name",
        "hours",
        "business_unit",
        "city",
        "state",
        "career_matrix",
        "total_years",
        "licenses",
        "skill",
        "skill_level",
    ]

    def as_dict(self):
        return {c: getattr(self, c) for c in self.column_names}


@app.route("/", methods=["GET"])
def basic():
    return render_template("EmployeeSearch.html")


@app.route("/Employee/AddEmployee", methods=["GET", "POST"])
def addEmployee():
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
        db.session.add(employee)

    db.session.commit()
    return render_template("EmployeeData.html")


@app.route("/Employee/Search", methods=["GET", "POST"])
def searchEmployee():
    if request.method == "GET":
        session["last_query_params"] = None
        return render_template("EmployeeSearch.html")

    if session.get("last_query_params") is None:
        # Select and prepare data for query
        payload = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "career_matrix": request.form.get("job_title"),
            "licenses": request.form.get("licenses"),
            "state": request.form.get("state"),
        }
        payload = {k: v for k, v in payload.items() if v != "" and v is not None}
        payload = {k: f"%{v}%" for k, v in payload.items()}

        search_query = Employee.query.filter(
            and_(*[getattr(Employee, k).ilike(v) for k, v in payload.items()])
        ).order_by(Employee.last_name)

    else:
        payload = session["last_query_params"]
        payload["licenses"] = {
            "PE": request.form.get("PE_checkbox"),
            "PG": request.form.get("PG_checkbox"),
            "EI": request.form.get("EI_checkbox"),
        }

        if list(payload["licenses"].values()) == [None, None, None]:
            payload["licenses"] = None

        payload = {k: v for k, v in payload.items() if v != "" and v is not None}

        subquery = Employee.query.filter(
            and_(*[getattr(Employee, k).ilike(v) for k, v in payload.items()])
        ).order_by(Employee.last_name)

        if payload.get("licenses") is not None:
            search_query = []
            checked_keys = [
                k
                for k in payload["licenses"].keys()
                if payload["licenses"][k] is not None
            ]
            for q in subquery:
                if q.licenses in checked_keys:
                    search_query.append(q)
        else:
            search_query = subquery

    # Save the last query per session for easy export
    session["last_query"] = [q.as_dict() for q in search_query]
    session["last_query_params"] = payload

    return render_template("Employee.html", data=search_query)


# This block below downloads the data returned by the database into a CSV file. Nothing is saved to the server.
@app.route("/exportdata")
def createCSV():
    buffer = StringIO()
    writer = csv.DictWriter(
        buffer,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL,
        fieldnames=Employee.column_names,
    )

    if session.get("last_query") is None:
        session["last_query"] = []

    writer.writeheader()
    writer.writerows(session["last_query"])

    # Create response object to download CSV
    download = make_response(buffer.getvalue())

    now = datetime.now().strftime("%d-%m-%y_%H-%M-%S")

    download.headers[
        "Content-Disposition"
    ] = f"attachment; filename=ExportedData_{now}.csv"
    download.headers["Content-type"] = "text/csv"

    return download


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
