def get_permutations(lst):
    if len(lst)==0:
        return []

    if len(lst)==1:
        return [lst]

    perms=[]
    for i in range(len(lst)):
        current = lst[i]
        rem_list = lst[:i] + lst[i+1:]
        rem_perm = get_permutations(rem_list)
        for p in rem_perm:
            perms.append([current]+p)
    return perms

data = [1,2,3]
for perm in get_permutations(data):
    print(perm)
