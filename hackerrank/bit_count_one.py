def count_one(n):
    # count the number of ones in the binary representation of
    # the given number
    count = 0
    while(n):
        print n
        print bin(n)
        print bin(n-1)
        n = n&(n-1) # remove last set bit A&(A-1)
        count+=1
    return count 

print count_one(100)