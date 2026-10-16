def classify_grade(score):
    if score is None:
        return "No score provided"
    elif score > 100 or score < 0:
        return "Invalid score"
    elif 90 <= score <= 100:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def classify_grade_match(score):
    match score:
        case None:
            return "No score provided"
        case score if 90 <= score <= 100:
            return "A"
        case score if 80 <= score < 90:
            return "B"
        case score if 70 <= score < 80:
            return "C"
        case score if 60 <= score < 70:
            return "D"
        case score if 0 <= score < 60:
            return "F"
        case _:
            return "Invalid score"

def classify_grade_ternary(score):
# separate guard logic from classification
    if score is None: "No score provided"
    if not (0 <= score <= 100): return "Invalid score"
    return (
        "A" if score >= 90 else
        "B" if score >= 80 else
        "C" if score >= 70 else
        "D" if score >= 60 else
        "F"
    )

print(classify_grade(95))
print(classify_grade(85))
print(classify_grade(75))
print(classify_grade(65))
print(classify_grade(55))
print(classify_grade(105))
print(classify_grade(-10))
print(classify_grade(None))

print(classify_grade_match(95))
print(classify_grade_match(85))
print(classify_grade_match(75))
print(classify_grade_match(65))
print(classify_grade_match(55))
print(classify_grade_match(105))
print(classify_grade_match(-10))
print(classify_grade_match(None))


print(classify_grade_ternary(95))
print(classify_grade_ternary(85))
print(classify_grade_ternary(75))
print(classify_grade_ternary(65))
print(classify_grade_ternary(55))
print(classify_grade_ternary(105))
print(classify_grade_ternary(-10))
print(classify_grade_ternary(None))

