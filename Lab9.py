def encode(password):
    password_list=[]
    for char in password:
        new_num=int(char)
        password_list.append(new_num)
    return ''.join(password_list)
    
def decode(password):
    print(f"The encoded password is {encode(password)}, The original passowrd is {password}")

while True:
    print("Menu")
    print("------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter a password to encode: ")
        encode(password)
        print("Your password has been encoded and stored!")

    elif option == 2:
        decode(password)
    elif option == 3:
        print("")
        break
