def change(x):
    if x == 0:
        return ''
    n = int(input())    
    return change(x - 1) + f' {n}'    




n = int(input('Введите сколько чисел в последовательности:'))
print(change(n))