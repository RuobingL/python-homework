import math
class Solution:
    """
    @param: a: parameter of the equation
    @param: b: parameter of the equation
    @param: c: parameter of the equation
    @return: a double array, contains at most two root
    """
    def rootOfEquation(self, a, b, c):
        delta_sqrt = b * b - 4 * a * c
        if delta_sqrt < 0:
            return []
        elif delta_sqrt == 0:
            return [-b / (2.0 * a)]
        else:
            delta = math.sqrt(delta_sqrt)
            return sorted([(-b - delta) / (2.0 * a), (-b + delta) / (2.0 * a)])