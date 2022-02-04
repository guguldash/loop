num=int(input('enter any number'))
rev=0
i=num
while i>0:
	rev=(rev*10)+i%10
	i=i//10
if(num==rev):
	print('palindrom no')
else:
	print('not palindrom no')

#palindrom  number