#1) Create a list containing five different fruits and print the third fruit.

fruits=['apple', 'lemon', 'pineapple', 'melon', 'watermelon']
print(fruits[2])

#2) Create two lists of numbers and concatenate them into a single list.

numbers_1=[1, 3, 5, 7, 9]
numbers_2=[2, 4, 6, 8, 10]
numbers_3=numbers_1+numbers_2
print(numbers_3)

#3) Given a list of numbers, extract the first, middle, and last elements and store them 
# in a new list.
numbers=[1,2,3,4,5,6,7,8,9,10]
new_nums=[]
first=numbers[0]
last=numbers[-1]
n=len(numbers)//2
middle=numbers[n]
new_list=[first, middle, last]
print("Yangi list: ", new_list)

#4)Create a list of your five favorite movies and convert it into a tuple.

movies=['Qish sonatasi', 'Yoz ifori', 'Kuz ertagi', 'Bahor nafasi', 'Muxtasham']
movies_t=tuple(movies)
print('Ruyhat: ', movies)
print('Tuple: ', movies_t)

 #5) Given a list of cities, check if "Paris" is in the list and print the result.

# Shaharlar ro'yxati
cities = ['London', 'New York', 'Paris', 'Tokyo', 'Berlin']
# "Paris" bor-yo'qligini tekshiramiz
if "Paris" in cities:
    print("Paris ro'yxatda mavjud.")
else:
    print("Paris ro'yxatda mavjud emas.")
#6) Create a list of numbers and duplicate it without using loops.
list=[10, 20, 30, 40, 50, 60, 70, 80]
copied_list=list.copy()
print(copied_list)

#7) Given a list of numbers, swap the first and last elements.

nums_1=[23, 455, -9, 35.6, 7, -90]
nums_1[0]=45
nums_1[-1]=66
print(nums_1)

#8) Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

a=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a[3:7])

#9) Create a list of colors and count how many times "blue" appears in the list.

colors=['black', 'white', 'blue', 'red', 'blue', 'violet', 'brown']
print(colors.count('blue'), "marta takrorlangan")

10) Given a tuple of animals, find the index of "lion".
animals=('lion', 'monkey', 'donkey', 'snake', 'monkey')
print("Lion ni indeksi: ", animals.index('lion'))

# #11) Create two tuples of numbers and merge them into a single tuple.

a=(4, 7, -56, 8, 9, 17)
b=(8, 10, -8, 67, 9)
c=a+b
print(c)

#12) Given a list and a tuple, find and print their lengths.

a_list=['Ali', 'Vali', 'Nemat', 'Asror', 'Eshmat']
a_tuple=('apple', 'banana', 'lemon', 'pineapple', 'melon', 'watermelon')
print('a_listning uzunligi:  ', len(a_list))
print("a_tuple ning uzunligi: ", len(a_tuple))

#13) Create a tuple of five numbers and convert it into a list.

tuple_a=(1, 67, 87, -8, 7)
list_a=list(tuple_a)
print(list_a)

#14) Given a tuple of numbers, find and print the maximum and minimum values.

tuple_n=(45, 76, -89, 1, 0, 12)
tuple_m=sorted(tuple_n)
print(tuple_n)
print("Max value: ", tuple_m[-1])
print("Min value: ", tuple_m[0])

#15) Create a tuple of words and print it in reverse order.
fruits=('banana', 'orange', 'lemon', 'melon', 'watermelon')
l_fruits=list(fruits)
print(l_fruits[::-1])

