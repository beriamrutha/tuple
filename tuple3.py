'''
Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''
def get_tuple_elements():
    """
    Get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
    """
    tup = tuple(map(int, input().split()))
    print(len(tup))
get_tuple_elements()
