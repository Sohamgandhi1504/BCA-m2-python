name = input("Enter Your Name :")
sub1 = int(input("Enter Marks of Subject 1:"))
sub2 = int(input("Enter Marks of Subject 2:"))
sub3 = int(input("Enter Marks of Subject 3:"))
sub4 = int(input("Enter Marks of Subject 4:"))
sub5 = int(input("Enter Marks of Subject 5:"))
Res = (sub1+sub2+sub3+sub4+sub5)/5

if Res >= 80 :
    print(f"Congratulations !\n{name} scored an A")
elif 50 <= Res <80:
    print(f"Congratulations !\n{name} scored an B")
else :
    print(f"Better Luck Next Time {name} !")
