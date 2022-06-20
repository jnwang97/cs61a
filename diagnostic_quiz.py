def lens(prev=lambda x: 0):
    """
    A lens store is a store that associates keys with values.

    To create a lens store, call the function "lens", to get a "put" function.
    This function enables you to "put" a key-value pair into the store, and returns two functions
    "get" and another "put". The "get" function should let you look up a key and return its corresponding
    value, while the new "put" function should let you continue adding on to the existing store.

    Note that you can assume that every key provided is unique. If you try the get the value for a key
    that does not exist, return 0.

    >>> put1 = lens()
    >>> get2, put2 = put1('cat', 'animal')
    >>> get3, put3 = put2('table', 'furniture')
    >>> get4, put4 = put3('cup', 'utensil')
    >>> get5, put5 = put4('thesis', 'paper')
    >>> get5('cup')
    'utensil'
    >>> get5('table')
    'furniture'
    >>> get5('cat')
    'animal'
    >>> get3('cup')
    0
    """
    def put(k, v):
        def get(k2):
            if k2 == k:
                return v
            else:
                return prev(k2)
        return get, lens(get)
    return put


def store(helium, fn_even, fn_odd):
    """
    Write a function 'storeroom' that takes in a positive integer 'helium' and two
    functions 'fn_even' and 'fn_odd'

    It applies 'fn_even' to all of the even digits in the integer and
    applies 'fn_odd' to all the odd digits in the integer. It then returns whether
    the result of the even values is greater than the result of odd values.
    You can guarantee that the number has at least one even and one odd digit.

    >>> store(1234, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 > 3 * 1
    True
    >>> store(11111111111112, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1 * 1 ... * 1
    True
    >>> store(11111111111112, lambda x,y: x+y, lambda x,y: x+y) # 2 < 1 + 1 ... + 1
    False
    >>> store(12, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1
    True
    >>> store(12345, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 < 1 * 3 * 5
    False
    >>> store(18383, lambda x,y: x-y, lambda x,y: x-y) # 8 - 8 > 3 - 3 - 1
    True
    """
    evens_defined, odds_defined = False, False
    evens, odds = None, None
    while helium > 0:
        last_digit, helium = helium % 10, helium // 10
        if last_digit % 2 == 0:
            if not evens_defined:
                evens = last_digit
                evens_defined = True
            else:
                evens = fn_even(evens, last_digit)
        else:
            if not odds_defined:
                odds = last_digit
                odds_defined = True
            else:
                odds = fn_odd(odds, last_digit)
    return evens > odds


def sculpture(ruler, k):
    """
    Given a number 'ruler', finds the largest number of length 'k' or fewer,
    composed of digits from 'ruler', in order.

    >>> sculpture(1234, 1)
    4
    >>> sculpture(32749, 2)
    79
    >>> sculpture(1917, 2)
    97
    >>> sculpture(32749, 18)
    32749
    """
    if k == 0 or ruler == 0:
        return 0
    a = ruler % 10 + sculpture(ruler // 10, k - 1) * 10
    b = sculpture(ruler // 10, k)
    return max(a, b)


def paths(m, n):
    """
    Returns the number of paths from one corner of an M by N grid to the
    opposite corner
    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)


def knapsack(n, k):
    """
    returns if the combination of the digits of n can equal k
    """
    if n < 10:
        return n == k
    else:
        a = knapsack(n // 10, k - n % 10)
        b = knapsack(n // 10, k)
        return a or b


def all_nums(k):
    """
    Print all binary numbers below k digits
    >>> all_nums(1)
    0
    1
    >>> all_nums(2)
    0
    1
    10
    11
    >>> all_nums(3)
    0
    1
    10
    11
    100
    101
    110
    111
    >>> all_nums(4)
    0
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
    1011
    1100
    1101
    1110
    1111
    """
    def helper(n, prefix):
        if n == 0:
            print(prefix)
        else:
            helper(n - 1, prefix * 10)
            helper(n - 1, prefix * 10 + 1)
    helper(k, 0)


def remove(n, digit):
    """
    Return all digits of non-negative N that are not DIGIT, for some non_negative digit less than 10
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    if n == 0:
        return 0
    else:
        if n % 10 == digit:
            return remove(n // 10, digit)
        else:
            return remove(n // 10, digit) * 10 + n % 10

