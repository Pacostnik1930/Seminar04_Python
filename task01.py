# Найти порследовательности числа фибоначчи

def fib(n):
    if n in (0,1):
        return 1
    return fib(n-1)+fib(n-2)  
print('Введите число:')      
n = int(input())
print(fib(n-2))
