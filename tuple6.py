'''
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
'''
def get_tuples(n):
    tuples = []
    for i in range(n):
        user_input = input("Enter tuple element {}: ".format(i+1))
        tuples.append(int(user_input))
    return tuples

def min_tuples(tuples):
    return min(tuples)

n = int(input("Enter the number of tuple elements: "))
tuples = get_tuples(n)
result = min_tuples(tuples)
print("The minimum value of the tuple elements is: {}".format(result))
