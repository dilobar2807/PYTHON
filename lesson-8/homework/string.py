#Exception Handling Exercises
#1. Write a Python program to handle a ZeroDivisionError exception when dividing 
# a number by zero.
try:
    a=float(input("a sonni kiriting: "))
    b=float(input("b sonni kiriting: "))
    natija=a/b
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas")
else:
    print("Sizning natijangiz {res} ga teng")

# 2. Write a Python program that prompts the user to input an integer and 
# raises a ValueError exception if the input is not a valid integer.
while True:
    try:
        a=int(input("Iltimos butun son kiriting: "))
        print("Kiritilgan sonning kvadrati: ", a**2)
        break
    except ValueError:
        print("int typedagi qiymat kiritishingiz  kerak")

#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the
#  file does not exist.

try:
    file=input("Fileni kiriting: ")
    with open(file, 'r') as f:
        mazmuni=f.read()
        print("File mazmuni: \n", mazmuni)
except FileNotFoundError:
    print("Bunday file topilmadi")

#4. Write a Python program that prompts the user to input two numbers and raises a TypeError 
# # exception if the inputs are not numerical.
try:
    a = input("a sonni kiriting: ")
    b = input("b sonni kiriting: ")
    
    # a va b ni son (int yoki float) qilib olish kerak
    a = int(a)
    b = int(b)
    
    natija = a + b / b
    print("Natija:", natija)

except TypeError:
    print("TypeError: Noto'g'ri tipdagi qiymat bilan amal bajarishga harakat qilindi.")
except ValueError:
    print("ValueError: Son emas, noto‘g‘ri qiymat kiritdingiz.")
except ZeroDivisionError:
    print("ZeroDivisionError: Nolga bo‘lish mumkin emas.")

#5. Write a Python program that opens a file and handles a PermissionError exception
#  if there is a permission issue.

try:
    file=input("Fileni kiriting: ")
    with open(file, 'w') as f:
        for line in f:
            print(line)
except PermissionError:
    print("Siz sizga ruxsat berilmagan filega kirishga harakat qilyapsiz")

#6. Write a Python program that executes an operation on a list and handles an IndexError
#exception if the index is out of range.

try:
    my_list=['apple', 'lemon', 'banana', 'pear']
    index=int(input("Qaysi indexdagi elementni ko'rmoqchisiz? "))
    element=my_list[index]
    print(f"{index} indexdagi element {element}")
except IndexError:
    print(f"Siz ko'rmoqchi bo'lgan {index}- indexdagi element mavjud emas")
except ValueError:
    print("Int tipidagi qiymat kiriting")

#7.Write a Python program that prompts the user to input a number and handles a 
# KeyboardInterrupt exception if the user cancels the input.
try:
    i=1
    while i<=10:
        print(i)
except KeyboardInterrupt:
    print("Jarayon dasturchi tomonidan to'xtatildi!")

#8.Write a Python program that executes division and handles an ArithmeticError exception 
# if there is an arithmetic error.

try:
    result=10/0
except ArithmeticError:
    print(f"ArithmeticError")

#9.Write a Python program that opens a file and handles a UnicodeDecodeError exception 
# if there is an encoding issue.

filename='uniq.txt'
try:
    with open(filename, 'w', encoding='latin-1') as f:
        f.write("Salom bu n harfi")
except UnicodeDecodeError:
    print("Xatolik: Fileni UTF-8 kodlashda o'qib bo'lmadi")
except FileNotFoundError:
    print(f" Xatolik: {filename} file topilmadi")

#10.Write a Python program that executes a list operation and handles an AttributeError
#exception if the attribute does not exist.
try:
    class Avto:
        def __init__(self, model):
            self.model=model

    avto=Avto("Tesla")
    print(avto.color)
except AttributeError:
    print("Siz kiritayotgan attribute bu klassga tegishli emas")

#File input/output exercises
#1.Write a Python program to read an entire text file.

with open ("C:\\Users\\Sardor\\OneDrive\\Documenti\\tire.txt") as f:
    for line in f:
        print(line.strip())

#2.Write a Python program to read first n lines of a file.

n=int(input("Faylning birinchi qatoridan nechanchi qatorgacha o'qimoqchisiz? "))
file_path="C:\\Users\\Sardor\\OneDrive\\Documenti\\tire.txt"
with open(file_path, 'r', encoding='utf-8') as f:
    for i in range(n):
        line=f.readline()
        if  not line:
            break
        print(line.strip())

#3. Write a Python program to append text to a file and display the text.

with open('entire.txt', 'a') as f:
    f.write("\nNechun vatan deya yeru osmonni\nMuqaddas atayman atayman tanho")

#Endi yangilangan faylni ekranga chiqaramiz
with open('entire.txt', 'r') as f:
    content=f.read()
    print(content)

