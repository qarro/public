class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])+1
            #j为nums2中的i+1位置
            while(j<len(nums2)):
                if (nums1[i]>nums2[j]):
                    j = j+1
                else:
                    break
            if j == len(nums2):
                result.append(-1)
            else:
                result.append(nums2[j])
        return result