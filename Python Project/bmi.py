height=float(input("Enter your height in cm:-"))
weight=float(input("Ente your weight in kg:-"))

height=height/100

BMI = weight/(height * height)

print("Your Body Mass Index is:",BMI)

if BMI>0:

    if BMI<18.5:
        print("Underweight")

    elif BMI<=25:
        print("Healthly weight")

    elif BMI<=30:
        print("Overweight")   

    else:
        print("Obese")   

else:
    print("you have Enter invalid Details:")