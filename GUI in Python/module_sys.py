import sys

def tong ( a, b = 10):
	print(a+b)
print(sys.argv)
if len(sys.argv) > 1:
	for i in sys.argv[1:]:
		tong(int(i))
				