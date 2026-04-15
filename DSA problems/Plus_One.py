# LeetCode 66 - Plus One
digits = [1, 2, 3]

def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # carry over
    return [1] + digits

result = plusOne(digits)
print(result)
