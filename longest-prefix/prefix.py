def longest_prefix(strs):
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for word in strs[1:]:
            if i >= len(word) or char != word[i]:
                return strs[0][:i]
    return strs[0]

print(longest_prefix(["dog","racecar","car"]))