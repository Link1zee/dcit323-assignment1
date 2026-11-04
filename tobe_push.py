def push():
    response = input("Do you wanna know what i can do? (y/n): ").lower()
    if response == "y":
        print("I submit assignment 1")
    elif response == "n":
        print("Why then did u view me")
    else:
        print("Obey simple instructions")
        push()

push()