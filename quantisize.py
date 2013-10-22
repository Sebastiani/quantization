from sys import argv
from math import pow


def quantisize(a,b, n):

	interval = (b-a)/pow(2,n)
	i = a
	aInterval= []
	while i <b :
		aInterval.append(str(i))
		i = i+ interval

	return ' '.join(aInterval)

def main(): 

	f =  open("anwser"+argv[3]+".txt", 'wb')
	f.write(quantisize(int(argv[1]), int(argv[2]), int(argv[3])))

if __name__ == '__main__':
	main()

