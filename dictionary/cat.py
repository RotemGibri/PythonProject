my_cat_status = {
    "tiredness": 10,
    "hunger": 8,
    "loneliness": 7,
    "happiness": 5,
}

MAX = 10
MIN = 0

def increase(my_cat_status, prop , to_inc=1):
    if my_cat_status[prop] < MAX:
        my_cat_status[prop] += to_inc

def decrease(my_cat_status, prop , to_inc=1):
    if my_cat_status[prop] < MIN:
        my_cat_status[prop] -= to_inc


def feed(my_cat_status):
    decrease(my_cat_status, "hunger", 4)
    decrease(my_cat_status, "tiredness", 2)

def pet(my_cat_status):
    decrease(my_cat_status, "loneliness", 3)
    increase(my_cat_status, "happiness", 2)

print(my_cat_status)
feed(my_cat_status)
pet(my_cat_status)
print(my_cat_status)