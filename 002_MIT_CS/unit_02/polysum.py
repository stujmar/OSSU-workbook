# Polysum Grader

# A regular polygon has n number of sides. Each side has length s.
#
# The area of a regular polygon is: (0.25*n*s^2)/tan(pi/n)
# The perimeter of a polygon is: length of the boundary of the polygon

def polysum(n, s):
    """
    n: number of sides
    s: length of each side
    """
    import math
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    perimeter = n*s
    return round(area + perimeter**2, 4)