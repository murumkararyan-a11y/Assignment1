def solution(A):
    # get the total sum of all elements in the array
    totalsum = sum(A)
    # keep track of the left side sum
    leftsum = 0
    # start with infinity so the first difference is always smaller
    mindiff = float('inf')
    
    # loop through each possible split point
    for i in range(len(A) - 1):
        # add current element to the left sum
        leftsum += A[i]
        # the rest is the right side sum
        rightsum = totalsum - leftsum
        # find the absolute difference between left and right
        diff = abs(leftsum - rightsum)
        
        # update the minimum difference if we found a smaller one
        if diff < mindiff:
            mindiff = diff
            
    # return the smallest difference we found
    return mindiff