# Expense Tracker with NumPy
import numpy as np

month = int(input("Enter How Many Months Are there: "))
Arr = np.zeros((month,4))

for i in range(month):
    Car_Exp = int(input(f"Enter Car Expenses for Month {i+1} :"))
    House_rent = int(input(f"Enter House Expenses for Month {i+1} :" ))
    Elec_Bill = int(input(f"Enter Electrical Expenses for Month {i+1} :"))
    Food_Bevr = int(input(f"Enter Food and Beverages Expenses for Month {i+1} :"))
    Arr[i]=[Car_Exp,  House_rent , Elec_Bill , Food_Bevr]

print("Final Expeses of Car , House_rent , Elec_Bill , Food_Bevr :\n",Arr)

for i in range(month):
    Total = np.sum(Arr[i])
    print(f"The Total Expense Of Month {i+1} is : {Total}")
    Avg = np.average(Arr[i])
    print(f"The Average Expense Of Month {i+1} is : {Avg}")
    Max = np.max(Arr[i])
    print(f"The Maximum Expense Of Month {i+1} is : {Max}")
    Min = np.min(Arr[i])
    print(f"The Minimum Expense Of Month {i+1} is : {Min}")