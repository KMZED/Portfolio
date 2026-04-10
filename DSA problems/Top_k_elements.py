A = [1,1,1,2,2,3]
k = 2

def top_k_frequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n,c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) -1, 0 ,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

print(top_k_frequent(A, k))        