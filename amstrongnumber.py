i=int(input('enter your number'))
a=i
sum=0
while i>0:
	sum=sum+(i%10)(i%10)(i%10)
	i=i//10
if a==sum:
	print(a,'armstrong number')
else:
	print(a,'not armstrong number')


#Armstrong number