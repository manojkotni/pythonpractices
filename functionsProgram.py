#19 18 22 even or odd without function
'''num1 = 19
num2 = 18
num3 = 22
if num1%2==0:
	print('{} is even'.format(num1))
else:
	print('{} is odd'.format(num1))
if num2%2==0:
	print('{} is even'.format(num2))
else:
	print('{} is odd'.format(num2))
if num1%3==0:
	print('{} is even'.format(num3))
else:
	print('{} is odd'.format(num3))'''
    
#now with functions
'''def evenorodd(number):
    "this program is to check the given numbers are even or odd"
    if number%2==0:
        print('{} is even'.format(number))
    else:
        print('{} is odd'.format(number))
evenorodd(19)
evenorodd(18)
evenorodd(22)
print(evenorodd.__doc__)
'''
#return
def cubeOfNumber(number):
    cube = number*number*number
    return cube
result = cubeOfNumber(10)
print(result)
