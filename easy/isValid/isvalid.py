"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        punc_dict = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in punc_dict:
                if stack:
                    pop_element = stack.pop()
                else:
                    pop_element = "#"

                if punc_dict[i] != pop_element:
                    return False
            else:
                stack.append(i)
        return not stack

s = "[())]"
print(Solution().isValid(s))