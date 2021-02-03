x1,y1=input().split()
x=int(x1)
y=int(y1)
if x<0 or y<0:
	if y<0 and x>=0:
		a=y*(-1)
		print("-%i %i"% (x/a,x%a))
	elif x<0 and y>0:
		ck = x
		i=0
		j=0
		while True:
			ans = y*i + j
			print(i,j)
			if ans==ck:
				print(i,j)
				break
			i = i-1
			j = j+1	
else:
	print(x/y,x%y)

		


		