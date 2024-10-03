'''
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''
def sum_tuples(tuples):
    total = 0
    for num in tuples:
        total += num
    return total

tuples = list(map(int, input("Enter tuple elements separated by space: ").split()))
result = sum_tuples(tuples)
print("The sum of the tuple elements is: {}".format(result))
