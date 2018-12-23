from datetime import datetime

class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        count = 0
        if length < 2:
            return 0
        # # # time limit
        # for i in range(length-1):
        #     sub_nums = nums[i+1:]
        #     sub_min = min(sub_nums)
        #     while sub_nums and nums[i] > 2 * sub_min:
        #         count += 1
        #         del sub_nums[sub_nums.index(sub_min)]
        #         if sub_nums:
        #             sub_min = min(sub_nums)
        #         else:
        #             break

        # # # time limit
        # for i in range(length - 1):
        #     for j in range(i+1, length):
        #         if nums[i] > 2 * nums[j]:
        #             count += 1

        # 建立一个新的列表
        sort_nums = nums[:]
        sort_nums.sort()

        for i in range(length - 1, 0, -1):
            # print('nums:', nums)
            # print('sort_nums:', sort_nums)
            del sort_nums[sort_nums.index(nums[i])]
            count += self.binary_search(sort_nums, nums[i])
        return count

    def binary_search(self, arr, e):
        low = 0
        size = len(arr)
        high = size-1
        while low <= high:
            index = (low+high)//2
            if 2 * e < arr[index]:
                # return high-index+1
                high = index-1
            elif 2 * e > arr[index]:
                low = index+1
            else:
                while index < size:
                        if index == size - 1:
                            return 0
                        if arr[index+1] > arr[index]:
                            break
                        index += 1
                return size - index - 1
        if low < 0:
            return size
        elif low > size:
            return 0
        else:
            return size-low


if __name__ == '__main__':
    start = datetime.now()
    arr1 = [2, 4, 3, 5, 4, 1]
    # arr1 = [1, 2, 1, 2, 1]
    sol = Solution()
    print(sol.reversePairs(arr1))
    end = datetime.now()
    print('cost time:', end-start)