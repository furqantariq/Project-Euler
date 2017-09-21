
def sum_filter(size):
    return sum(filter(lambda x: (x%3==0 or x%5==0), range(1,size)))

def sum_math(size):
    n3 = int(size/3)
    n5 = int(size/5)
    n15 = int(size/15)
    sum3 =  (n3/2)*(2*3+(n3-1)*3)
    sum5 =  (n5/2)*(2*5+(n5-1)*5)
    sum15 =  (n15/2)*(2*15+(n15-1)*15)
    return int(sum3+sum5-sum15)

    
if __name__ == "__main__":
    print("Filtering over series ",sum_filter(1000))
    print("Math approach",sum_math(1000-1))
    