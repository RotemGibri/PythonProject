my_shop = {
    "banana": 10,
    "orange": 3,
    "apple": 5,
    "cucamber": 6,
    "tomato": 8
}

def buy_item (item, quantity):
    if item not in my_shop :
        raise Exception (f'there is no {item} in our store ')

    if my_shop[item] < quantity:
        raise Exception (f'there is not enough {item}s')

    new_item_count = my_shop[item] - quantity
    my_shop[item] = new_item_count
    print (f'you have now only {my_shop[item]} {item}s left.')


if __name__ == "__main__":
    print ("welcome to our shop.")
    try:
        buy_item("banana",11)

    except Exception as e:
        print (e)
