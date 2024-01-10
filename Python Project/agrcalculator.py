def Agecalculator(y,m,d):
    import datetime
    today = datetime.datetime.now().date()
    dob=datetime.date(y,m,d)
    age=int((today-dob).days/365.25)
    print(age)

y=int(input("Enter Year of birth:-"))
m=int(input("Enter Month of birth:-"))
d=int(input("Enter Date of birth:-"))
Agecalculator(y,m,d)