from collections import deque
def priority(x):
    if x in '^':
        return 3
    elif x in '*/':
        return 2
    elif x in '+-':
        return 1
    else:
        return -1

def infix_to_postfix(s):
    st = deque()
    ans =""
    for ch in s:
        if (ch>='A' and ch <='Z') or (ch >= 'a' and ch<='z') or (ch >= '0' and ch <='9'):
            ans = ans+ch
        elif ch in '({[':
            st.append(ch)
        elif ch in ')}]':
            while st[-1] not in '({[':
                ans = ans+st.pop()
            st.pop()
        else:
            while st and priority(ch) <= priority(st[-1]):
                ans = ans+st.pop()
            st.append(ch)
    while len(st) != 0:
        ans = ans+st.pop()
    return ans

s= 'a+b^6*5/4*(2*3+4)'

print(infix_to_postfix(s)) #a b 6 ^ 5 * 4 / 2 3 * 4 + * +
        
