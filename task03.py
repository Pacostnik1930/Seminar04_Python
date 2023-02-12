n = int(input())
def simple_number(n):
    flag = True
    for i in range(2,n):
        if n % i != 0:
           continue
        else :
            flag = False
            break
    return flag  
print(simple_number(n))        
