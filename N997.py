"""
In a town, there are N people labelled from 1 to N.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing
that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

Note:
1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
"""


def findJudge1(N, trust):
    if N == 1 and not trust:
        return 1
    elif N == 2 and len(trust) == 1:
        return trust[0][1]
    temp = list(zip(*trust))
    pre = list(set(temp[1]) - set(temp[0]))
    if len(pre) != 1:
        return -1
    for i in range(1, N):
        if i not in pre:
            if [i, pre[0]] not in trust:
                return -1
    return pre[0]


def findJudge2(N, trust):
    l = [i[0] for i in trust]
    pre = list(filter(lambda x: x not in l, list(range(1, N + 1))))
    if len(pre) != 1:
        return -1
    for i in range(1, N):
        if [i, pre[0]] not in trust and i != pre[0]:
            return -1
    return pre[0]


def findJudge3(N, trust):  # not finished
    # indim = [ 0 for _ in range(len(trust))]
    outdim = [ N for _ in range(N)]
    for i in trust:
    #     indim[i[0]] += 1
        outdim[i[1]] -= 1
    for i in range(1, N+1):
        if outdim[i] == 1:
            pre = i
    for i in range(1, N):
        if [i, pre] not in trust and i != pre:
            return -1
    return pre



n = 3
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
trust2=[[1,3],[2,3]]

print(findJudge1(n, trust))
print(findJudge3(2, trust2))
