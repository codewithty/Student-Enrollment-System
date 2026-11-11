# Student, Course, and Enrollment System

A small Flask web app for managing students, courses, and enrollments, backed by SQLite.

# Requirements
- Python 3
- Flask (`pip3 install flask`)

# How to run
1. Open a terminal in this folder.
2. Run `python3 app.py`
3. Open http://127.0.0.1:5001 in your browser.

The first run builds the database (`school.db`) automatically from `schema.sql` and `seed.sql`, so it starts with 6 students, 6 courses, and 16 enrollments.

Note: the app uses port 5001 because macOS reserves port 5000.

# Features
- Create students, create courses, and enroll students in courses
- Show all students, courses, and enrollments
- Edit and delete students

# Files
- `app.py`: main script (routes and database access)
- `models.py`: the Student, Course, and Enrollment classes
- `schema.sql`: creates the tables
- `seed.sql`: sample data
- `templates/`: HTML pages