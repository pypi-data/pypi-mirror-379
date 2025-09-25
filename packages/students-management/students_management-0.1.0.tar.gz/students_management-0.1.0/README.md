# Students Management Package

A simple Python package for managing student records, including different types of students (Undergraduate, Master, PhD).

## Installation

```bash
pip install .
```

## Usage

```python
from student_package import Student, StudentManager
from student_package import Undergraduate, Master, PhD

# Create a student manager
manager = StudentManager()

# Add students
student1 = Student(1, "John", 20, [85, 90])
manager.add_student(student1)

# Add specialized students
phd_student = PhD("AI Lab", 2, "Alice", 25, [95, 92])
manager.add_student(phd_student)

# Get all students
all_students = manager.all_students()

# Get specific student
student = manager.get_student(1)

# Add grades
student.add_grade(88)

# Get average grade
avg = student.average_grade()
```

## Features

- Basic student management (add, remove, get students)
- Support for different student types (Undergraduate, Master, PhD)
- Grade management
- Average grade calculation