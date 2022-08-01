"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""
# from typing import List
import time

class Solution:
    
    def longestCommonPrefix(self, strs):
        prefix=[]
        num = len(strs)
        for i in zip(*strs):
            # print(i, type(x))
            print("-----")
            if len(set(i)) == 1:
                prefix.append(i[0])
            else:
                break
        return "".join(prefix)

    def longestCommonPrefix_listcomp(self, strs):
        prefix=[]
        prefix=[i[0] for i in zip(*strs) if len(set(i)) == 1]
        return "".join(prefix)
        #list comp solution doesn't seem suitable since list comps can't use break or continue
        #list comps are better performance when you want a list returned
        #list comps shouldn't be used when you want to do anything other than building a list like using break/continue
    
strs = ["flower","flow","flight", "fligp","flipp", "flipper", "flash"]
sol1=Solution()

start1=time.time()
print(sol1.longestCommonPrefix(strs=strs))
end1=time.time()
runtime1= end1-start1

start2=time.time()
print(sol1.longestCommonPrefix_listcomp(strs=strs))
end2=time.time()

runtime2=end2-start2

print(runtime1, "vs.", runtime2)
print(runtime1 < runtime2)
