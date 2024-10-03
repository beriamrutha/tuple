'''
Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''
def count_x(tuples, x):
    return tuples.count(x)

tuples = list(map(int, input("Enter tuple elements separated by space: ").split()))
x = int(input("Enter the value to count: "))
result = count_x(tuples, x)
print("The value {} is present {} times in the tuple.".format(x, result))
