def min_operation(X, Y, m , n):
    if m==0:
        return n
    
    if n==0:
        return m
    
    if X[m-1] == Y[n-1]:
        return min_operation(X, Y, m-1, n-1)

    return 1 + min(min_operation(X, Y, m, n-1), min_operation(X, Y, m-1, n), min_operation(X, Y, m-1, n-1))


'''
logic :

If the characters are the same, we don't need to do any operation. We just move to the next character in both strings.
If the characters are different, we consider three possible operations:
1> insert       2> remove    3> replace
If one string is longer than the other after we've compared all characters, the remaining characters need to be either inserted or deleted, depending on which string is longer.
'''


x = "abcd"
y = "adcb"
print(min_operation(x, y, len(x), len(y)))