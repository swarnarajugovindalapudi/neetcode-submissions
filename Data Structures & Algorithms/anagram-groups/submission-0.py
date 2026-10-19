import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Initialize a Hash Map. If we try to access a key that doesn't exist, 
        # it instantly creates an empty list [] for us.
        res = collections.defaultdict(list) 
        
        # Loop through every string in the input array exactly once
        for s in strs:
            
            # Action: Sort the string. 
            # Note: sorted(s) returns a list of characters: ['a', 'e', 't'].
            # Action: "".join() stitches the list back into a single string: "aet".
            # This string "aet" is immutable, making it a perfect dictionary key.
            sorted_s = "".join(sorted(s)) 
            
            # Decision: Go to the "aet" key in our dictionary, and append the ORIGINAL string 's' to its list.
            res[sorted_s].append(s) 
            
        # .values() extracts just the lists of grouped strings, ignoring the sorted keys.
        return list(res.values())