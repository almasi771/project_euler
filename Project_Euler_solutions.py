"""
Solutions to Project Eulers problems
"""

#P1: calcualtes the sum of all multiples of 3 or 5 below 1000
def problem_one():
	sum_of_multiples = sum([i for i in range(1000) if i%3 == 0 or i%5 == 0])

def fib(n):
	if n <= 1: return 1
	else: return fib(n-1) + fib(n-2)

#P2: calculates the sum of the even-valued numbers under the Fibonacci sequence whose values are less than 4M
def problem_two():
	x = sum([fib(i) for i in range(35) if fib(i)%2 == 0 and fib(i)<40*10**6])
	
if __name__ == '__main__':
	print problem_one();
	print problem_two(); 
