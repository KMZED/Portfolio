# LeetCode 344 - Reverse String
s = ["h", "e", "l", "l", "o"]

def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

reverseString(s)
print(s)
