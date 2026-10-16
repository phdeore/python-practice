from typing import Dict
from dataclasses import dataclass, field

records = [
    {"name": "Alice", "age": 30, "scores": {"math": 95, "english": 88}},
    {"name": "Bob",   "age": 25, "scores": {"math": 72, "english": 91}},
]

@dataclass
class Student:
    name: str
    age: int = 0
    scores: Dict[str, int] = field(default_factory=dict)

students_list = []

for record in records:
    student = Student(record["name"], record["age"], record["scores"])
    students_list.append(student)

sorted_students = sorted(students_list, key=lambda s: -s.scores["english"])
print(sorted_students)


'''
TODO:

Issue 1 — manual __init__ in the dataclass defeats the entire purpose. The whole point of @dataclass is that it generates __init__, __repr__, and __eq__ for you from the field annotations. By writing __init__ yourself, you're using @dataclass as a cosmetic decorator and getting none of the benefit. Remove the __init__ entirely — the generated one will work identically:

dataclass advantage: mutable by default (can reassign fields), supports methods naturally, supports field(default_factory=...) for mutable defaults, can be made frozen with frozen=True

'''