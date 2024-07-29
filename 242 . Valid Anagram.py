def is_anagram(s,t):
    if len(s)!=len(t):          # racecar and carrace(anagrams)
        return False
    
    count_s,count_t={},{}
    for i in s:
        count_s[i]=count_s.get(i,0)+1
    for j in t:
        count_t[j]=count_t.get(j,0)+1
    
    print("Is it anagram : ",count_s==count_t)
is_anagram("racecar","carrace")