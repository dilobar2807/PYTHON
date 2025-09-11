#1) Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name=input("Ismingizni kiriting: ") 
birth=int(input("Tugilgan yilingizni kiriting: "))
print(f"{name.title()}, sizning yoshingiz {2025-birth} yoshda!")

#2) Extract car names from the following text:
#Quyidagi matndan mashina nomlarini ajrating: 

txt = 'LMaasleitbtui'
print('LM\baa\bsl\bei\btb\btu\bi')

#3)Extract car names from the following text:

txt = 'MsaatmiazD'
txt='Ms\baa\btm\bia\bzD\b'
print(txt[0:-2])

#4) Extract the residence area from the following text:

txt = "I'am John. I am from London"
print(txt[-6:])

#5)Write a Python program that takes a user input string and prints it in reverse order.

word=input('Xoxlagan so\'zingizni kiriting: ')
print(word[::-1])

#6) Write a Python program that counts the number of vowels in a given string.

word=input("Istalgan so'zingizni kiriting: ")
a=word.count('a')
o=word.count('o')
e=word.count('e')
i=word.count('i')
u=word.count('e')
unli_soni=a+o+e+i+u
print("Matndagi unli harflar soni: ",unli_soni)

#7) Write a Python program that takes a list of numbers as input and prints the maximum value.

sonlar = input("1 xonali sonlarni vergul bilan kiriting (masalan: 5,3,9,2): ")
raqamlar = sonlar.split(",")  
eng_katta = max(rakam.strip() for rakam in raqamlar)
print("Eng katta raqam:", eng_katta)

#8)Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word=input("Ixtiyoriy so'z kiriting: ")
polindrome=word[::1]
if word==polindrome:
   print('Bu so\'z polindrom')
else:
  print("Bu so'z polindrom emas")

#9)Write a Python program that extracts and prints the domain from an email address provided by the user.
e_mail = input("E_mailingizni kiriting: ")

part = e_mail.split('@')

if len(part) == 2:
    domen = part[1]  # '@' dan keyingi qism
    print("Email domeni:", domen)
else:
    print("Noto'g'ri email manzili!")

#10) Write a Python program to generate a random password containing letters, digits, and special characters.
#xarflar, raqamlar va belgilardan tashkil topgan tasodifiy password yaratadigan kod yozing
characters=input("Harflar, raqamlar va belgilardan tashkil topgan, kamida 8 xonalik ixtiyoriy matn kiriting: ")
print(characters[0:12])

