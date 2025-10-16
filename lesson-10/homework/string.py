from datetime import datetime

# ================================
# 1. Task klassi — bitta vazifani ifodalaydi
# ================================
class Task:
    def __init__(self, title, description, due_date, status="Bajarilmagan"):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")  # Sana formatini o'zgartiramiz
        self.status = status

    def mark_complete(self):
        """Vazifani bajarilgan deb belgilaydi."""
        self.status = "Bajarilgan"

    def is_incomplete(self):
        """Vazifa bajarilmaganligini tekshiradi."""
        return self.status != "Bajarilgan"

    def display(self, index):
        """Vazifa haqida ma'lumot chiqaradi."""
        due_date_str = self.due_date.strftime("%Y-%m-%d")
        print(f"{index}. 📌 {self.title} | 📝 {self.description} | 📅 {due_date_str} | 📊 {self.status}")


# ================================
# 2. ToDoList klassi — vazifalar ro'yxatini boshqaradi
# ================================
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Yangi vazifani ro'yxatga qo'shish."""
        self.tasks.append(task)
        print(f"✅ Vazifa qo‘shildi: {task.title}")

    def list_tasks(self):
        """Barcha vazifalarni ko‘rsatish."""
        if not self.tasks:
            print("📭 Vazifalar ro‘yxati bo‘sh.")
            return
        print("\n📋 Barcha vazifalar:")
        for i, task in enumerate(self.tasks, 1):
            task.display(i)
        print()

    def mark_complete(self, index):
        """Berilgan raqamdagi vazifani bajarilgan deb belgilash."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"✔️ Vazifa bajarildi: {self.tasks[index].title}")
        else:
            print("⚠️ Noto‘g‘ri raqam kiritildi!")

    def list_incomplete(self):
        """Faqat bajarilmagan vazifalarni ko‘rsatish."""
        incomplete_tasks = [t for t in self.tasks if t.is_incomplete()]
        if not incomplete_tasks:
            print("🎉 Bajarilmagan vazifalar yo‘q!")
            return
        print("\n⏳ Bajarilmagan vazifalar:")
        for i, task in enumerate(incomplete_tasks, 1):
            task.display(i)
        print()


# ================================
# 3. CLI — foydalanuvchi bilan muloqot
# ================================
def show_menu():
    print("""
📝 ToDo List — menyu:
1. Vazifa qo‘shish
2. Barcha vazifalarni ko‘rish
3. Vazifani bajarilgan deb belgilash
4. Faqat bajarilmagan vazifalarni ko‘rish
5. Chiqish
""")


