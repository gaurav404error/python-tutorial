nums = [1,2,3,4]
new = [3,4,5,6]

# merge two list without using extra space. 
# [1,2,3,3,4,4,5,6]

for i in range(len(new)):
    if new[i] in nums:
        idx = nums.index(new[i])
        nums.insert(idx, new[i])
    else:
        nums.append(new[i])

print(nums)
# 3 -> 2 | nums.insert(2, 3) => [1,2,3,3,4]
# 4 -> 3 | nums.insert(3, 4) => [1,2,3,3,4,4]
# [1,2,3,3,4,4,5]
# [1,2,3,3,4,4,5,6]