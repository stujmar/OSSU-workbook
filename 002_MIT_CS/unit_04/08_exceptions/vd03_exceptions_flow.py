# Using Exceptions to control flow.
# using the raise keyword.

# raise <exceptionName>(<arguments>)
# raise ValueError('Invalid value')

# No you can pick when and which exception to raise vs having python raise them.


def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i]
    """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except TypeError:
            raise TypeError('get_ratios called with bad types')
        except:
            raise Exception('get_ratios called with bad types')
    return ratios

L1 = [1, 2]
L2 = [1, 0]

# print(get_ratios(L1, L2))

test_data = [
    ['joe', [80, 75, 85]],
    ['jane', [75, 80, 90]],
    ['jill', [85, 95, 100]],
    ['jack', [100, 90, 95]],
    ['deadpool', []],
    ]

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grade data')
        return 0.0
    # finally:
    #     return "no average"

def get_stats(class_list):
    new_stats = []
    for student in class_list:
        print(student)
        new_stats.append([student[0], student[1], avg(student[1])])
    return new_stats

# print(get_stats([['joe', [80, 90, 95]], ['jane', [75, 80, 90]]]))
print(get_stats(test_data))