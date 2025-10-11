#1.Write a Python program to create a class representing a Circle. Include methods to calculate
#its area and perimeter.

from math import pi
class Circle:
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        natija=int(pi*(self.radius**2))
        return  f"Radiusi {self.radius} ga teng bo'lgan doira yuzi {natija} ga teng."
    
    def perimeter(self):
        natija=int(2*pi*(self.radius))
        return f"Radiusi {self.radius} ga teng bo'lgan doira perimetri {natija} ga teng"
    
    
circle1=Circle(7)
print(circle1.perimeter())

#2. Write a Python program to create a Person class. Include attributes like name, country,
#and date of birth. Implement a method to determine the person's age.
from datetime import datetime
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
    
    def age(self):
        birthday=datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        bugun=datetime.today()
        age=bugun.year-birthday.year
        return f"{self.name} ning yoshi {age} da"
    
person1=Person("Zilola", "Uzbekistan", "1993-07-25")
print(person1.age())

#3.Write a Python program to create a Calculator class. Include methods for basic arithmetic
#operations.

class Calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    
    def addition(self):
        return f"{self.a}+{self.b}={self.a+self.b}"
    
    def subtraction(self):
        return f"{self.a}-{self.b}={self.a-self.b}"

    def multiplication(self):
        return f"{self.a}*{self.b}={self.a*self.b}"
    
    def division(self):
        return f"{self.a}/{self.b}={self.a/self.b}"
    
calc1=Calculator(5, 8)
print(calc1.addition())
print(calc1.subtraction())
print(calc1.multiplication())
print(calc1.division())

#4. Write a Python program to create a class that represents a shape. Include methods to 
# calculate its area and perimeter. Implement subclasses for different shapes like Circle, 
# Triangle, and Square.

class Shape:
    def __init__(self, side):
        self.side=side

    def area(self):
        return f"Tomoni {self.side} ga teng  shaklning yuzi "
    
    def perimeter(self):
        return f"Tomoni {self.side} ga teng shaklning perimetri "

from math import pi
class Circle:
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        natija=int(pi*(self.radius**2))
        return f"Radiusi {self.radius} ga teng bulgan doira yuzasi {natija} ga teng"
    
    def primeter(self):
        natija=2*pi*(self.radius)
        return f"Radiusi {self.radius} ga teng bulgan doira uzunligi {natija} ga teng "
    
class Square:
    def __init__(self, side):
        self.side=side

    def area(self):
        return f"Tomoni {self.side} bulgan kvadrat yuzi {(self.side)**2} ga teng"
    
#5. Write a Python program to create a class representing a binary search tree. Include methods 
# for inserting and searching for elements in the binary tree.

#6.Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items=[]  # ruyhat yaratamiz elementlarni saqlash uchun

    def push(self, item):
        self.items.append(item) 
        print(f"Stackga {item} qo'yildi") # ruyhatga element qoshish
    
    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"Stackdan {removed} elementi o'chirildi")
            return removed
        else:
            print("Stack bo'sh! Undan element o'chirib bulmaydi")
            return None
        
    def is_empty(self):
        return len(self.items)==0

stack1=Stack()
print(stack1.push(10)) 
stack1.push(20)
stack1.pop(10)
   
#7.Write a Python program to create a class representing a linked list data structure. 
# Include methods for displaying linked list data, inserting, and deleting nodes.

#Har bir tugunni ifodalovchi class yaratamiz
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
    
#endi LinkedList tuzilmasini yaratish uchun class
# 
class LinkedList:
    def __init__(self):
        self.head=None

    
    def append(self, value):
        new_node=Node(value)
        if self.head is None:   #Agar ruyhat bosh bolsa
            self.head=new_node
            return
        current=self.head      #Agar ruyhat bosh bolmasa 
        while current.next:   #Ruyhatni oxirigacha boramiz
            current=current.next
        current.next=new_node

    #Ruyhatning ichidagi elementlarni ko'rish uchun
    def display(self):
        current=self.head
        while current:
            print(current.value, end=' -> ')
            current=current.next
        print("None")

ll=LinkedList()
ll.append(5)
ll.append(10)
ll.append(20)
ll.display()

#8.Write a Python program to create a class representing a shopping cart.
#  Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add(self, name, price, quantity):
        self.items.append({'name':name, 'price':price, 'quantity':quantity})
    
    def remove_item(self, name):
        self.items=[item for item in self.items if item['name']!=name]

    def total(self):
        return sum(item['price']*item['quantity'] for item in self.items)

    def display_card(self):
        if not self.items:
            print("Savat bo'sh")
            return
        for item in self.items:
            print(f"{item['name']} mahsulotdan - {item['price']} so'm- {item['quantity']} dona")
        print("Umumiy ", self.total(), "so'm")

cart1=ShoppingCart()
cart1.add('Sut', 5000, 4)
cart1.display_card()

#9. Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing, popping, and displaying elements.
class StackDataStructure:
    def __init__(self):
        self.items=[]
    
    def pushing(self, item):
        self.items.append(item)
        return f"Stackga {item} qo'yildi"
    
    def popping(self, item):
        if not self.is_empty():
            self.items.pop(item)
            removed=f"Stackdan {item} o'chirildi" 
            return removed
        else:
            print("Stack bo'sh! Undan element o'chirishning imkoni yo'q")
    
    def display_item(self):
        for item in self.items:
            print(item)
            return
        
    def is_empty(self):
        return len(self.items)==0
stack1=StackDataStructure()
print(stack1.pushing('banana'))
print(stack1.pushing('apple'))
print(stack1.pushing('pineapple'))
stack1.display_item()

#10.Write a Python program to create a class representing a queue data structure. 
# Include methods for enqueueing and dequeueing elements.
class QueueDataStructure:
    def __init__(self):
        self.items=[]

    def enqueueing(self, item):
        self.items.append(item)
        return f"Ruyhatga {item} qo'shildi"
    
    def dequeueing(self, item):
        if not self.is_empty:
            self.items.pop(0)
            return 
        else:
            print("Ruyhat bo'sh! Undan element o'chirishning iloji yo'q")
            return
        
    def is_empty(self):
        return len(self.items)==0  
   
#11.Write a Python program to create a class representing a bank.
#  Include methods for managing customer accounts and transactions.
class Bank:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} so‘m hisobga qo‘shildi. Yangi balans: {self.balance} so‘m.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Hisobda yetarli mablag‘ yo‘q.")
        else:
            self.balance -= amount
            print(f"{amount} so‘m yechildi. Qolgan balans: {self.balance} so‘m.")

    def check_balance(self):
        print(f"Hisobingizda: {self.balance} so‘m mavjud.")

    def transfer(self, amount, other_account):
        if amount > self.balance:
            print("O‘tkazma amalga oshmadi. Yetarli mablag‘ yo‘q.")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"{amount} so‘m {other_account.name} ga o‘tkazildi.")

    def get_account_info(self):
        print(f"Mijoz: {self.name}")
        print(f"Hisob raqami: {self.account_number}")
        print(f"Balans: {self.balance} so‘m")

