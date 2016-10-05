
from random import shuffle


a = ["python", "c", "c++"]

def random(a):
	shuffle(a)
	print a[0]


if __name__ == "__main__" :
	random(a)