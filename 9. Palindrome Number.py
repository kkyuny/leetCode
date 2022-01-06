class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        
        results = []
        while x >= 1:
            results.append(x%10)
            x /= 10
            x = int(x)            
        
        answer = 0
        for result in range(0, len(results)//2):
            if results[result] == results[len(results)-result-1]:
                answer += 1
            else:
                answer = 0
    
        if answer == len(results)//2:
            return True
        else:
            return False
            
# Runtime: 76 ms, faster than 33.08% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14 MB, less than 92.49% of Python3 online submissions for Palindrome Number.
