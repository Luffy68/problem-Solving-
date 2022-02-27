x = int(input(" "))
y = int(input(" "))

z = 0
for i in range(x, y):
	if i % 2 == 0:
		z += i
	else:
		pass
print(z)