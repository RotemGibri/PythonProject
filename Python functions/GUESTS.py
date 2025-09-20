if __name__ == '__main__':
    MAX_TABLES = 5
    SEATS_PER_TABLE = 4

    occupied_tables = []
    opened_tables = [1,2,3]

    def too_many_guests():
        return guests > SEATS_PER_TABLE

    def sit_table():
        next_free_table = len(occupied_tables) + 1
        print("you may sit at table " + str(next_free_table))
        occupied_tables.append(next_free_table)

    def open_table():
        new_table = len(opened_tables) + 1
        opened_tables.append(new_table)
        print("let me just open a table for you.")

    while True:
        guests = int(input("how many guests are you? "))
        if too_many_guests():
            print("Sorry, you are too many guests.")
            continue

        #sit
        if len(opened_tables) >= MAX_TABLES:
           print("sorry we are full.")
           break

        if len(opened_tables) <= len(occupied_tables):
            open_table()

        sit_table()



