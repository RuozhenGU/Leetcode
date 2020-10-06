class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            if lower < upper:
                return ["%d->%d" % (lower, upper)]
            else:
                return ["%d" % lower]

        ans = []

        # handle first
        first_item = nums[0]
        if first_item - 1 == lower:
            ans.append("%d" % lower)
        elif first_item - lower > 1:
            ans.append("%d->%d" % (lower, first_item - 1))

        for idx, item in enumerate(nums[0:-1]):

            next_item = nums[idx + 1]
            if next_item - item == 1:
                continue
            elif next_item - 1 - item == 1:
                ans.append("%d" % (next_item - 1))
            else:
                ans.append("%d->%d" % (item + 1, next_item - 1))

        last_item = nums[-1]
        if upper - last_item == 1:
            ans.append("%d" % (upper))
        elif upper - last_item > 1:
            ans.append("%d->%d" % (last_item + 1, upper))

        return ans
