import random
import string

try:
    length = int(input("Enter the length of the password you want: "))
    print("Enter A for Alphabet\nEnter 1 for numeric\nEnter $ for dollar")
    data = input("Enter the type of character you want: ")

    pawd = ""
    
    if data.lower() == 'a':
        for i in range(0, length):
            pawd += random.choice(string.ascii_letters)
        print("Generated password:", pawd)
          
    elif data == '1':
        for i in range(0, length):
            x = str(random.randint(1, 9))
            pawd += x
        print("Generated password:", pawd)

    elif data == '$':
        for i in range(0, length):
            x = random.choice(string.punctuation)
            pawd += x
        print("Generated password:", pawd)
    else:
        print("Invalid Selection")


except ValueError as e:
    print("Please Enter a Integer ")
