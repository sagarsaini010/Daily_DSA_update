<<<<<<< HEAD
def longest_sub_string(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        # remove character from set untile dupplicate remove
        # remove only duplicate that is found or even all character that is before dupplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        # add every uniqu character in set
        char_set.add(s[right])
        # track the maximum length of set
        max_len = max(max_len,right - left+1)
    return max_len
=======
def longest_sub_string(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        # remove character from set untile dupplicate remove
        # remove only duplicate that is found or even all character that is before dupplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        # add every uniqu character in set
        char_set.add(s[right])
        # track the maximum length of set
        max_len = max(max_len,right - left+1)
    return max_len
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
