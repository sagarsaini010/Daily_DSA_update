def reverseWords(s):
        words = (s.strip()).split()
        words = words[::-1]
        revers_s = ' '.join(words)
        return revers_s
        