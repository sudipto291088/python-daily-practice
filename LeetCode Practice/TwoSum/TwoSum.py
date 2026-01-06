def TwoS(nums,target):
    seen = {}
    for i in range(len(nums)):
        diff = target-nums[i]

        if diff in seen:
            return [seen[diff],i]

        else:
            seen[nums[i]]=i


TwoS([2,5,3,8,12,4,14],18)