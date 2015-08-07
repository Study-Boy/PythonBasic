#10! + 9! + ... + 2!

def sumall(N):
	y = 1
	i = N
	while i>=2:
		x = 1
		j = i
		while j >= 2:
			x = x*j
			j = j - 1
		y = y+x
		i = i - 1
	return y

#for i in range(5):
#	print(i)

ss = sumall(3)
print(ss)
ss = sumall(4)
print(ss)
ss = sumall(5)
print(ss)