# katz_deli = []
def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        deli_string = ""
        for i in range(len(katz_deli)):
            deli_string += f" {i + 1}. {katz_deli[i]}"
        print(f"The line is currently:{deli_string}")
    

def take_a_number(katz_deli, new_person):
    print(f"Welcome, {new_person}. You are number {len(katz_deli) + 1} in line.")
    katz_deli.append(new_person)

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        current_person = katz_deli[0]
        del(katz_deli[0])
        print(f"Currently serving {current_person}.")