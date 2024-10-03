'''
Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
def count_x(tuples, x):
    return tuples.count(x)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

tuples = list(map(int, input("Enter tuple elements separated by space: ").split()))
x = int(input("Enter the value to count: "))
count = count_x(tuples, x)
result = factorial(count)
print("The value {} is present {} times in the tuple. Its factorial value is: {}".format(x, count, result))
