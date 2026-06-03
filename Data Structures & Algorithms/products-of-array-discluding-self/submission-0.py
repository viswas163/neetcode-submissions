class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardProds = [1 for i in range(len(nums))]
        reverseProds = [1 for i in range(len(nums))]
        trailingProd = 1
        prevNum = 1

        for i, num in enumerate(nums):
            forwardProds[i] = trailingProd * prevNum
            trailingProd = forwardProds[i]
            prevNum = num

        trailingProd = 1
        prevNum = 1
        for i, num in enumerate(reversed(nums)):
            fwdIndex = len(nums) - i - 1
            reverseProds[fwdIndex] = trailingProd * prevNum
            trailingProd = reverseProds[fwdIndex]
            prevNum = num
        
        products = [1 for i in range(len(nums))]
        for i in range(len(forwardProds)):
            products[i] = forwardProds[i] * reverseProds[i]

        return products