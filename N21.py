def mergeTwoLists(l1, l2):
    res = []
    for i in range(len(l1)):
        res.append(l1[i])
        res.append(l2[i])
    return res