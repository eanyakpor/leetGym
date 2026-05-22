def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    need = {}
    for ch in s1:
        need[ch] = need.get(ch, 0) + 1

    window = {}
    left = 0

    for right in range(len(s2)):
        ch = s2[right]
        window[ch] = window.get(ch, 0) + 1

        # keep window size same as s1
        if right - left + 1 > len(s1):
            left_ch = s2[left]
            window[left_ch] -= 1

            if window[left_ch] == 0:
                del window[left_ch]

            left += 1

        if window == need:
            return True

    return False
