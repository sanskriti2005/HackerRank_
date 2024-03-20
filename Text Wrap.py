# QUESTION: https://www.hackerrank.com/challenges/text-wrap/problem
#SOLUTION:
import textwrap

def wrap(string, max_width): 
    wrap = textwrap.fill(string, max_width)
    
    return wrap

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)