def solution(A):
    # get the total length including the missing number
    n = len(A) + 1
    # use the math formula to find what the total sum should be
    expected = n * (n + 1) // 2
    # add up what is actually in the array right now
    actual = sum(A)
    # whatever is left over is our missing number
    return expected - actual