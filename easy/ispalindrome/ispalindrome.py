"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

    -231 <= x <= 231 - 1
"""



class Solution:
        
    def isPalindrome(self, x):
        origin_x = x
        rev = 0
        while x > 0:
            last_digit = x % 10
            rev = rev * 10 + last_digit
            x = x // 10
        
        if origin_x < 0:
            rev *= -1
        
        return rev == origin_x
    

print(Solution().isPalindrome(121))