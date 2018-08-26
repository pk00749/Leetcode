class Solution:
    def __init__(self):
        self.unique = []

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = 0
        len_set = len(nums)
        for i in range(len_set):
            self.scan(nums[i])

        len_unique = len(self.unique)
        for i in range(len_unique):
            result += self.unique[i]

        return result

    def scan(self, set):
        for i in range(4):
            if set[i] not in self.unique:
                self.unique.append(set[i])
            else:
                continue


if __name__ == '__main__':
    set = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
    t = Solution()
    print(t.fourSum(set, 0))
x