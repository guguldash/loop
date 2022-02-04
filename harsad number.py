a=int(input("num"))
b=a
sum=0
while b!=0:
	c=b%10
	sum=sum+c
	b=b//10
if a%sum==0:
	print("harshad num")
else:
	print("not harshad num")