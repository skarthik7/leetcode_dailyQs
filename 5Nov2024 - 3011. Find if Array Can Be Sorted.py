class Solution:
    #uts
    def countSetBits(self, nums) -> list:
        set_bit_list = []
        for num in nums:
            set_bit_list.append(bin(num).count('1'))
        return set_bit_list

    def checkSorted(self, nums) -> bool:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True

    def canSortArray(self, nums: List[int]) -> bool:
        l = len(nums)
        last_pointer = 0
        bit_count_list = self.countSetBits(nums)

        for i in range(l-1):
            if bit_count_list[i] != bit_count_list[i+1]:
                start, end = last_pointer, i
                nums[start:end+1] = sorted(nums[start:end+1])
                last_pointer = i + 1

        start, end = last_pointer, l - 1 # to sort the last chunk
        nums[start:end+1] = sorted(nums[start:end+1])

        return self.checkSorted(nums)
# O(n) time and space complexity