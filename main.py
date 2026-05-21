from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)







import math

I = float(input("Your number is: "))

QN = input("Do you need the log operator? (Yes or No): ")


if QN == "Yes" or QN == "yes":
    print("Your answer is: ", math.log10(I))
     

else:
    I2 = float(input("Your second number is: "))
    I3 = input("Your operation is: ")
 
    if I3 == "+":
        print("Your answer is: ", I + I2)
       
    elif I3 == "-":
        print("Your answer is: ", I - I2)
       

    elif I3 == "*":
        print("Your answer is:")
        print(I * I2)

    elif I3 == "/":
        if I2 != 0:
            print("Your answer is:")
            print(I / I2)
        else:
            print("Cannot divide by 0")

    elif I3 == "%":
        print("Your remainder is:")
        print(I % I2)

    else:
        print("Invalid")