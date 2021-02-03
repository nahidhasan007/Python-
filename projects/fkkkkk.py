x=int(input())
sum=0
for i in range(1,x+1,1):
	if x%i==0:
		sum=sum+i
print(sum)		
if sum==x:
	print("%i eh perfeito"%x)
else:
	print("%i nao eh perfeito"%x)