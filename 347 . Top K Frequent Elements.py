from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    most_common = count.most_common(k)
    return [item[0] for item in most_common]

# Example usage
nums = [1,2,2,3,3,3]
k = 2
print(topKFrequent(nums, k))