# LeetCode 20 - Valid Parentheses
s = "()[]{}"

def isValid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
        else:
            stack.append(c)
    return not stack

result = isValid(s)
print(result)
