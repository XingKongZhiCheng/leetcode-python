import collections
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        d = collections.defaultdict(set)
        for i, num in enumerate(nums):
                d[num].add(i)

        # 可能的差值
        for e1 in d.keys():
            for e2 in d.keys():
                if e1 == e2 and t == 0 and len(d[e1]) > 1:
                    for k1 in d[e1]:
                        for k2 in d[e1]:
                            if abs(k1-k2) == k:
                                return True
                elif e1 != e2 and abs(e1-e2) == t:
                    for k1 in d[e1]:
                        for k2 in d[e2]:
                            if abs(k1-k2) == k:
                                return True
                else:
                    pass
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = nums = nums = [1, 5, 9, 1, 5, 9]
    print(sol.containsNearbyAlmostDuplicate(nums, 2, 3))



