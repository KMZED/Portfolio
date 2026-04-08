ransom = "aa"
magazine = "aab"
def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(ransom) > len(magazine):
        return False
    freq = {}
    for char in magazine:
        freq[char] = freq.get(char,0) + 1
    for char in ransom:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False
    return True
result = canConstruct(ransom, magazine)
print(result)