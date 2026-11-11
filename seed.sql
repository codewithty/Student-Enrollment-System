INSERT INTO Students (FirstName, LastName, Email) VALUES
('Ada', 'Lovelace', 'ada.lovelace@live.lagcc.edu'),
('Alan', 'Turing', 'alan.turing@live.lagcc.edu'),
('Grace', 'Hopper', 'grace.hopper@live.lagcc.edu'),
('Maria', 'Gonzalez', 'maria.gonzalez@live.lagcc.edu'),
('Jamal', 'Carter', 'jamal.carter@live.lagcc.edu'),
('Priya', 'Patel', 'priya.patel@live.lagcc.edu');

INSERT INTO Courses (CourseID, CourseCode, Credits) VALUES
(1, 'MAC250', 3),
(2, 'CSC101', 4),
(3, 'ENG101', 3),
(4, 'MAT120', 4),
(5, 'BUS101', 3),
(6, 'HUM110', 3);

INSERT INTO Enrollments (RegistrationDate, StudentID, CourseID) VALUES
('2026-08-25', 1, 1),
('2026-08-25', 1, 2),
('2026-08-26', 1, 4),
('2026-08-26', 2, 1),
('2026-08-27', 2, 3),
('2026-08-27', 3, 2),
('2026-08-28', 3, 3),
('2026-08-28', 3, 6),
('2026-08-29', 4, 1),
('2026-08-29', 4, 5),
('2026-08-30', 4, 6),
('2026-08-30', 5, 4),
('2026-08-31', 5, 5),
('2026-09-01', 6, 2),
('2026-09-01', 6, 4),
('2026-09-02', 6, 6);