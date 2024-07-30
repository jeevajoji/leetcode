def groupAnagrams(strs):
    anagrams = {}
    
    for s in strs:
        key = tuple(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    
    return list(anagrams.values())

# Example usage
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))