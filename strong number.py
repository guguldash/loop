number=int(input('enter your number'))
sum=0
rem=0
t=number
while number>0:
	factor=1
	i=1
	reminder=number%10
	while i<=reminder:
		factor=factor*i
		i += 1
	sum=sum+factor
	number //= 10
if sum==t:
	print(t,'strong number')
else:
	print(t,'not a strong number')