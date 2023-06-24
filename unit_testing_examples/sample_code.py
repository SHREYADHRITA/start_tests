"Given an array arr[] and an integer K where K is smaller than size of array,"
"the task is to find the Kth smallest element in the given array."
"It is given that all array elements are distinct."


class Solution:
    def kthSmallest(arr, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        n = len(arr)
        for i in range(0, n - 1):
            for j in range(0, n - 1 - i):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

        return arr[k - 1]
