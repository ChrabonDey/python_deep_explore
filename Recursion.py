# 1 

mod=10**9+7

def power(x,n,mod):
    if n==0:
        return 1
    half=power(x,n//2,mod)
    result=(half*half)%mod
    if n%2==1:
        result=(result*x)%mod
    return result

def count_good_string(n):
    even_count = (n + 1) // 2
    odd_count = n // 2

    return (power(5, even_count, mod) *
            power(4, odd_count, mod)) % mod
    
    
print(count_good_string(1))


#2

from typing import List

class Solution:
    def generateParenthesis(self,n:int) -> List[str]:
        result=[]
        def backtrack(s='',open=0,close=0):
            if len(s)==2*n:
                result.append(s)
                return
            if open<n:
                backtrack(s+'(',open+1,close)
            if close<open:
                backtrack(s+')',open,close+1)
        backtrack()
        return result
    
    
#3

def sum_of_List(lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0]+sum_of_List(lst[1:])

sum_list=[1,2,3,4,5]
print(f"The sum of the list is: {sum_of_List(sum_list)}")   


#4

def reverse_string_with_recursion(s):
    if len(s)<=1:
        return s
    return reverse_string_with_recursion(s[1:]+s[0])    


#5
