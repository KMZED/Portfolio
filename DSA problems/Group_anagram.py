from collections import defaultdict
str = ["eat", "tea", "tan", "ate", "nat", "bat"]  
def groupAnagrams(str): 
   anagrams = defaultdict(list)

   for word in str:
      key = [0] * 26
      for char in word:
         key[ord(char) - ord('a')] += 1
      anagrams[tuple(key)].append(word)

   return list(anagrams.values())

print(groupAnagrams(str))