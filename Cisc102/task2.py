def solution(A):
    # start with zero for xor math
    result = 0
    # loop through every number in the array
    for x in A:
        # xor each number to cancel out pairs and leave the odd one out
        result ^= x
    # return the final unpaired number
    return result