def solution(A, K):
    # just return if the array is empty
    if not A:
        return A
    
    # figure out the actual shifts needed if k is bigger than array length
    k = K % len(A)
    # slice and swap the ends to rotate it
    return A[-k:] + A[:-k]