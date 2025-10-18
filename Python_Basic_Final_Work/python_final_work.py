

def ex1():
    for x in range (12,25):
        print ("print number " + str(x))

def ex2():
    for x in range (7,32):
        if x%2 == 1:
            print ("odd number " + str(x))

def ex3():
    for x in range(-20,10):
        if x % 2 == 0:
            print("even number " + str(x))

def ex4():
    for x in range (1,46):
        if (x % 3 == 0) and (x % 5 == 0):
            print(f" {str(x)} is FizzBuzz")
        else:
            if x%3==0:
                print (f" {str(x)} is Fizz")
            if x % 5 == 0:
                print(f" {str(x)} is Buzz")

def ex5():
    numbers= [1,13,22,123,49,34,5,24,57,45]
    summery= 0
    for i in numbers:
        summery += i
    print (summery)


def ex6():
    student_list = [
        {"id": 1,
         "first name": "nahum",
         "last name": "barnea",
         "age": 34,
         "country": "israel",
         "city": "netanya"
         },
        {"id": 2,
         "first name": "yoav",
         "last name": "barnea",
         "age": 56,
         "country": "israel",
         "city": "netanya"
         },
        {"id": 3,
         "first name": "noam",
         #"last name": "gibri",
         "age": 33,
         "country": "israel",
         "city": "netanya"
         }]
    #1
    def ex6_1(p:str, students):
        for student in students:
            keys = student.keys()
            if p in keys:
                del student[p]
                print(f'{p} was deleted from {student["first name"]}')
    #2
    def ex6_2(students):
        for student in students:
            keys = student.keys()
            for key in keys:
                print(key)

    #3
    def ex6_3(students):
        sorted_students= sorted(students, key=lambda s:s["age"], reverse=True)
        print(sorted_students)

    ex6_1("last name", student_list)
    ex6_2(student_list)
    ex6_3(student_list)

def ex7():

    our_pets = [
        {
            "animal_type": "cat",
            "names": [
                "Meowzer",
                "Fluffy",
                "Kit-Cat"
            ]
        },
        {
            "animal_type": "dog",
            "names": [
                "Spot",
                "Bowser",
                "Frankie"
            ]
        }
    ]

    #1
    def ex7_1(pets):
        for pet in pets:
            if pet["animal_type"] == "cat":
                print("animal type:",pet["animal_type"])

    ex7_1(our_pets)

    def ex7_2(animal_type , pets):
        for pet in pets:
            if pet["animal_type"]== animal_type:
                print(f'{animal_type} names are: {pet["names"]}')

    ex7_2("cat", our_pets)

    def ex7_3(pets, animal_name):
        for pet in pets:
            if animal_name not in pet["names"]:
                pet["names"].append(animal_name)
                print (f'the name {animal_name} was added to the {pet["animal_type"]} names list.')

    ex7_3(our_pets, "rocky")

def ex8():

    student = {
        'name': 'John',
        'age': 20,
        'hobbies': ['reading', 'games', 'coding'],
    }

    #1
    def ex8_1():
        for item in student.items():
            print(item)

    ex8_1()

    #2
    def ex8_2(student_object, hobby):
        if hobby not in student_object["hobbies"] :
            student_object["hobbies"].append(hobby)
            print(f"hobby {hobby} was added to the student's hobbies list")

    ex8_2(student, "music")
    #3
    ex8_1()

    #4
    def ex8_4(student_object, hobby):
        hobbies= student_object["hobbies"]
        if hobby in hobbies:
            hobby_index= hobbies.index(hobby)
            hobbies.pop(hobby_index)
            print(f"hobby {hobby} was deleted from the student's hobbies list")

    ex8_4(student, "music")
    #5
    ex8_1()

    #6
    def ex8_6():
        student["family name"] = "gibri"
        # student.update({"family name": "gibri"})
        print (student)
    ex8_6()

def ex9():
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    def print_matrix(mat):
        jz = ""
        for i in mat:
            for j in i :
                jz+= f'{j} '
        print (jz)

    print_matrix(matrix)

def ex10():
    matrix = [
        [0, 1, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]

    def count_zeros(mat):
        zero_count = 0
        for i in mat:
            for j in i :
                if j == 0:
                    zero_count += 1
        print (zero_count)
    count_zeros(matrix)

def ex11():
    arr = [4, 2, 34, 4, 1, 12, 1, 4]
    dup_set = set()
    for i in arr :
        find_dup= arr.count(i)
        if find_dup >1:
            dup_set.add(str(i))
    print(dup_set)

def ex12():
    arr = [43, "what", 9, True, "cannot", False, "be", 3, True]
    reverse_arr = []
    for i in arr :
        reverse_arr.insert(0, i)
    print(reverse_arr)

def ex13():
    first_array = [4, 6, 7]
    second_array = [8, 1, 9]
    arr_sum = []
    for i in range(len(first_array)):
        summery = first_array[i]+ second_array[i]
        arr_sum.append(summery)
    print(arr_sum)

def ex14():
    first_str = "racecar"
    second_str = "Java"
    def is_palindrome(x):
        x:str
        rev_str = "".join(reversed(x))
        if x == rev_str:
            print (True)
        else:
            print(False)

    is_palindrome(first_str)
    is_palindrome(second_str)


def ex15():
    counter= 1
    while counter <= 100:
        counter *= 2
        print (counter)

def ex16():
    counter = 900000
    while counter >= 50:
        counter /= 2
        print (counter)

def ex17():
    names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
    duplicated = []
    def duplications(x):
        i=0
        while i< len(x):
            names_count = x.count(x[i])
            if names_count >1 :
                duplicated.append(x[i])
            i += 1
        print (duplicated)

    duplications(names)


def ex18():
    names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
    unique = []
    i = 0
    while i < len(names):
        if names[i] not in unique:
            unique.append(names[i])
        i += 1
    print(unique)

def ex19():
    names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
    unique = []
    i = 0
    while i < len(names):
        if (names[i] not in unique) & (names[i] != "Pete"):
            unique.append(names[i])
        i += 1
    print(unique)

def ex20():
    array_1 = [True, False, False, True, True, False]
    array_2 = [True, False, True, False, True, True]
    array_3 = [True, False, True, False, True, False]

    def loop(arr):
        i = 0
        while i < (len(arr) -1):
            next_idx = i + 1
            if arr[i]== arr[next_idx]:
                print (next_idx)
                return
            i+=1
        print (-1)

    loop(array_1)
    loop(array_2)
    loop(array_3)


def ex21():

    while True:
        user_full_name = input("please enter your full name: ").strip()
        if not user_full_name.__contains__(" "):
            print("full name should be two separate words.")
            continue
        print(f"user name is: {user_full_name}")
        break

    while True:
        try :
            user_age = int(input("enter your age (number between 1-130): "))
        except ValueError:
            print ("invalid input. please enter a number.")
            continue
        if 1> user_age or user_age >130 :
            print ("age should be a number between 1-130.")
            continue
        print (f"user age is: {user_age}")
        break

    while True:
        user_email = input("enter your email: ")
        if not user_email.__contains__("@"):
            print("invalid input. please enter valid email.")
            continue
        print(f"user email is: {user_email}")
        break


if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    ex6()
    ex7()
    ex8()
    ex9()
    ex10()
    ex11()
    ex12()
    ex13()
    ex14()
    ex15()
    ex16()
    ex17()
    ex18()
    ex19()
    ex20()
    ex21()