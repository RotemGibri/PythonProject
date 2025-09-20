def add(first, second):
    print(result)
    return sum([first, second])


def mult(first, second):
    return first * second


def divide(first, second):
    return first / second


def redact(first, second):
    return first - second


def power(first, second):
    print(a)
    print(b)
    return pow(first, second)

b = "Global"
if __name__ == "__main__":
    a = 'Blabla'
    options = {
        'Add': "+",
        'Multiply': "*",
        'Divide': "/",
        'Redact': "-",
        'Power': "^",
    }
    result = int((input('Enter a number: ')))
    while True:
        try:
            action = input(f'What you want to do: \n'
                           f'1) Add ({options["Add"]}) \n'
                           f'2) Multiply ({options["Multiply"]})\n'
                           f'3) Divide ({options["Divide"]})\n'
                           f'4) Redact({options["Redact"]})\n'
                           f'5) Power({options["Power"]})\n')
            user_number_input = float(input('Enter a number: '))
            last_result = result

            match action:
                case "1":
                    action = options["Add"]
                case "2":
                    action = options["Multiply"]
                case "3":
                    action = options["Divide"]
                case "4":
                    action = options["Redact"]
                case "5":
                    action = options["Power"]


            match action:
                case "+":
                    result = add(result, user_number_input)
                case "*":
                    result = mult(result, user_number_input)
                case "/":
                    result = divide(result, user_number_input)
                case "-":
                    result = redact(result, user_number_input)
                case "^":
                    result = power(result, user_number_input)

            print(str(last_result) + " " + str(action) + " " + str(user_number_input) + " = " + str(result))
            print("\n")
        except Exception as e:
            print('Math error!\nPlease try again' + e)

