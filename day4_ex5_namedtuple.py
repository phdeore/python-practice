from typing import Dict
from collections import namedtuple

records = [
    {"name": "Alice", "age": 30, "scores": {"math": 95, "english": 88}},
    {"name": "Bob",   "age": 25, "scores": {"math": 72, "english": 91}},
]

students_list = []

Scores = namedtuple("Scores", ["math", "english"])
Student = namedtuple("Student", ["name", "age", "scores"])

students = [Student(r["name"], r["age"], Scores(**r["scores"])) for r in records]

'''
for record in records:
    Student = namedtuple('Student', record.keys())
    student = Student(**record)
    students_list.append(student)


sorted_students = sorted(students_list, key=lambda s: -s.scores["math"])
'''
print(students)


'''
TODO:
Issue 2 — namedtuple defined inside the loop. Student = namedtuple('Student', record.keys()) runs on every iteration, creating a new class each time. Define it once outside the loop. Also — the scores field stores a raw dict, which means the namedtuple isn't fully hashable (dict isn't hashable). The idiomatic version nests a Scores namedtuple for the scores:

namedtuple advantage: hashable (when contents are hashable), so it can be used as a dict key or set element; also iterable/unpackable like a tuple; slightly lower memory footprint

'''