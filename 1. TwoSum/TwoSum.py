class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of the numbers
        PrevMap={} #value :index

        for i, n in enumerate(nums):
            diff= target-n
            # Check if the complement of the current number exists in the dictionary
            if diff in PrevMap:
                # Return the index of the current number and the index of its complement
                return [PrevMap[diff],i]
            # Add the current number and its index to the dictionary
            PrevMap[n]=i
        #return




"""
Thought Process:

Initialize a dictionary: This will keep track of the numbers we've encountered so far and their indices. The key is the number, and the value is its index.

Iterate through the array: Go through each number in the nums array one by one.

Calculate the complement: For each number, calculate its complement by subtracting the current number from the target. The complement is the number we need to find in the array to pair with the current number to reach the target.

Check for the complement: Look in the dictionary to see if the complement already exists. If it does, it means we have found two numbers that add up to the target. We then immediately return their indices.

If the current number is nums[i], and its complement is target - nums[i], check if this complement is a key in the dictionary.
If the complement is found, that means we have previously encountered it, and nums[i] + (target - nums[i]) = target. Therefore, we return the index of the current number i and the index of the complement, which we retrieve from the dictionary.
Store the number and its index: If the complement is not found, store the current number and its index in the dictionary and proceed to the next element in the array.

Repeat until a solution is found: The process continues until a pair of numbers whose sum is equal to the target is found.

This approach guarantees that each element is added to the dictionary and checked for a possible match in a single pass through the array, making it highly efficient with a time complexity of O(n), where n is the number of elements in nums.

"""