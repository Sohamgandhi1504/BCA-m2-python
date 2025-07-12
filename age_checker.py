name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))

if age >= 18 :
    print(f"{name} is Legal for Driving and Voting !")
else :
    res = 18 - age
    print(f"Comeback after {res} Years !")