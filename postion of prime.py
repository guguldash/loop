a=int(input('enter number'))
i=1
count=0
while count<a:
	j=1
	f=0
	while j<=i:
		if i%j==0:
			f=f+1
		j+=1
	if f==2:
		x=i
		count=count+1
	i=i+1
print(x)
#position of prime number