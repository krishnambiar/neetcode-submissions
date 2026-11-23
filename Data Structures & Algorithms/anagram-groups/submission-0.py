
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicc = {} # contains every word and its sorted letters

        for word in strs: # loop through words to add letters to each
            dicc[word] = sorted(list(word))

        sortedWords = sorted(strs, key=lambda word: dicc[word])

        final = []
        intermediary = [] #used to chunk the list

        for i in range(len(sortedWords)):
            intermediary.append(sortedWords[i])
            # if its the last word in the list or the next word isnt the same (meaning we need a new list)
            if i == len(sortedWords) - 1 or dicc[sortedWords[i]] != dicc[sortedWords[i+1]]:
                final.append(intermediary)
                intermediary = []

        return final