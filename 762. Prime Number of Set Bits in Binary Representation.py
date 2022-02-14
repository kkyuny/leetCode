import math

def prime(n):
    if n==1:
        return False

    for x in range(2, (int)(math.sqrt(n))+1):
        if n%x==0:
            return False
    return True

def make_base(n, base):
        q = n // base
        r = str(n % base)
    
        if q == 0:
            return r
        else:
            return make_base(q, base) + r

class Solution:     
    def countPrimeSetBits(self, left: int, right: int) -> int:        
        result = 0
        while left <= right:
            answer = 0
            x = str(make_base(left, 2))
            for i in x:
                if i == '1':
                    answer += 1           
            if(prime(answer)):
                result += 1
            left += 1
        return result
            
        
