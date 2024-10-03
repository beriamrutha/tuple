'''
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
'''
def get_tuples(n):
    tuples = []
    for i in range(n):
        user_input = input("Enter tuple element {}: ".format(i+1))
        tuples.append(int(user_input))
    return tuples

def sum_tuples(tuples):
    return sum(tuples)

n = int(input("Enter the number of tuple elements: "))
tuples = get_tuples(n)
result = sum_tuples(tuples)
print("The sum of the tuple elements is: {}".format(result))
