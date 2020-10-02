"""[summary]
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


"""
######### WRONG SOLUTION BELOW ##############################
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)

        for i, item in enumerate(strs):
            char_v_sum = 0
            for _c in item:
                char_v_sum += ord(_c) - ord('a') # wrong if defaultdict(<class 'list'>, {4: ['ac', 'd']})
            hash_map[char_v_sum].append(item)
        print(hash_map)
        return hash_map.values()

############### RIGHT ##########################################
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)
        for i, item in enumerate(strs):
            count = [0] * 26
            for _c in item:
                count[ord(_c) - ord('a')]+=1
            hash_map[tuple(count)].append(item)
        return hash_map.values()