
def characterReplacement(s,k):
    left = 0
    counts = {}
    max_freq = 0
    mx = 0

    for right in range(len(s)):
        char = s[right]
        counts[char] = counts.get(char, 0) + 1
        max_freq = max(max_freq, counts[char])

        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1

        mx = max(mx, right - left + 1)

    return mx
