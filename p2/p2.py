
odd = 1
even = 2
s=0
while even <= 4000000:
    s+=even
    odd = 2*even + odd
    even = 2*odd - even   
        
print("sum", s)