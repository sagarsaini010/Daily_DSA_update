<<<<<<< HEAD
def frequencySort( s):
        ch_dict={}
        ss = ""
        for ch in set(s):
            ch_dict[ch] = s.count(ch)
        # for key, value in sorted(ch_dict.items(), key=lambda item: item[1], reverse=True):
        #     ss+(key*value)
        for key, value in sorted(ch_dict.items(), key=lambda item: item[1], reverse=True):
            ss = ss+(key*value)

        return ss


s = "aaaqqwwssddxcfrcseedds"
print(frequencySort(s))
=======
def frequencySort( s):
        ch_dict={}
        ss = ""
        for ch in set(s):
            ch_dict[ch] = s.count(ch)
        # for key, value in sorted(ch_dict.items(), key=lambda item: item[1], reverse=True):
        #     ss+(key*value)
        for key, value in sorted(ch_dict.items(), key=lambda item: item[1], reverse=True):
            ss = ss+(key*value)

        return ss


s = "aaaqqwwssddxcfrcseedds"
print(frequencySort(s))
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
