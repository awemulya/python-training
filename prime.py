def primeCal(*args):
    prime_numbers = []
    for i in args:
        j = 2;
        flag = 1
        while j<i:
            if i%j==0:
                flag = 0
                break
            j +=1
        if flag == 1:
            prime_numbers.append(i)

    return prime_numbers
x = primeCal(1,2,3,4,5,6)
print('Primenumber are :')
print(x)
