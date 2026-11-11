import sqlite3
import os
from models import Student, Course, Enrollment


DB_PATH = os.path.join(os.path.dirname(__file__), "school.db")

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def courses():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT CourseID, CourseCode, Credits FROM Courses").fetchall()
    conn.close()
    courses = [Course(*row) for row in rows]
    return render_template("courses.html", courses=courses)

@app.route("/students")
def students():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT StudentID, FirstName, LastName, Email FROM Students").fetchall()
    conn.close()
    students = [Student(*row) for row in rows]
    return render_template("students.html", students=students)

@app.route("/students/add", methods=["POST"])
def add_student():
    first = request.form["first_name"]
    last = request.form["last_name"]
    email = request.form["email"]
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "INSERT INTO Students (FirstName, LastName, Email) VALUES (?, ?, ?)",
            (first, last, email),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return "That email is already registered.", 400
    conn.close()
    return redirect("/students")

@app.route("/students/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM Students WHERE StudentID = ?", (student_id,))
    conn.commit()
    conn.close()
    return redirect("/students")

@app.route("/students/edit/<int:student_id>")
def edit_student(student_id):
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT StudentID, FirstName, LastName, Email FROM Students WHERE StudentID = ?",
        (student_id,),
    ).fetchone()
    conn.close()
    student = Student(*row) if row else None
    return render_template("edit_student.html", s=student)

@app.route("/students/edit/<int:student_id>", methods=["POST"])
def update_student(student_id):
    first = request.form["first_name"]
    last = request.form["last_name"]
    email = request.form["email"]
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "UPDATE Students SET FirstName = ?, LastName = ?, Email = ? WHERE StudentID = ?",
            (first, last, email, student_id),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return "That email is already registered.", 400
    conn.close()
    return redirect("/students")

@app.route("/courses/add", methods=["POST"])
def add_course():
    course_id = request.form["course_id"]
    code = request.form["course_code"]
    credits = request.form["credits"]
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "INSERT INTO Courses (CourseID, CourseCode, Credits) VALUES (?, ?, ?)",
            (course_id, code, credits),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return "That course ID or course code already exists.", 400
    conn.close()
    return redirect("/courses")

@app.route("/enrollments")
def enrollments():
    conn = sqlite3.connect(DB_PATH)
    enrollments = [Enrollment(*row) for row in conn.execute(
        "SELECT EnrollmentID, RegistrationDate, StudentID, CourseID FROM Enrollments ORDER BY EnrollmentID"
    ).fetchall()]
    students = [Student(*row) for row in conn.execute("SELECT StudentID, FirstName, LastName, Email FROM Students").fetchall()]
    courses = [Course(*row) for row in conn.execute("SELECT CourseID, CourseCode, Credits FROM Courses").fetchall()]
    conn.close()
    student_names = {s.student_id: s.first_name + " " + s.last_name for s in students}
    course_codes = {c.course_id: c.course_code for c in courses}
    return render_template("enrollments.html", enrollments=enrollments, students=students, courses=courses,
    student_names=student_names, course_codes=course_codes)

@app.route("/enrollments/add", methods=["POST"])
def add_enrollment():
    student_id = request.form["student_id"]
    course_id = request.form["course_id"]
    date = request.form["registration_date"]
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO Enrollments (RegistrationDate, StudentID, CourseID) VALUES (?, ?, ?)",
        (date, student_id, course_id),
    )
    conn.commit()
    conn.close()
    return redirect("/enrollments")

def init_db():
    if os.path.exists(DB_PATH):
        return
    conn = sqlite3.connect(DB_PATH)
    folder = os.path.dirname(__file__)
    for name in ("schema.sql", "seed.sql"):
        with open(os.path.join(folder, name)) as f:
            conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)