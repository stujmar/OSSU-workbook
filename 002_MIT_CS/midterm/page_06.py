def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here
    if len(t) == 1:
        return t[0]
    else:
        return max(t[0], max_val(t[1:]))

# or

    def openItem(term):
        newList = []

        for item in term:
           if type(item) == int:
              newList.append(item)

           else:
              newList += openItem(item)

        return newList

    sortingList = openItem(t)

    maximum = sortingList[0]

    for item in sortingList:
        if maximum < item:
            maximum = item

    return maximum