#4.Write a Python program to read last n lines of a file.

def read_lines(filepath, n):
    with open ("C:\\Users\\Sardor\\OneDrive\\Documenti\\tire.txt") as f:
        lines=f.readlines()
    last_lines=lines[-n:]
    for line in last_lines:
        print(line)

n=int(input("Oxirgi nechta qatorni ko'rmoqchisiz? "))
file_path="C:\\Users\\Sardor\\OneDrive\\Documenti\\tire.txt"
read_lines(file_path, n)

#5.Write a Python program to read a file line by line and store it into a list.

file_path="C:\\Users\\Sardor\\OneDrive\\Documenti\\tire.txt"
lines=[]
with open(file_path, 'r') as f:
    for line in f:
        lines.append(line)

print(lines)
    
#6. Write a Python program to read a file line by line and store it into a variable.

file_path="C:\\Users\\Sardor\\OneDrive\\Documenti\\tire.txt"
content=""
with open(file_path, 'r') as f:
    for line in f:
        content+=line
        
print(content)


# #8.Write a Python program to find the longest words.
def find_longest_word(filename):
    
    longest_words=[]
    max_len=0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                clean_word=word.strip(", \n . \t").lower()
                word_len=len(clean_word)

                if word_len>max_len:
                    longest_words=[clean_word]
                    max_len=word_len
                elif word_len==max_len:
                    if clean_word not in longest_words:
                        longest_words.append(clean_word)

    return longest_words, max_len

longest_words, max_len= find_longest_word('entire.txt')                

#9.Write a Python program to count the number of lines in a text file.

def line_counter(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
            lines=f.readlines()
            len_line=len(lines)
    return len_line
            
len_line = line_counter("entire.txt")  
print(f"Fayldagi qatorlar soni: {len_line}")

#10.Write a Python program to count the frequency of words in a file.
words=[]
with open('entire.txt', 'r', encoding='utf-8') as f:
    for line in f:
        for word in line.split():
            clean_word=word.strip(", \n . \t")
            words.append(clean_word)
            

#11. Write a Python program to get the file size of a plain file.
import os

# Fayl nomini kiriting (yoki to'liq yo'lini)
file_path = 'entire.txt'  # O'zingizga kerakli fayl nomini bu yerga yozing

# Tekshiramiz: Fayl mavjudmi va oddiy faylmi?
if os.path.isfile(file_path):
    file_size = os.path.getsize(file_path)  # Hajmi baytlarda
    print(f"'{file_path}' faylining hajmi: {file_size} bayt")
else:
    print(f"'{file_path}' degan oddiy fayl topilmadi yoki bu fayl emas.")

#12.Write a Python program to write a list to a file.

my_list=['olma', 'anor', 'nok', 'apelsin', 'tarvuz', 'qovun']
filename='entire.txt'
with open(filename, 'w', encoding='utf-8') as file:
    for item in my_list:
        file.write(item+'\n')

print(f"Ro'yhat ichidagi so'zlar {filename} fayliga muvaffaqqiyatli yozildi")

#13. Write a Python program to copy the contents of a file to another file.

with open('entire.txt', 'r', encoding='utf-8') as file:
    matn=file.read()

with open('new.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(matn)

print("Fayl muvaffaqqiyatli nusxalandi.")

#14.Write a Python program to combine each line from the first file with the corresponding 
# line in the second file.
# Fayllarni ochamiz
with open('fayl1.txt', 'r') as fayl1, open('fayl2.txt', 'r') as fayl2:
    # Har ikki fayldan qatorma-qator o'qiladi
    for qator1, qator2 in zip(fayl1, fayl2):
        # Qatorlardagi ortiqcha bo'sh joylarni olib tashlaymiz
        qator1 = qator1.strip()
        qator2 = qator2.strip()

        # Qatorlarni birlashtiramiz va chiqaramiz
        birlashgan = qator1 + " " + qator2
        print(birlashgan)

#15.Write a Python program to read a random line from a file.

import random

# Fayldagi barcha qatorlarni o'qib olamiz
with open('fayl.txt', 'r') as fayl:
    qatorlar = fayl.readlines()

# Tasodifiy bir qatorni tanlaymiz
tasodifiy_qator = random.choice(qatorlar)

# Natijani chiqaramiz
print("Tanlangan qator:")
print(tasodifiy_qator.strip())

#16.Write a Python program to assess if a file is closed or not.
# Faylni ochamiz
fayl = open('entire.txt', 'r')

# Fayl yopilgan yoki yopilmaganligini tekshiramiz
if fayl.closed:
    print("Fayl yopilgan.")
else:
    print("Fayl hali yopilmagan.")

# Faylni yopamiz
fayl.close()

# Yana tekshiramiz
if fayl.closed:
    print("Fayl yopilgan.")
else:
    print("Fayl hali yopilmagan.")



