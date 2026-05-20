import math

I = float(input("Your number is: "))

QN = input("Do you need the log operator? (Yes or No): ")

# FIX 1: correct way to compare strings
if QN == "Yes" or QN == "yes":
    print("Your answer is:")
    print(math.log10(I))

else:
    I2 = float(input("Your second number is: "))
    I3 = input("Your operation is (+(plus), -(minus), *(times), /(divide), %(remainder)): ")

    if I3 == "+":
        print("Your answer is:")
        print(I + I2)

    elif I3 == "-":
        print("Your answer is:")
        print(I - I2)

    elif I3 == "*":
        print("Your answer is:")
        print(I * I2)

    elif I3 == "/":
        if I2 != 0:   # safety check
            print("Your answer is:")
            print(I / I2)
        else:
            print("Error: Cannot divide by zero")

    elif I3 == "%":
        print("Your remainder is:")
        print(I % I2)

    else:
        print("Invalid operation")