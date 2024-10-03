'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''
def get_tuples(n):
    tuples = []
    for i in range(n):
        user_input = input("Enter tuple element {}: ".format(i+1))
        tuples.append(int(user_input))
    return tuples

def max_tuples(tuples):
    return max(tuples)

n = int(input("Enter the number of tuple elements: "))
tuples = get_tuples(n)
result = max_tuples(tuples)
print("The maximum value of the tuple elements is: {}".format(result))
