n=int(input("enter"))
s=0
for i in range(1, n):
	if n%i==0:
		s=s+i
if s==n:
	print("perfect")
else:
	print("not")

#Perfect number