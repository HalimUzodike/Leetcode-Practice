# Alto Pharmacy Interview Questions

"""
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
It is often used in algorithm examples, and is defined by the following formula: F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1.

Your task is to implement the Fibonacci algorithm in three different methods: 1. Recursively 2. Iteratively 3. Using Memoization

Example 1:

Input:

n = 5

Output:

fibonacci(n) -> 5

Example 2:

Input:

n = 10

Output:

fibonacci(n) -> 55

The Fibonacci sequence starts as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

"""

def fibonacci_recursive(n):
    """
    Time    : O(2^n)
    Space   : O(n)
    """
    if n<=1: return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_memoization(n, memo={}):
    """
    Time    : O(n)
    Space   : O(n)
    """
    if n in memo: return memo[n]
    if n<=1:
        memo[n] = n
        return n
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

def fibonacci_iterative(n):
    """
    Time    : O(n)
    Space   : O(1)
    """
    if n<=1: return n
    f0, f1 = 0, 1
    res = 1
    for i in range(2, n+1):
        res=(f0 + f1)
        f0 = f1
        f1 = res
    return res

def fib(n):
    """
    Time    : O(logn)
    Space   : O(1)
    """
    golden_ratio = (1 + (5 ** 0.5)) / 2
    return int(round((golden_ratio ** n) / (5 ** 0.5)))



"""
Flatten N-Dimensional Array to 1D Array

You are given an N-dimensional array (a nested list) and your task is to convert it into a 1D array.
The N-dimensional array can have any number of nested lists and each nested list can contain any number of elements.
The elements in the nested lists are integers. Write a function that takes an N-dimensional array as input and returns a 1D array.

Example 1:

Input:

array = [1, [2, 3], [4, [5, 6]], 7]

Output:

flatten_array(array) -> [1, 2, 3, 4, 5, 6, 7]

Example 2:

Input:

array = [[1, 2], [3, 4], [5, 6]]

Output:

flatten_array(array) -> [1, 2, 3, 4, 5, 6]

Can potentially use isinstance() to check if element is a list
"""

def flatten_array(array):
    """
    Time    : O(n)
    Space   : O(n)
    """
    res = []
    for i in array:
        if type(i) == list:
            res.extend(flatten_array(i))
        else:
            res.append(i)
    return res


# Testing functions

array = [1, [2, 3], [4, [5, 6]], 7]
# array = [[1, 2], [3, 4], [5, 6]]
print(flatten_array(array))


"""
Triplet Counting

Imagine you have been given an array of integers, and a query number k.
Your task is to write a function that finds all the triplets in the array that sum up to the query number k.

Let’s illustrate this with some examples:

Example 1:

Input:

nums = [1, 2, 3, 4, 5]
k = 6

Output:

count_triplets(nums, k) -> 1

In this case, there is only one triplet that sums up to 6: (1, 2, 3).

Example 2:

Input:

nums = [10, 10, 20, 30, 40]
k = 60

Output:

count_triplets(nums, k) -> 3

In this case, there are three triplets that sum up to 60: (10, 10, 40), (10, 20, 30), and (10, 20, 30).
The value 10 can be retrieved as nums[0] or nums[1], therefore resulting in two triplets with the same value.

"""

from itertools import combinations
def count_triplets(nums, k):
    comb = combinations(nums, 3)
    # print(list(comb)) # [(10, 10, 20), (10, 10, 30), (10, 10, 40), (10, 20, 30), (10, 20, 40), (10, 30, 40), (10, 20, 30), (10, 20, 40), (10, 30, 40), (20, 30, 40)]
    main_list = []
    for element in list(comb):
        if sum(element) == k:
            main_list.append(element)
    return len(main_list)

# Testing functions

# nums = [1, 2, 3, 4, 5]
# k = 6

nums = [10, 10, 20, 30, 40]
k = 60
print(count_triplets(nums, k))



"""
Given an array of words and a search term, write a search algorithm to sort them appropriately.
"""

def search_and_sort(words, search_term):
    def calculate_score(word):
        word = word.lower()
        search = search_term.lower()

        # Exact match
        if word == search:
            return 100

        # Starts with search term
        if word.startswith(search):
            return 75

        # Contains search term
        if search in word:
            return 50

        # Calculate Levenshtein distance
        distance = levenshtein_distance(word, search)
        max_length = max(len(word), len(search))
        similarity = 1 - (distance / max_length)

        return similarity * 25

    def levenshtein_distance(s1, s2):
        if len(s1) < len(s2):
            return levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    # Sort the words based on their scores
    sorted_words = sorted(words, key=lambda word: calculate_score(word), reverse=True)

    return sorted_words

# Example usage
words = ["apple", "application", "apartment", "appendix", "banana", "app", "apply"]
search_term = "app"
result = search_and_sort(words, search_term)
print(result) # ['app', 'apple', 'apply', 'application', 'apartment', 'appendix', 'banana']