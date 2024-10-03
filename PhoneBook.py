Phone_Numbers = []
Options = ["yes", "no", "reverse", "nothing"]
def add_Numbers():
    userinput = input("What do you want to add? Say nothing for nothing: ")
    if userinput == "nothing":
        print(Phone_Numbers)
    else:
        Phone_Numbers.append(userinput)
        print(Phone_Numbers)
        
def remove_Numbers():
    userinput2 = input("What do you want to remove? Say nothing for nothing: ")
    if userinput2 == "nothing":
        print(Phone_Numbers)
    else:
        Phone_Numbers.remove(userinput2)
        print(Phone_Numbers)

def sort_Numbers():
    userinput3 = input("Do you want to sort by alphabetical order? Say no for no, yes for yes, and reverse for reverse sorting:")
    if userinput3 == "no":
        print(Phone_Numbers)
    elif userinput3 == "yes":
        Phone_Numbers.sort()
        print(Phone_Numbers)
    elif userinput3 == "reverse":
        Phone_Numbers.reverse()
        print(Phone_Numbers)
    else:
         print("try again")
         print(Phone_Numbers)

def search_Numbers():
    userinput4 = input("What do you want to search? say nothing for nothing: ")
    if userinput4 in Phone_Numbers:
        print(Phone_Numbers)

def main_Menu():
    while True:
        userinput5 = input("add(1), remove(2), sort(3), search(4): ")
        print(Phone_Numbers)
        if userinput5 == "1":
            add_Numbers()
        if userinput5 == "2":
            remove_Numbers()
        if userinput5 == "3":
            sort_Numbers()
        if userinput5 == "4":
            search_Numbers()
main_Menu()