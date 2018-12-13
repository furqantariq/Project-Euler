
import itertools

def is_palindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return temp==rev

print(max([(x1,x2,x1*x2) for (x1,x2) in itertools.product(range(999,0,-1),range(999,0,-1)) if is_palindrome(x1*x2) ],key=lambda x:x[2]))
    
