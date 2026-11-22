class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        officialDict = {}
        for i in range(len(nums)):
            if nums[i] in officialDict: #if the key exists
                officialDict[nums[i]] += 1
                return True
            else: #if it doesnt exist
                officialDict[nums[i]] = 1 #create a new place in the dict for it
        return False