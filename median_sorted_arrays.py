#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#Example 1:
#nums1 = [1, 3]
#nums2 = [2]
#The median is 2.0
#Example 2:
#nums1 = [1, 2]
#nums2 = [3, 4]
#The median is (2 + 3)/2 = 2.5

"""
Algorithm:

1) Calculate the medians m1 and m2 of the input arrays ar1[]
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)
3) If m1 is greater than m2, then median is present in one
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
Example:

   ar1[] = {1, 12, 15, 26, 38}
   ar2[] = {2, 13, 17, 30, 45}
For above two arrays m1 = 15 and m2 = 17

For the above ar1[] and ar2[], m1 is smaller than m2. So median is present in one of the following two subarrays.

   [15, 26, 38] and [2, 13, 17]
Let us repeat the process for above two subarrays:

    m1 = 26 m2 = 13.
m1 is greater than m2. So the subarrays become

  [15, 26] and [13, 17]
Now size is 2, so median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
                       = (max(15, 13) + min(26, 17))/2
                       = (15 + 17)/2
                       = 16
"""

class Solution:
    def find_median_of_array(self,array,start,end):
        if array==None or array==[]:
            return
        median=0
        total_length=end-start+1
        if total_length%2==1:
            #there are odd number of elements
            #median is the middle element
            median_index=start+((end-start)//2) # 1 2 3 4 5 6 start=1 end=5 end-start=4/2=2
            median=array[median_index]
            print("odd array"+str(array[start:end+1])+", median=%d"%(median))
        else:
            #there are even number of elements
            #median is the average of the two middle elements
            # 1 2 3 4 5 6 start=1 end=4
            median_index=start+int((end-start)//2)
            median=(array[median_index]+array[median_index+1])/2
            print("median_index=%d"%(median_index)+" even array"+str(array[start:end+1])+",median=%d"%(median))

        return median
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median=-1
        if nums1 == None or nums2 == None:
            return median
        #declare the start and end range
        median1_start=0
        median1_end=len(nums1)-1
        median2_start=0
        median2_end=len(nums2)-1
        while (median1_end-median1_start)+1>2 and (median2_end-median2_start+1)>2:
            #compute median of the arrays
            median1=self.find_median_of_array(nums1,median1_start,median1_end)
            median2=self.find_median_of_array(nums2,median2_start,median2_end)
            if median1==median2:
                #found the median
                return median1
            elif median1 > median2:
                #the median is somewhere in between 0 and len(nums1)//2
                #and the median is somewhere in betweeen len(nums2)//2 and len(nums2)
                #keep doing this until there are 2 elements in nums1 and 2 elements in nums2
                median1_end=(len(nums1)-1)//2
                median2_start=(len(nums2)-1)//2
            elif median1 < median2:
                # the median is somewhere in between 0 and len(nums2)//2
                # and the median is somewhere in betweeen len(nums1)//2 and len(nums1)
                # keep doing this until there are 2 elements in nums1 and 2 elements in nums2
                median1_start=(len(nums1)-1)//2
                median2_end=(len(nums2)-1)//2
        #Now that you have four elements left to search
        print(nums1[median1_start:median1_end+1])
        print(nums2[median2_start:median2_end+1])
        median=(max(nums1[median1_start],nums2[median2_start])+ min(nums1[median1_end],nums2[median2_end]))/2

        return median

array1=[1,3,5,7,9]
array2=[2,4,6,8,10]
sol=Solution()
median=sol.findMedianSortedArrays(array1,array2)
print("median=%.2f"%(median))
