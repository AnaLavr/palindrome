def is_prime(num):
    b=0
    for i in range(2,num):  
        if num%i == 0:
            b += 1
    if b!=0:
        return('False')    
    else:
        return('True')
    


def primes_below(n,m):
    l=[]
    for i in range(n,m+1):
        if is_prime(i)=='True' and palindrome(i)=='True': 
            l.append(i)
    return(l)

def palindrome(n):
    if str(n)==str(n)[::-1]:
        return('True')
    else:
        return('False')
    
print(primes_below(10000,99999))