b_number = [1, 0, 0, 1, 1, 0, 1, 1]
sum=0
for i in range(len(b_number)):
    decimal=b_number[i]*2**(len(b_number))-(i+1)
    sum=sum+decimal
print(sum) 
#mq6  