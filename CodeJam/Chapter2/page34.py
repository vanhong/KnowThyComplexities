import pdb

def fun():
	global n
	n = input("n:")
	if n < 1 or n > 20:
		print "please input n between 1 to 20"
		return 0
	global a
	a = []
	for i in range(n):
		a.append(input())
	if len(a) != n:
		print "please input " + n + " numbers"
		return 0
	global k
	k = input("k:")
	if DFS(0, 0):
		print "Yes"
	else:
		print "No"
	return 0

def DFS(i, sum):
	global a, n, k
	# pdb.set_trace()
	if (i == n):
		return sum == k
	if (DFS(i + 1, sum)):
		return True
	if (DFS(i + 1, sum + a[i])):
		return True
	return False

fun()