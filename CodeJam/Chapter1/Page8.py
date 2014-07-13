def fun():
	n = input("n=")
	m = input("m=")
	k = []
	for i in range(n):
		k.append(input())
	b = False
	for i in range(n):
		for j in range(n):
			for p in range(n):
				for q in range(n):
					if (k[i] + k[j] + k[p] + k[q] == m):
						b = True
	if (b):
		print "Yes"
	else:
		print "No"
	return 0;

fun()
