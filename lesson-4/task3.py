def fun(txt):
    ans = ''
    arr = 'aeiuo'
    c = 0
    for i in range(len(txt)):
        ans += txt[i]
        c += 1
        if i != len(txt) - 1 and c >= 3 and txt[i] not in arr:
            arr += txt[i]
            ans += '_'
            c = 0
    return ans

txt = input()
print(fun(txt))