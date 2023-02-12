
def fib(n):
    if n in (0,1):
        return 1
    return fib(n-1)+fib(n-2)    
n = int(input())
print(fib(n))
# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))    
# print(list_1)    