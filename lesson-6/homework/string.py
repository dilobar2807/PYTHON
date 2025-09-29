# Given a string txt, insert an underscore (_) after every third character. 
# If a character is a vowel or already has an underscore after it, shift the underscore placement
# to the next character. No underscore should be added at the end.
txt='assalossm'
index=2
used_char=['o', 'u', 'i', 'e', 'a']
while index<len(txt)-1:
    if txt[index] not in used_char:
        used_char.append(txt[index])
        txt=txt[: index+1]+'_'+txt[index+1:]
        index+=4
    else: 
        index+=1
print(txt)

# The provided code stub reads an integer, n, from STDIN. 
# For all non-negative integers i where 0 <= i < n, print i^2.

n=int(input("n sonni kiriting: "))
for i in range(n):
    i=i*i
    print(i)
    i+=i

# 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop
i=0
while i<11:
    print(i)
    i+=1

#Exercise 2: Print the following pattern

i=1
while i<=5:
    j=1
    while j<=i:
        print(j, end=' ')
        j+=1
    print()
    i+=1

#Exercise 3: Calculate sum of all numbers from 1 to a given number
n=int(input("n sonni kiriting: "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)

#Exercise 4: Print multiplication table of a given number
i=1
while i<=10:
    print(i*2)
    i+=1


#Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num>500:
        break
    else:
        continue
print(num)

#Exercise 6: Count the total number of digits in a number
num=int(input("Istalgan xonali son kiriting: "))
hisoblagich=0
while num!=0:
    num//=10
    hisoblagich+=1
print(hisoblagich)

#Exercise 7: Print reverse number pattern

i=5
while i>=1:
    j=i
    while j>=1:
        print(j, end=' ')
        j-=1
    print()
    i-=1
  
#Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
i=len(list1)-1
while i>=0:
    print(list1[i])
    i-=1

#Exercise 9: Display numbers from -10 to -1 using a for loop
i=-10
while i<=-1:
    print(i)
    i+=1

#Exercise 10: Display message “Done” after successful loop execution
i=0
while i<=10:
    if i==5:
        print("Done")
        break
    print(i)
    i+=1

# #Exercise 11: Print all prime numbers within a range

# Boshlanish va tugash sonlarini belgilaymiz
L = 10
R = 30

# Tub sonlarni topish uchun L dan R gacha bo'lgan sonlarni tekshiramiz
n = L  # n - hozir tekshirilayotgan son

while n <= R:
    if n < 2:
        n += 1
        continue  # 0 va 1 tub emas, shu bois o'tkazib yuboramiz

    # Har bir son uchun bo'luvchilarni tekshiramiz
    i = 2
    tubmi = True  # Avvaliga bu son tub deb hisoblaymiz

    while i * i <= n:
        if n % i == 0:
            tubmi = False  # Agar bo'linib qolsa, bu son tub emas
            break  # Tekshirishni to'xtatamiz
        i += 1

    # Agar son tub bo'lsa, uni chiqaramiz
    if tubmi:
        print(n, "tub son")

    n += 1  # Keyingi songa o'tamiz

#Exercise 12: Display Fibonacci series up to 10 terms

#Fibonacci sequence:
#0  1  1  2  3  5  8  13  21  34   
n=10
a, b=0, 1
i=0
while i<n:
    print(a, end=' ')
    a, b=b, a+b
    i+=1

#Exercise 13: Find the factorial of a given number

n=int(input("n sonni kiriting! "))
i=1
mul=1
while i<n+1:
    mul*=i
    i+=1
print(f"{n}!=", mul)

# 4. Return Uncommon Elements of Lists
list_1=[1, 3, 5, 7]
list_2=[3, 5, 7, 12, 15]
list_s_1=set(list_1)
list_s_2=set(list_2)
print(list_s_1.symmetric_difference(list_s_2))
