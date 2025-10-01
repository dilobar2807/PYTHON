#1. 1. is_prime(n) funksiyasi

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(is_prime(23))

#2. digit_sum(k) funksiyasi

def digit_sum(k):
    k=abs(int(k))
    summa=0
    for i in str(k):
        summa+=int(i)
    return summa

print(digit_sum(1234))

# 3. Ikki sonning darajalari

def daraja(n):
    i=1
    while  2**i<n:
        print(2**i)
        i+=1
daraja(17)

