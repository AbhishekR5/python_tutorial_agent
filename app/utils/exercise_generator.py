from pathlib import Path
import json
import random

# Load syllabus
syllabus_dir = Path("app/data")
syllabus_dir.mkdir(parents=True, exist_ok=True)

# Then use the file path
syllabus_path = syllabus_dir / "syllabus.json"

# Load file if it exists
if syllabus_path.exists():
    with open(syllabus_path, "r") as f:
        syllabus = json.load(f)
else:
    syllabus = {}  

# Concept alias mapping
alias_map = {
    # Day 1
    "Syntax basics": "Basics",
    "Comments": "Basics",
    "Print function": "Basics",

    # Day 2
    "int, float, str, bool": "Data Types",
    "type() and isinstance()": "Data Types",

    # Day 3
    "Arithmetic operators": "Operators",
    "Comparison operators": "Operators",
    "Logical operators": "Operators",

    # Day 4
    "if-else statements": "Conditionals",
    "nested conditions": "Conditionals",
    "boolean expressions": "Conditionals",

    # Day 5
    "for loops": "Loops",
    "while loops": "Loops",
    "break and continue": "Loops",

    # Day 6
    "string indexing": "Strings",
    "string slicing": "Strings",
    "format() and f-strings": "Strings",

    # Day 7
    "list operations": "Lists",
    "tuple immutability": "Lists",
    "list methods": "Lists",

    # Day 8
    "dictionary keys and values": "Dictionaries",
    "set operations": "Dictionaries",
    "dictionary methods": "Dictionaries",

    # Day 9
    "def and return": "Functions",
    "parameters and arguments": "Functions",
    "local vs global scope": "Functions",

    # Day 10
    "lambda": "Functional",
    "map, filter, reduce": "Functional",
    "any, all, zip": "Functional",

    # Day 11
    "import, from-import": "Modules",
    "dir() and help()": "Modules",
    "pip basics": "Modules",

    # Day 12
    "open(), read(), write()": "File Handling",
    "with statement": "File Handling",
    "file modes": "File Handling",

    # Day 13
    "try-except": "Exceptions",
    "finally": "Exceptions",
    "custom exceptions": "Exceptions",

    # Day 14
    "list comprehension": "Comprehensions",
    "dict and set comprehensions": "Comprehensions",
    "nested comprehensions": "Comprehensions",

    # Day 15
    "datetime module": "DateTime",
    "strftime and strptime": "DateTime",
    "timedelta": "DateTime",

    # Day 16
    "math functions": "Math",
    "random module": "Math",
    "statistics module": "Math",

    # Day 17
    "*args, **kwargs": "Advanced Functions",
    "closures": "Advanced Functions",
    "decorators": "Advanced Functions",

    # Day 18
    "class and object": "OOP",
    "attributes and methods": "OOP",

    # Day 19
    "__init__ method": "OOP",
    "self keyword": "OOP",
    "instance attributes": "OOP",

    # Day 20
    "instance methods": "OOP",
    "classmethod and staticmethod": "OOP",

    # Day 21
    "access modifiers": "Encapsulation",
    "property() function": "Encapsulation",
    "getter/setter methods": "Encapsulation",

    # Day 22
    "single and multilevel inheritance": "Inheritance",
    "super()": "Inheritance",
    "method overriding": "Inheritance",

    # Day 23
    "method overloading": "Polymorphism",
    "duck typing": "Polymorphism",

    # Day 24
    "__str__ and __repr__": "Magic Methods",
    "__len__, __eq__, __lt__": "Magic Methods",

    # Day 25
    "composition": "Advanced OOP",
    "aggregation": "Advanced OOP",
    "MRO": "Advanced OOP",

    # Day 26
    "json.load() and json.dump()": "JSON",
    "json.loads() and json.dumps()": "JSON",

    # Day 27
    "unittest basics": "Testing",
    "assertEqual, assertTrue, assertRaises": "Testing",

    # Day 28
    "venv": "Environment",
    "pip install and freeze": "Environment",
    "requirements.txt": "Environment",

    # Day 29
    "project structure": "Projects",
    "planning logic": "Projects",
    "modular coding": "Projects",

    # Day 30
    "refactoring": "Projects",
    "testing": "Projects",
    "presentation": "Projects"
}


