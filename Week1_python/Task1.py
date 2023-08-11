#!/usr/bin/python3
def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count +=1

  return count

print(list_count_4([1, 4, 4, 4, 4]))
print(list_count_4([1, 2, 2, 4, 4, 4]))