n=int(input())
arr = list(map(int,input().split()))
low=arr[0]
pos = 0
for i in range(1,len(arr)):
	if low>arr[i]:
		low = arr[i]
		pos = i
print("Menor valor: %i"%low)
print("Posicao: %i"%pos)		