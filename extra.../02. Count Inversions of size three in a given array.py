"""

problem link : https://www.geeksforgeeks.org/count-inversions-of-size-three-in-a-give-array/

Count Inversions of size three in a given array
Given an array arr[] of size n. Three elements arr[i], arr[j] and arr[k] form an inversion of size 3 if a[i] > a[j] >a[k] and i < j < k. Find total number of inversions of size 3.

Example :

Input:  {8, 4, 2, 1}
Output: 4
The four inversions are (8,4,2), (8,4,1), (4,2,1) and (8,2,1).

Input:  {9, 6, 4, 5, 8}
Output:  2
The two inversions are {9, 6, 4} and {9, 6, 5}
We have already discussed inversion count of size two by merge sort, Self Balancing BST and BIT.


"""

from typing import List


# sol 1) Time Complexity : O(n**2)

def solution(arr: List[int], n: int):
    # initialize result
    cnt = 0

    for i in range(1, n - 1):

        # Count all smaller elements
        # on right of arr[i]
        small = 0
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                small += 1

        # Count all greater elements
        # on left of arr[i]
        great = 0
        for j in range(i - 1, -1, -1):
            if arr[i] < arr[j]:
                great += 1

        cnt += great * small

    return cnt


if __name__ == "__main__":
    arr = [8, 4, 2, 1]
    n = len(arr)
    print(solution(arr, n))
