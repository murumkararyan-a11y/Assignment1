import math

def solution(X, Y, D):
    # divide the total distance by jump size and round up to get the min jumps
    return math.ceil((Y - X) / D)