# Student Marks Management
stud = {'Prakhar':89 , 'Suhani':90 , 'Priyanshu':91 , 'Ankit':96 }
print("Welcome to Student Marks Management !!!!")
print("1. Add A Student Record\n2. Update Marks\n3. Display Highest ,Lowest and Average Marks !\n4. Show all Records !")
opt = int(input("Enter Your Option :"))
if opt == 1:
    sname = input("Enter Name of Student :")
    smarks = input("Enter Marks :")
    stud[sname] = smarks
    print(stud)
elif opt == 2:
    sname = input("Enter name to update mark: ")
    smarks = int(input("Enter marks to update: "))
    stud[sname] = smarks
elif opt == 3:
        sum = 0
        c = 0
        min = 100
        max = 0
        for i in stud:
            sum += stud[i]
            c += 1
            if stud[i] < min:
                min = stud[i]
            if stud[i] > max:
                max = stud[i]
        print("Highest marks: ", max)
        print("Lowest marks: ", min)
        print("Average marks: ", sum/c)
elif opt == 4:
        for i in stud:
            print(i, " : ", stud[i])