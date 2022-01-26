#CS351 -- HW1
#Erin Saijan

def greatest_difference(nums1, nums2):
    result = 0
    for i in range(len(num1)):        
        abs_diff = abs(num1[i] - num2[i])        
        if result <= abs_diff:            
            result = abs_diff    
    return result

    """ (list of number, list of number) -> number
    
    Return the greatest absolute difference between numbers at corresponding
    positions in nums1 and nums2.
    
    Precondition: len(nums1) == len(nums2) and nums1 != []
    
    >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    >>> greatest_difference([1, -2, 3], [-6, 8, 10])
    10
    """


def can_pay_with_two_coins(denoms, amount):
    possible = True
    k = 1
    for i in range(4):
        for k in range(4):
            if denoms (i) + denoms(i+1) == amount:
                possible = True
    return possible

    """ (list of int, int) -> bool
    
    Return True if and only if it is possible to form amount, which is a 
    number of cents, using exactly two coins, which can be of any of the 
    denominations in denoms.
    
    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 20)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    False
    """
	
	
def all_fluffy(s):
    val = False
    fluffy = "fluyFLUY"
    for i in range(len(s)):
        val = False
        found = fluffy.find(s(i))
        if found == 1:
            val = False
            break
           
    return val
    """ (str) -> bool

    Return True iff every letter in s is fluffy. Fluffy letters are those that
    appear in the word 'fluffy'.
    
    >>> all_fluffy('fullfly')
    True
    >>> all_fluffy('firefly')
    False
    """


def digital_sum(nums_list):
    result = 0
    for i in range(len(nums_list)):
        for k in range(len(nums_list(i))):
            sum += nums_list(i)[k]
    return result
    """ (list of str) -> int
    
    Precondition: s.isdigit() holds for each string s in nums_list.
    
    Return the sum of all the digits in all strings in nums_list.
    
    >>> digital_sum(['64', '128', '256'])
    34
    >>> digital_sum(['12', '3'])
    6
    """
    


def count_collatz_steps(n):
    """ (int) -> int
    
    Return the number of steps it takes to reach 1, by applying the two steps
    of the Collatz conjecture beginning from n.

    >>> count_collatz_steps(6)
    8
    """

    
    
