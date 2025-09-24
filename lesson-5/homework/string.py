#  1) 
def is_leap_year(year):
    if not isinstance(year, int):
        raise ValueError("Yil butun son bo‘lishi kerak.")

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

# 2) 
n = int(input("n sonini kiriting: "))
if n % 2 !=0:
    print("Weird")
elif n % 2 ==0:
    if 2<n<5:
        print("Not weird")
    elif 6<n<20:
        print("Weird")
    elif n>20:
        print("Not weird")

#3) Given two integer numbers a and b. Find even numbers between this numbers.
# a and b are inclusive. Don't use loop.
a = 3
b = 15

even_numbers = list(filter(lambda x: x % 2 == 0, range(a, b + 1)))
print(even_numbers)
