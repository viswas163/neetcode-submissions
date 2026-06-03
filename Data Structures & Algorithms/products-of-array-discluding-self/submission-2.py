class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardProds = [1 for i in range(len(nums))]
        trailingProd = 1
        prevNum = 1

        for i, num in enumerate(nums):
            forwardProds[i] = trailingProd * prevNum
            trailingProd = forwardProds[i]
            prevNum = num

        trailingProd = 1
        prevNum = 1
        products = [1 for i in range(len(nums))]

        for i, num in enumerate(reversed(nums)):
            fwdIndex = len(nums) - i - 1
            products[fwdIndex] = trailingProd * prevNum
            trailingProd = products[fwdIndex]
            prevNum = num
            products[fwdIndex] = forwardProds[fwdIndex] * products[fwdIndex]

        return products