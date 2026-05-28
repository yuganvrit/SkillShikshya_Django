def calc_avg(*scores):
    return sum(scores) / len(scores)


def get_grades(avg):
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade


def get_status(avg):
    if avg >= 50:
        status = "Pass"
    else:
        status = "Fail"
    return status


def create_student(name, *scores, **extras):
    avg = calc_avg(*scores)
    grade = get_grades(avg)
    status = get_status(avg)

    return {
        "name": name,
        "scores": scores,
        "average": avg,
        "grade": grade,
        "status": status,
        **extras,
    }


def print_report_card(student):
    return {
        "Name": student["name"],
        "Scores": student["scores"],
        "Average": student["average"],
        "Grade": student["grade"],
        "Status": student["status"],
    }


student1 = create_student(
    "Santosh Bohara", 12, 24, 53, 21, 54, Sports="basketball", standard=12
)

print(student1)
print(type(student1))

report = print_report_card(student1)
print(report)
print(type(report))