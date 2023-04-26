def Pascal(n):
    if n == 1:
        return [1]
    else:
        prev = Pascal(n-1)
        return [1]+[prev[i]+prev[i+1] for i in range(len(prev)-1)]+[1]
    
print(Pascal(7))
    