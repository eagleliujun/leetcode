"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

"""

def isIsomorphic1(s,t):  # overtime
    c = list(zip(s,t))
    for i, value1 in enumerate(c):
        for j, value2 in enumerate(s):
            if i != j and value1[0] ==value2:
                if value1[1] != t[j]:
                    return False
            elif i != j and value1[1] == t[j]:
                if value1[0] != value2:
                    return False
    return True

# def isIsomorphic2(s,t):    # a-->b  b--->c is false ,but this problem should be true
#     comp = {}
#     for i, value1 in enumerate(s):
#         if value1 not in comp:
#             if t[i] not in comp.values():
#                 comp.setdefault(value1, t[i])
#             elif comp[t[i]] != value1:
#                 return False
#         elif t[i] not in comp:
#             if comp[value1] != t[i]:
#                 return False
#     return True


def isIsomorphic2(s,t):
    comp1 = {}
    for i, value1 in enumerate(s):
        if comp1.setdefault(value1, t[i]) != t[i]:
            return False
    comp1.clear()
    for j, value2 in enumerate(t):
        if comp1.setdefault(value2, s[j]) != s[j]:
            return False
    return True

def isIsomorphic3(s,t):   # ref to the solution
    return [*map(s.index, s)] == [*map(t.index, t)]

def isIsomorphic32(s,t):
    k1 = list(map(s.index, s))
    k2 = [*map(t.index, t)]
    return k1==k2

def isIsomorphic4(s, t):
    d = {}
    for i, j in zip(s, t):
        if i in d:
            if d[i] != j:
                return False
        elif j not in d.values():
            d[i] = j
        else:
            return False
    return True

def isIsomorphic5(s, t):
    d = {}
    for i, j in zip(s, t):
        if i not in d:
            if j not in d.values():
                d[i] = j
            else:
                return False
        elif d[i] != j:
            return False
    return True

def isIsomorphic6(s, t):
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            if t[i] not in d.values():
                d[s[i]] = t[i]
            else:
                return False
        elif d[s[i]] != t[i]:
            return False
    return True

s1 = "aba"
t1 = "baa"  #false
s= 'ab'
t= 'ca'     # true
s2 = 'aba'
t2 = 'foo'   #false
s3 = 'ab'
s4 = 'aa'    #false
print(isIsomorphic6(s2, t2))