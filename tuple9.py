'''
Raju is a 3rd grade kid, he is struggling to find which is "even" number and which is a "odd" number. So, his teacher gave him a task to find how many even numbers and how many odd numbers are there in the given collection of values and print "Even" if even count is more than odd count, else print "Odd", if odd count is more and print "Equal" if both even count and odd count are same. Help Raju to understand the difference of even and odd.
Sample Input:
1 2 3 4 5
Sample Output:
Odd
'''
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count > odd_count:
        return "Even"
    elif odd_count > even_count:
        return "Odd"
    else:
        return "Equal"

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = count_even_odd(numbers)
print("Result: {}".format(result))
