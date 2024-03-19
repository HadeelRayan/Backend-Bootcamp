def get_input():
    msg = input("what is your msg? ")
    while len(msg) == 0:
        print("Invalid input, enter your msg")
        msg = input("what is your msg? ")

    return msg

