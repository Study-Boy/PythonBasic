
names = ['Machael','Bob','Tracy']
for name in names:
	print('hello,',name)

print('+++++++++++++')

for i in range(3):
	print('hello,%s!' % names[i])

print('+++++++++++++')

sum = 0
for i in range(100):
	sum += i
#	print (i)
print('sum  =  ',sum) #sum = 4950

print('+++++++++++++')

sum = 0
n = 0
while n <= 100:
	sum += n
	n += 1
print ('sum2 = %d' % sum) #sum2 = 5050
