"""
    A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
    where A and B are valid parentheses strings, and + represents string concatenation. 
     For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

    A valid parentheses string S is primitive if it is nonempty,
    and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

    Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
    where P_i are primitive valid parentheses strings.
    Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

    Example 1:

    Input: "(()())(())"
    Output: "()()()"
    Explanation:
    The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
    After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
    Example 2:

    Input: "(()())(())(()(()))"
    Output: "()()()()(())"
    Explanation:
    The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
    After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
    Example 3:

    Input: "()()"
    Output: ""
    Explanation:
    The input string is "()()", with primitive decomposition "()" + "()".
    After removing outer parentheses of each part, this is "" + "" = "".
 
    Note:
    S.length <= 10000
    S[i] is "(" or ")"
    S is a valid parentheses string
"""


def removeOuterParentheses(s):
    if s[0] != '(':
        return -1
    primitive = []

    count = 0    # if count == 1 , '(' and future ')'should be removed
    for i in s:
        if i == '(':
            count += 1
            if count != 1:         # not the first '(' add to list
                primitive.append(i)
        elif i == ')' and count != 1:   # not the outer parentheses ')'
            primitive.append(i)
            count -= 1              # finished a pair of '( )'
        else:
            count -= 1              # count == 1, ')' should be removed
    return ''.join(primitive)



S1 = "(()())(())"           #out: ()()()
S2 = "(()())(())(()(()))"   #out: ()()()()(())
S3 = "()((()))"             #out: (())
S4 = "(()(()))()"           #out: ()(())
S5 = "()"
print('s1 =', removeOuterParentheses(S1))
print('s2 =', removeOuterParentheses(S2))
print('s3 =', removeOuterParentheses(S3))
print('s4 =', removeOuterParentheses(S4))
print('s5 =', removeOuterParentheses(S5))

