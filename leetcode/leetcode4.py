def findMedianSortedArrays(nums1, nums2) -> float:
        arr = list(sorted(nums1+nums2))
        if len(arr)%2==0:
            return (arr[len(arr)//2-1]+arr[len(arr)//2])/2
        elif len(arr)%2==1:
            return arr[len(arr)//2]

print(findMedianSortedArrays([1], [3]))