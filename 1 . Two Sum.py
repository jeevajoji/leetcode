# Bruteforce
def twosum(nums,target):
    for i in range(len(nums)):
       for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                ind=[i,j]
                return ind
ind=twosum([3,4,5,6],7)
print(ind)

# Hashmap shit but efficient
def two_sum(nums,target):
    ind={}
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in ind:
            return [ind[diff],i]
        ind[nums[i]]=i
    return[]
var=two_sum([3,4,5,6],7)
print(var)
