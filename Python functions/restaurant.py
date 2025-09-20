




if __name__ == '__main__':
    MAX_TABLES = 5
    SEATS_PER_TABLE = 4

    tables = [1,2,3]
    free_tables = [1,2,3]
    next_table = 4

    def find_table():
        global next_table  # נשתמש במשתנה שמחוץ לפונקציה
        if len(free_tables) == 0:
            if len(tables) < MAX_TABLES:
                tables.append(next_table)
                table_number = next_table
                next_table += 1
                return "You may sit at table " + str(table_number)
            else:
                return "Restaurant is full"
        else:
            return "You may sit at table " + str(free_tables.pop())


    # -----------------------------
    # כאן קלט מהמשתמש
    guests = int(input("How many guests? "))

    if guests <= SEATS_PER_TABLE:
        print(find_table())  # קריאה לפונקציה
    else:
        print("Sorry, we are full")
