class Solution:
    def frequencySort(self, s: str) -> str:
        ch_dict={}
        ss = ""
        for ch in set(s):
            ch_dict[ch] = s.count(ch)
        for key, value in sorted(ch_dict.items(), key=lambda item: item[1], reverse=True):
            ss=ss+(key*value)
        return ss