# ================================
# 4. Asosiy dastur
# ================================
def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input("Tanlovingizni kiriting (1-5): ")

        if choice == "1":
            title = input("📌 Vazifa nomi: ")
            description = input("📝 Vazifa tavsifi: ")
            due_date = input("📅 Muddati (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)

        elif choice == "2":
            todo.list_tasks()

        elif choice == "3":
            todo.list_tasks()
            if not todo.tasks:
                continue
            try:
                index = int(input("Qaysi vazifa bajarildi (raqam): ")) - 1
                todo.mark_complete(index)
            except ValueError:
                print("⚠️ Raqam kiriting!")

        elif choice == "4":
            todo.list_incomplete()

        elif choice == "5":
            print("👋 Dastur tugatildi.")
            break

        else:
            print("⚠️ Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")


# ================================
# 5. Dastur ishga tushirish
# ================================
if __name__ == "__main__":
    main()

#TASK-2

class Post:
    def __init__(self, title, content, author):
        self.title=title
        self.content=content
        self.author=author
        self.created_at=datetime.now()        
    
    def display(self, index):
        """Bitta post haqida ma'lumot"""
        created_post=datetime.strftime(self.created_at, "%Y-%m-%d %H-%M")
        print(f"{index}.{self.title}, {created_post}, {self.author}")
        print(f"{self.content}")

class Blog:
    def __init__(self):
        self.posts=[]
    
    def add_post(self, title, content, author):
        """Yangi post qo'shish"""
        post=Post(title, content, author)
        self.posts.append(post)
        print(f"{post} Muvaffaqiyatli qo'shildi")

    def list_all_post(self):
        """Barcha postlarni ko'rish"""
        if not self.posts:
            print("Hali postlar mavjud emas")
            return
        for i, post in enumerate(self.posts, start=1):
            post.display(i)

    def list_by_author(self, author):
        """Muallif bo‘yicha postlarni ko‘rsatish"""
        found = False
        for i, post in enumerate(self.posts, start=1):
            if post.author.lower() == author.lower():
                post.display(i)
                found = True
        if not found:
            print(f"❌ '{author}' tomonidan yozilgan post topilmadi.")

    def delete_post(self, index):
        """Ruyhatdan postni o'chirish"""
        if 0<index<=len(self.posts):
            deleted=self.posts.pop(index-1)
            print(f"{deleted} post o'chirildi")
        else:
            print("Noto'g'ri index kiritilgan")

    def edit_post(self, index, new_title=None, new_content=None):
        """Postni tahrirlash"""
        post=self.posts[index-1]
        if 0<index<len(self.posts):
            if new_title:
                post.title=new_title
            if new_content:
                post.content=new_content
            print("Post muvaffaqqiyatli tahrirlandi")
        else:
            print("Mavjud bo'lmagan index kiritildi")
        
    def show_latest_posts(self, n=3):
        """Oxirgi 3 ta postni ko'rish"""
        if not self.posts:
            print("Ruyhatda post mavjud emas")
            return
        print(f"\n So'ngi {min(n, len(self.posts))} ta postni ko'rish")
        for i, post in enumerate(self.posts[-n:], start=1):
            post.display(i)

#3. CLI interfeys 
            

def show_menu():
    print("""
    Blog menu:
    1.Post qo'shish
    2.Barcha postlarni ko'rish
    3.Muallif buyicha postlarni ko'rish
    4.Postni o'chirish
    5.Ruyhatni o'zgartirish
    6.Oxirgi postlarni ko'rish
    7.chiqish
""")

def main():
    blog=Blog()
    while True:
        show_menu()
        choice=input("Tanlovingizni kiriting: (1-7)")
        if choice=='1':
            title=input("Post sarlavhasini kiriting: ")
            content=input("Post contentini kiriting: ")
            author=input("Post authorini kiriting: ")
            blog.add_post(title, content, author) 
        elif choice=='2':
            blog.list_all_post()
        elif choice=='3':
            author=input("Avtorni kiriting: ")
            blog.list_by_author()
        elif choice=='4':
            index=input("O'chirmoqchi bo'lgan post raqamini kiriting: ")
            blog.delete_post(index)
        elif choice=='5':
            index=input("Indexni kiriting: ")
            new_title=input("Yangi sarlavha kiriting: ")
            new_content=input("Yangi post matnini kiriting: ")
            blog.edit_post(index, new_title if new_title else None, new_content if new_content else None)

        elif choice=='6':
            blog.show_latest_posts()
        
        elif choice=='7':
            print("Dastur tugadi!")
            break
        else:
            ("Noto'g'ri! Qaytadan urinib ko'ring!")
if __name__ == "__main__":
    main()

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm hisobga qo'shildi. Yangi balans: {self.balance} so'm")
        else:
            print("Noto‘g‘ri summa kiritildi!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Qolgan balans: {self.balance} so'm")
        else:
            print("Hisobda yetarli mablag‘ yo‘q!")

    def display(self):
        print(f"Hisob raqami: {self.account_number}, Egasi: {self.holder_name}, Balans: {self.balance} so'm")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, holder_name, balance=0):
        if account_number in self.accounts:
            print("Bunday hisob allaqachon mavjud!")
        else:
            self.accounts[account_number] = Account(account_number, holder_name, balance)
            print("Hisob muvaffaqiyatli qo‘shildi!")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def check_balance(self, account_number):
        acc = self.get_account(account_number)
        if acc:
            print(f"Balans: {acc.balance} so'm")
        else:
            print("Hisob topilmadi!")

    def deposit(self, account_number, amount):
        acc = self.get_account(account_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Hisob topilmadi!")

    def withdraw(self, account_number, amount):
        acc = self.get_account(account_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Hisob topilmadi!")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"{amount} so'm {from_acc} dan {to_acc} ga yuborildi.")
            else:
                print("Yetarli mablag‘ yo‘q!")
        else:
            print("Hisob raqami topilmadi!")

    def display_all_accounts(self):
        if self.accounts:
            for acc in self.accounts.values():
                acc.display()
        else:
            print("Hech qanday hisob mavjud emas!")


# Asosiy dastur (CLI menyu)
def main():
    bank = Bank()

    while True:
        print("\n--- 🏦 BANK TIZIMI ---")
        print("1. Hisob qo‘shish")
        print("2. Balansni tekshirish")
        print("3. Pul qo‘yish")
        print("4. Pul yechish")
        print("5. Pul o‘tkazish")
        print("6. Hisoblarni ko‘rish")
        print("0. Chiqish")
        choice = input("Tanlovingizni kiriting: ")

        if choice == "1":
            acc_no = input("Hisob raqamini kiriting: ")
            name = input("Hisob egasining ismi: ")
            balance = float(input("Boshlang‘ich balans: "))
            bank.add_account(acc_no, name, balance)

        elif choice == "2":
            acc_no = input("Hisob raqamini kiriting: ")
            bank.check_balance(acc_no)

        elif choice == "3":
            acc_no = input("Hisob raqamini kiriting: ")
            amount = float(input("Qo‘yiladigan summa: "))
            bank.deposit(acc_no, amount)

        elif choice == "4":
            acc_no = input("Hisob raqamini kiriting: ")
            amount = float(input("Yechiladigan summa: "))
            bank.withdraw(acc_no, amount)

        elif choice == "5":
            from_acc = input("Jo‘natuvchi hisob raqami: ")
            to_acc = input("Qabul qiluvchi hisob raqami: ")
            amount = float(input("Summani kiriting: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == "6":
            bank.display_all_accounts()

        elif choice == "0":
            print("Tizimdan chiqildi. Rahmat!")
            break

        else:
            print("Noto‘g‘ri tanlov!")


if __name__ == "__main__":
    main()

