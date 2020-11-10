count = int(input())
nums = list(map(int, input().split()))
nums.sort()
if len(nums) < 4:
    print(nums[0] * nums[1] * nums[2])
else:
    if nums[0] < 0 and nums[1] < 0:
        r1 = nums[0] * nums[1] * nums[len(nums) - 1]
    else:
        r1 = nums[-1] * nums[-2] * nums[-3]

print(r1)