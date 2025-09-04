<<<<<<< HEAD

def longestCommonPrefix(strs):
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]

        i =0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i+=1
=======

def longestCommonPrefix(strs):
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]

        i =0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i+=1
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
        return first[:i]