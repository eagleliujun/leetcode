"""




"""

def generate(n):
    i=1
    res = []
    if n == 0:
        return None
    temp = [1]
    res.append(temp)
    if n ==1:
        return res
    temp = [1,1]
    res.append(temp)
    if n == 2:
        return res
    while i < n:
        for j in range(i):
            temp.append(j)

        res.append(temp)
