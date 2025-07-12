import pandas as Pd
import matplotlib.pyplot as Mp
import seaborn as Sn

File = Pd.read_csv(r"D:\Documents\Ds_Ml\marks.csv")
# File.info()

def Mean():
    print("Mean: ", File['Marks'].mean())
# Mean()

def Median():
    # print(Sorted_File)
    print("Median :",File['Marks'].median())
# Median()

def Mode():
    print("Mode:\n", File['Marks'].mode())
# Mode()

def Standard_deviation():
    print("Standard Deviation: ", File['Marks'].std())
# Standard_deviation()

def Variance():
        print("Varience:",File['Marks'].var())
# Varience()

def Graph():
    Mp.figure(figsize=(12,8))
    Mp.bar(File.Student,File.Marks)
    Mp.title("Graph for Marks Vs Student :")
    Mp.xlabel("Students")
    Mp.ylabel("Marks")
    Mp.show()

print("Welcome to Student Marks Analysis using Statistics")
print("1 : Mean")
print("2 : Median")
print("3 : Mode")
print("4 : Standard Deviation")
print("5 : Variance")
print("6 : Graph for Marks Vs Student")
while (True):
    Opt = int(input("Enter Your Choice :"))
    match Opt:
        case 1 :
            Mean()
        case 2 :
            Median()
        case 3 :
            Mode()
        case 4 :
            Standard_deviation()
        case 5 :
            Variance()
        case 6 :
            Graph()
        case 7 :
            print("Exiting The Loop !!")
            break
        case _:
            print("Invalid Option ")