# Paste your function here
def applyF_filterG(L, f, g):
    my_list = []
    for item in L:
        if g(f(item)) == True:
            my_list.append(item)
    L[:] = my_list
    if len(L) == 0:
        return -1
    else:
        return max(L)