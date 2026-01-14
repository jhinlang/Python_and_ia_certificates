🧙 Character Creation Validator (Python)
---
📌 Description

This project is part of the Python Certification path on FreeCodeCamp.
It focuses on building a function that validates character creation rules and returns a formatted character profile.

The goal is to practice:

input validation

conditional logic

string manipulation

clean and readable Python code
---

⚙️ Features

The function create_character performs the following validations:

🔹 Character name validation

Must be a string

Must not be empty

Must not exceed 10 characters

Must not contain spaces

🔹 Statistics validation

All stats must be integers

Each stat must be between 1 and 4

The total number of stat points must be exactly 7

If any validation fails, the function returns a clear error message.
---

📤 Output Format

When all validations pass, the function returns a four-line string:

Name
STR ●●●○
INT ●●○○
CHA ●○○○


● represents a stat point

○ represents a missing stat point
---

🧪 Example Usage
print(create_character("Ren", 4, 2, 1))


Output:

Ren
STR ●●●●
INT ●●○○
CHA ●○○○
---

🧠 Concepts Practiced

isinstance() for type checking

Conditional validation with early returns

String formatting with f-strings

Building multi-line strings

Defensive programming
---

👤 Author

Julien Hinlang
Project completed during the FreeCodeCamp Python Certification learning path.

---
🚀 Notes

This project is intentionally strict and validation-focused, following the requirements of automated graders and real-world input handling practices.
