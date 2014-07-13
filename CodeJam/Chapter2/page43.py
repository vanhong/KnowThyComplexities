import pdb
import math
def fun():
	value_list = [1, 5, 10, 50, 100, 500]
	coin_input = raw_input("please input coins number:").split()
	coin_list = [int(i) for i in coin_input]
	if len(value_list) != len(coin_list):
		print "input wrong coins number"
		return 0
	A = input("please input the dollar:")
	n = 0
	for i in range(len(value_list)-1, -1, -1):
		t = min(coin_list[i], A / value_list[i])
		n = n + t
		A = A - t * value_list[i]
	print n
	return 0

fun()