# Templates for each normalized concept
#all_templates = {
#    "Syntax basics": [
#        ("Write a Python program that prints your name, age, and favorite language.", "print('Name: John')\nprint('Age: 25')\nprint('Language: Python')"),
#        ("Write a program that prints 'Hello, Python!' three times.", "for _ in range(3): print('Hello, Python!')"),
#        ("Write a script that prints the result of 3 + 5.", "print(3 + 5)"),
#        ("Create a program that prints a line with both single and double quotes.", "print(\"He said, 'Python is fun!'\")"),
#        ("Write a Python script to swap two variables.", "a, b = 5, 10\na, b = b, a\nprint(a, b)")
#    ],
#    "Comments": [
#        ("Write a program with inline comments explaining each step.", "# This program adds two numbers\na = 5\nb = 10\nprint(a + b)"),
#        ("Write a script that includes a multiline comment describing the script.", '"""\nThis script calculates the square of a number\n"""\nx = 4\nprint(x**2)'),
#        ("Add comments to explain what a variable does in your program.", "x = 10  # This variable stores the user age\nprint(x)"),
#        ("Add a comment at the top of your code with your name and date.", "# Author: You | Date: Today\nprint('Starting program')"),
#        ("Create a Python script with useless code and comment it out.", "# print('This line is commented out')\nprint('This line runs')")
#    ],
#    "Print function": [
#        ("Print a triangle pattern using the `print()` function.", "for i in range(1, 6): print('*' * i)"),
#        ("Use `print()` to display your name in a box of asterisks.", "print('************')\nprint('* John Doe *')\nprint('************')"),
#        ("Print the output of multiple lines using newline characters.", "print('Line 1\\nLine 2\\nLine 3')"),
#        ("Print a multiplication table of 5.", "for i in range(1, 11): print(f'5 x {i} = {5*i}')"),
#        ("Print a formatted receipt using tabs and newlines.", "print('Item\\tQty\\tPrice')\nprint('Apple\\t2\\t$3')\nprint('Total:\\t\\t$6')")
#    ],
#    "Primitive Data Types": [
#        ("Create variables of int, float, string, and boolean types, then print them.", "a = 10\nb = 3.14\nc = 'Python'\nd = True\nprint(a, b, c, d)"),
#        ("Print the type of each of the following: 42, 3.14, 'hello', False.", "print(type(42))\nprint(type(3.14))\nprint(type('hello'))\nprint(type(False))"),
#        ("Demonstrate type conversion between int and float.", "a = 5\nb = float(a)\nprint(b)"),
#        ("Concatenate string and integer after type casting.", "age = 25\nprint('Age: ' + str(age))"),
#        ("Check if a variable is of a specific type using isinstance().", "x = 'hello'\nprint(isinstance(x, str))")
#    ],
#    "Type Checking": [
#        ("Use type() to print the data type of a variable.", "x = 10\nprint(type(x))"),
#        ("Check whether a value is a float using isinstance().", "y = 3.14\nprint(isinstance(y, float))"),
#        ("Write a function that prints the type of input argument.", "def check_type(val):\n    print(type(val))\ncheck_type(100)"),
#        ("Determine if a list contains only integers using isinstance().", "lst = [1, 2, 3]\nprint(all(isinstance(i, int) for i in lst))"),
#        ("Use type() and isinstance() together to compare behaviors.", "val = 10.5\nprint(type(val), isinstance(val, float))")
#    ]
#}

# Template generator for a concept
TEMPLATE_PATH = Path("app/data/all_templates.json")

def generate_template(concept, day):
    return {
        "title": f"Practice: {concept}",
        "description": f"Write a Python program that demonstrates your understanding of **{concept}**. "
                       f"Be sure to explain the concept in comments and try different examples.",
        "sample_solution": f"# Sample code for {concept}\n# TODO: Add your logic here for {concept.lower()}",
        "difficulty": "Beginner",
        "day": day
    }

# Generate all_templates
all_templates = {}

for day, details in syllabus.items():
    all_templates[day] = []
    for concept in details.get("concepts", []):
        all_templates[day].append(generate_template(concept, day))

# Output file
output_path = Path("app/data/all_templates.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w") as f:
    json.dump(all_templates, f, indent=2)

print(f"✅ Generated all_templates.json with {len(all_templates)} days of exercises.")

# 🔁 Generates exercises based on a list of concepts
def generate_exercises(concepts):
    selected = []

    for day, exercises in all_templates.items():
        for ex in exercises:
            for concept in concepts:
                if concept.lower() in ex["title"].lower():
                    selected.append({
                        "title": ex["title"],
                        "description": ex["description"],
                        "sample_solution": ex["sample_solution"],
                        "difficulty": ex.get("difficulty", "Beginner"),
                        "day": ex["day"]
                    })

    random.shuffle(selected)
    for i, ex in enumerate(selected[:20]):
        ex["title"] = f"{ex['title']} #{i+1}"
    return selected[:20]

# 📝 Generates full JSON file mapping day -> 20 exercises
def generate_daywise_exercise_file():
    all_day_exercises = {}
    for day, content in syllabus.items():
        concepts = content.get("concepts", [])
        print(f"📘 {day} -> {concepts}")
        all_day_exercises[day] = generate_exercises(concepts)

    output_path = Path("app/data/day_wise_exercises.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(all_day_exercises, f, indent=2)
    return output_path
