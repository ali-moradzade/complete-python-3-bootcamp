# one.py

def func():
	print("FUNC() in one.py")


print("TOP LEVEL in one.py")

if __name__ == '__main__':
	print('one.py is being run directory!')
else:
	print('one.py has been imported!')
