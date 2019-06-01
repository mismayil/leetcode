def longestsubstr(s: str) -> int:
    longest = 0
    i = j = 0

    for ch in s:
        if ch in s[i:j]:
            longest = max(j-i, longest)
            i = s[i:j].find(ch) + 1 + i

        j += 1

    return max(j-i, longest)
