# Student CRUD API

A simple RESTful API built with Flask for managing student data, including basic Create, Read, Update, and Delete (CRUD) operations.

## Table of Contents
- [Features](#features)
- [Endpoints](#endpoints)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [License](#license)

---

## Features
- Add new student records
- Retrieve a list of all students or specific student details by ID
- Update student information
- Delete student records

## Endpoints

| Method | Endpoint            | Description                       |
|--------|----------------------|-----------------------------------|
| GET    | `/students`         | Retrieve all students             |
| GET    | `/students/:id`     | Retrieve a student by ID          |
| POST   | `/students`         | Add a new student                 |
| PUT    | `/students/:id`     | Update an existing student by ID  |
| DELETE | `/students/:id`     | Delete a student by ID            |

