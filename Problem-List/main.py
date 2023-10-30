class Solution(object): 
    def twoSum(self, nums, target): 
        """ 
        :type nums: List[int]
        :type target: int
        :rtype: List[int] 
        """
        # Initialize an empty list to store the indices of the two numbers.
        indexes = []

        # Iterate through the 'nums' list.
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the sum of the current pair of numbers equals the target.
                if nums[i] + nums[j] == target:
                    # If a valid pair is found, add their indices to the 'indexes' list.
                    indexes.append(i)
                    indexes.append(j)
        
        # Return the list of indices representing the two numbers that add up to the target.
        return indexes

# Create an instance of the Solution class.
solution = Solution()

# Call the 'twoSum' method with 'nums' and 'target' parameters.
result = solution.twoSum(nums, target)

# Print the result, which is a list of indices of the two numbers.
print(result)
