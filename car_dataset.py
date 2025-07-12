import pandas as Pd 
import matplotlib.pyplot as Mp
import seaborn as Sn

File = Pd.read_csv(r"D:\Documents\Ds_Ml\data.csv")
def File_Info():
  File.info()

def File_Desc():
    Desc = File.describe()
    print(Desc)

# print(File.isnull().sum())

def Mean():
    Num_Val = ['Model','Engine HP','Engine Cylinders','Number of Doors','highway MPG','city mpg','Popularity','MSRP']
    File[Num_Val] = File[Num_Val].apply(Pd.to_numeric, errors='coerce')
    Num_Val = File.select_dtypes(include='number')
    Num_Val.fillna(Num_Val.mean(), inplace=True)
    # print(Num_Val)
    # print(Num_Val.isnull().sum())

def Corr_Matr():
    Num_Data = File.apply(Pd.to_numeric ,errors='coerce')
    Corr_Mat = Num_Data.corr()
    print("Correlation Matrix :",Corr_Mat)

def MSRP_popularity():
    Mp.figure(figsize=(12,8))
    Sn.histplot(data=File , x='Popularity', bins=20, kde=True)
    Mp.title('Predicted price with respect to popularity')
    Mp.xlabel('Popularity')
    Mp.ylabel('MSRP')
    Mp.show()

def Top_MSRP():
    top_msrp = File.sort_values(by='MSRP',ascending = False).head(10)
    print('Top Suggested Price',top_msrp)

def Top_Pop():
    top_pop = File.sort_values(by='Popularity',ascending = False).head(10)
    print('Most Popular',top_pop)

def Low_MSRP():
    low_msrp = File.sort_values(by='MSRP',ascending = True).head(10)
    print("Lowest Suggested Price :",low_msrp)

def Low_Pop():
    low_pop = File.sort_values(by='Popularity',ascending = True).head(10)
    print("Lowest Popular :",low_pop)

def MSRP_Year():
    Mp.figure(figsize=(12, 8))
    Sn.lineplot(data=File, x='Year', y='MSRP')
    Mp.title('Top Suggested Price Based on Year')
    Mp.xlabel('Year')
    Mp.ylabel('MSRP')
    Mp.show()

def MSRP_Pop():
    Mp.figure(figsize=(12, 8))
    Sn.lineplot(data=File, x='Year', y='Popularity')
    Mp.title('Most Popularity Based on Year')
    Mp.xlabel('Year')
    Mp.ylabel('Popularity')
    Mp.show()

def EHP():
    Mp.hist(File['Engine HP'], bins=20)
    Mp.title('Engine HP with respect to Count')
    Mp.xlabel('Engine HP')
    Mp.ylabel('Count')
    Mp.show()

def HMPG_CMPG():
    Mp.scatter(File['highway MPG'], File['city mpg'])
    Mp.xlabel('Highway MPG')
    Mp.ylabel('City MPG')
    Mp.title('Scatter Plot of Highway MPG vs. City MPG')
    Mp.show()

# Num_Data = File.select_dtypes(include=['int', 'float'])
# Corr_Mat2 = Num_Data.corr()
# Mp.figure(figsize=(12, 8))
# Sn.heatmap(Corr_Mat2, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
# Mp.title('Correlation Matrix of Car Set Data')
# Mp.show()

def MSRP_Suggs():
    Mp.figure(figsize=(10, 6))
    Mp.hist(File['MSRP'], bins=20, color='pink', edgecolor='black')
    Mp.xlabel('MSRP')
    Mp.ylabel('Frequency')
    Mp.title('Distribution of Suggested Price :')
    Mp.show()

def Highest_MSRP():
    File['Model'] = File['Model'].astype(str)  # Ensure Model is string type
    Data_For_MSRP = File.sort_values(by='MSRP', ascending=False)
    top_ten_MSRP = Data_For_MSRP.head(80)
    
    Mp.figure(figsize=(12, 8))
    Mp.bar(top_ten_MSRP['Model'], top_ten_MSRP['MSRP'], color='brown')
    Mp.xlabel('Model')
    Mp.ylabel('MSRP ($)')
    Mp.title('Top 4 Cars with Highest MSRP')
    Mp.xticks(rotation=45, ha='right')
    Mp.tight_layout()
    Mp.show()

def Pop_Name():
    File['Popularity'] = Pd.to_numeric(File['Popularity'], errors='coerce')
    File_sorted = File.sort_values(by='MSRP', ascending=False)
    top_ten_MSRP = File.head(80)
    Mp.figure(figsize=(12, 6))
    Mp.bar(top_ten_MSRP['Make'], top_ten_MSRP['Model'], color='red')
    Mp.xlabel('Make')
    Mp.ylabel('Model')
    Mp.title('Top Five Popular with its Company and Model')
    Mp.xticks(rotation=45, ha='right')  
    Mp.show()

# File[''] = Pd.to_numeric(data['Half_Centuries'], errors='coerce')
# data_sorted = data.sort_values(by='Half_Centuries', ascending=False)
# top_ten_players = data_sorted.head(10)
# plt.figure(figsize=(12, 6))
# plt.bar(top_ten_players['Player_Name'], top_ten_players['Half_Centuries'], color='skyblue')
# plt.xlabel('Player Name')
# plt.ylabel('Half Centuries')
# plt.title('Top Ten Players by Half Centuries')
# plt.xticks(rotation=45, ha='right')  
# plt.show()

Mean()
print("\t\tWelcome to Car Data Set Analysis ")
print("1 : Show File Info !")
print("2 : Show File Discription !")
print("3 : Show Correlation MAtrix !")
print("4 : Show Top Suggested Price !")
print("5 : Show Top Popularity !")
print("6 : Show Lowest Suggested Price !")
print("7 : Show Lowest Popularity !")
print("8 : Show Graph for Predicted price with respect to popularity !")
print("9 : Graph For Top Suggested Price Based on Year !")
print("10 : Graph For Engine HP with respect to Count !")
print("11 : Scatter Plot Diagram of Highway MPG vs. City MPG !")
print("12 : Distribution of Suggested Price !")
print("13 : Top Four Cars with Highest MSRP !")
print("14 : Top Five Popular with its Company and Model !")
print("15 : Exit the loop !")
while (True):
    Opt = int(input("Enter the Analysis You want to see :"))
    match Opt:
        case 1 :
            File_Info()
        case 2:
            File_Desc()
        case 3:
            Corr_Matr()
        case 4:
            Top_MSRP()
        case 5:
            Top_Pop()
        case 6:
            Low_MSRP()
        case 7:
            Low_Pop()
        case 8:
            MSRP_Pop()
        case 9:
            MSRP_Year()
        case 10:
            EHP()
        case 11:
            HMPG_CMPG()
        case 12:
            MSRP_Suggs()
        case 13:
            Highest_MSRP()
        case 14:
            Pop_Name()
        case 15:
            print("Exiting The Loop !")
            break
        case _:
            print("Invalid Option !!!!!")