#####  HOMEWORK-1     #######

import pandas as pd
data={"First Name": ['Alice', 'Bob', 'Charlie', 'David'],
      "Age": [25, 30, 35, 40],
      'City': ['New York', 'Los Angelos', 'San Fransisco', 'Chicago']}
d_f=pd.DataFrame(data)

#Rename column names using function. "First Name" --> "first_name", "Age" --> "age

d_f.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)
d_f

#Print the first 3 rows of the DataFrame

d_f.head(3)

#Find the mean age of the individuals
d_f.age.mean()

#Select and print only the 'Name' and 'City' columns

data={"First Name": ['Alice', 'Bob', 'Charlie', 'David'],
      "Age": [25, 30, 35, 40],
      'City': ['New York', 'Los Angelos', 'San Fransisco', 'Chicago']}
d_f=pd.DataFrame(data)
d_f[["First Name", "City"]]

#Add a new column 'Salary' with random salary values
d_f['Salary']=[12000, 34000, 21000, 15000]
d_f

#Display summary statistics of the DataFrame
d_f.describe()

##########      HOMEWORK 2      ##############

#1. Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly 
# sales and expenses data. Use below table.
data={
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expences': [3000, 3500, 4000, 4500]
}

d_f=pd.DataFrame(data)
d_f

#2. Calculate and display the maximum sales and expenses.

print("Maximum Sales: ", d_f['Sales'].max(),    "Maximum Expences: ", d_f['Expences'].max())

#3.Calculate and display the minimum sales and expenses.

print("Minimum Sales: ", d_f['Sales'].min(),    "Minimum Expences: ", d_f['Expences'].min())

# 4.Calculate and display the average sales and expenses.

print("Average Sales: ", d_f['Sales'].mean(),    "Average Expences: ", d_f['Expences'].mean())



#########   HOMEWORK 3 #########

#1. Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', 
# representing monthly expenses for different categories. Use below table.
import pandas as pd

exp={
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February':[1300, 220, 320, 160],
    'March':[1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expences=pd.DataFrame(exp)
expences=expences.set_index('Category')

#Calculate and display the maximum expense for each category.
expences['Max']=expences.loc[:, 'January':'April'].max(axis=1)
expences

#Calculate and display the minimum expense for each category.
expences['Min']=expences.loc[:, 'January':'April'].min(axis=1)
expences

#Calculate and display the average expense for each category.
expences['Average']=expences.loc[:, 'January':'April'].mean(axis=1)
expences
