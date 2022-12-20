def solve(A):
    vowel=['a','e','i','o','u']
    str=""
    for i in A:
        if i in vowel:
            str=str+i
    return str
A = 'interviewbit'
print(solve(A))