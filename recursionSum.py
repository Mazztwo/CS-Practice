

# Write a Python program to calculate the sum of a list of numbers.




def sumRec(nums, sum, curr):

    if(curr < len(nums)-1):
        sum = nums[curr] + sumRec(nums, sum, curr+1)

    else:
        sum = nums[curr]

    return sum







n = [2,4,5,6,7,6,2]

print(sumRec(n, 0, 0))