# Bus ticket fare calculator (with age-based discount)
print("\t\t\tWelcome To Bus ticket fare Calculator \nDiscounts on Age Below 10(-40%) And Above 70(-30%)")
num = int(input("Enter Total Members :"))
Total_Val = 0
Basic_Val = 0
Below_10 = int(input("Enter Number of Members below the Age of 10 :"))
Above_70 = int(input("Enter Number of Members above the Age of 70 :"))
print("1: Jammu Kashmir(1000 For Each) \n2: Haryana(600 For Each) \n3: Uttar Pradesh(500 For Each)")
Dest = int(input("Enter Destination :"))
if Dest == 1 :
    Basic_Val = num*1000
    Bel_10_Val = (((Below_10*1000)*40)/100)
    Abo_70_Val = (((Above_70*1000)*30)/100)
    Total_Val = (Basic_Val - (Bel_10_Val + Abo_70_Val))
    print(f"Total Fare for {num} members which have {Below_10} members Below 10 and {Above_70} members above 70 :",Total_Val)
    print("HAVE A GREAT JOURNEY TO JAMMU & KASHMIR !!!!!!")
elif Dest == 2 :
    Basic_Val = num*600
    Bel_10_Val = (((Below_10*600)*40)/100)
    Abo_70_Val = (((Above_70*600)*30)/100)
    Total_Val = (Basic_Val - (Bel_10_Val + Abo_70_Val))
    print(f"Total Fare for {num} members which have {Below_10} members Below 10 and {Above_70} members above 70 :",Total_Val)
    print("HAVE A GREAT JOURNEY TO HARYANA !!!!!!")
elif Dest == 3:
    Basic_Val = num*500
    Bel_10_Val = (((Below_10*500)*40)/100)
    Abo_70_Val = (((Above_70*500)*30)/100)
    Total_Val = (Basic_Val - (Bel_10_Val + Abo_70_Val))
    print(f"Total Fare for {num} members which have {Below_10} members Below 10 and {Above_70} members above 70 :",Total_Val)
    print("HAVE A GREAT JOURNEY TO UTTAR PRADESH !!!!!!")
else :
    print("Invalid Option !!!!!")