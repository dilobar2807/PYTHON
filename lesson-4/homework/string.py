#1)Write a Python script to sort (ascending and descending) a dictionary by value.

names=dict(first='Ali', second='Vali', third='Eshmat', fourth='Toshmat', fifth='Guli')
a_names=dict(sorted(names.items()))
print(a_names)

names=dict(first='Ali', second='Vali', third='Eshmat', fourth='Toshmat', fifth='Guli')
d_names=dict(sorted(names.items(), reverse=True))
print(d_names)

# 2) Write a Python script to add a key to a dictionary.

a={0: 10, 1: 20}
a[2]=30
print(a)

#3) Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#4) Write a Python script to generate and print a dictionary that contains a number 
#(between 1 and n) in the form (x, x*x).
#Foydalanuvchidan n sonini olish
n = int(input("n ni kiriting: "))

# Dictionary hosil qilish
squares = {}

for x in range(1, n + 1):
    squares[x] = x * x

# Natijani chiqarish
print(squares)

#5) Write a Python script to print a dictionary where the keys are numbers between 
# 1 and 15 (both included) and the values are the square of the keys.

n = int(input("n ni kiriting: "))

# Dictionary hosil qilish
squares = {}

for x in range(1, n + 1):
    squares[x] = x * x

# Natijani chiqarish
print(squares)

#Set exercises
#1) Write a Python program to create a set.

my_set={1, 2, 3, 4}
print(my_set)

#2) Write a Python program to iterate over sets.

n_set={'Naima', 'Xolida', 'Anora', 'Mohinur', 'Xilola'}

for n in n_set:
    print(n)

#3) Write a Python program to add member(s) to a set.

names={'John', 'James', 'Alice', 'Mike', 'Elena'}
names.update(['Oliver', 'Tomas'])
print(names)

# 4) Write a Python program to remove item(s) from a given set.

names={'Tomas', 'John', 'James', 'Alice', 'Oliver', 'Elena', 'Mike'}
names.remove('Tomas')
names.discard('Elena')
print(names)

#5) Write a Python program to remove an item from a set if it is present in the set.

nums={1,6,8,-9,6,7}
nums.discard(1)
print(nums)
