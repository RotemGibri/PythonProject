#coffee making
coffee_typs = {1: "espresso" , 2: "americano", 3: "cappuccino"}
milk_typs = {1: "cow milk" , 2: "soy milk", 3: "out milk"}


def choose_coffee_type (coffe_type):
    coffe_type = int(input(f"what coffe do you want? {coffee_typs}"))
    print(f"you chose " + coffee_typs[coffe_type])

def choose_milk_typ (coffe_type):
    milk_type = int(input(f"what milk do you want? {milk_typs}"))
    print(f"you chose " + milk_type[milk_typs])

if __name__ ==  "__main__":

    print("welcome to our coffee machine")
    choose_coffee_type(coffee_typs)
    coffe = input ("is there coffee in the machine? y/n ")
    if coffe == "n" :
        print ("add coffee to the machine")
    else:
        print ("grinding your coffee...")

    water = input ("is there coffee in the machine? y/n ")
    if coffe == "n" :
        print ("add water to the machine")
    else:
        print ("boiling your coffee...")

    print ("now its time to put your favorite glass ")

    choose_milk_typ(milk_typs)
    #input- milk?
#input- what kind?
#input- shuger?
#stirr
#drink
