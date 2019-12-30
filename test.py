def Find_Common_Characters1(a):

    record = []
    a1_temp = list(a[1])
    for i in range(len(a[0])):
        if a[0][i] in a1_temp:
            record.append(a[0][i])
            a1_temp.remove(a[0][i])

    for each in a[2:]:
        each_list = list(each)
        for rec in record:
            if rec not in each_list:
                record.remove(rec)
            else:
                each_list.remove(rec)
    return record


def Find_Common_Characters2(a):
    ans ={}
    for each in a[0]:
        ans[each] = a[0].count(each)
    for each in a[1:]:


A1= ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
print(Find_Common_Characters2(A1))
