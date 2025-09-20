student= {
    "name": "rotem",
    "surname": "gibri",
    "age": 36,
    "gender": "Female",
    "course": "Python"
}

def print_student(student):
    for [key, value] in student.items():

        student.update({"is_pay_recived":"yes", "payment_meyhod":"visa"})

def display_name(student):
    print(student.get("name"), student.get("surname"))


display_name(student)
