class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)

        dicc = {} # contains all of the numbers and how many times they appear

        for i in range(len(nums)): # add each category to list to dict: 1:1 2:2 3:3 in the ex
            #if dicc[nums[i]] == dicc[nums[i+1]]: doesnt work bc there might not be a key value to look at
            if nums[i] in dicc:
                dicc[nums[i]] += 1
            else:
                dicc[nums[i]] = 1
        
        sortedDicc = dict(sorted(dicc.items(), key=lambda item: item[1], reverse=True)) #sorts dicc highest first
        final = []
        for i in range(k):
            num = next(iter(sortedDicc))
            final.append(num)
            sortedDicc.pop(num)
        return final



        