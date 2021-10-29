# find the slope of a line

# rise over run
def find_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "undefined"
    else:
        return (y2 - y1) / (x2 - x1)

print(find_slope(3, -5, 1, -1))

# find the incercept of two lines
# interesting I don't know how this works
def find_incercept(x1, y1, x2, y2):
    if x1 == x2:
        return "undefined"
    else:
        return y1 - (find_slope(x1, y1, x2, y2) * x1)


    