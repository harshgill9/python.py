age=int(input("enter your age : "))
gender=input("enter your gender : ")
if age>15:
    if gender=="Male":
        print("you are male")
    elif gender=="Female":
        print("you are a adoult female")
    else:
        print("you are femlae")

else:
    print("you are minor")
    