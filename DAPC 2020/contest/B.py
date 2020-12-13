# Wrong answer
def palyndrom(n, mem={}):
    if n in mem:
        return mem[n]
    if n < 10:
        if n == 0:
            return []
        return [n]
    s = str(n)
    l2 = int(len(s)/2)
    imp = len(s)%2
    pals = []
    # if len(s) > 1 and set(s[1:]) == {'0'}:
    #     f = int(s[0]) - 1
    #     if f > 0:
    #         sn = str(f) + '9'*(len(s)-2) + str(f)
    #     else:
    #         sn = '9'*(len(s)-1)
    #     pal = int(sn)
    #     pals.append(pal)
    #     reste = n - pal
    #     pals.extend(palyndrom(reste, mem))
            
    if s[l2-1] < s[l2+imp]:
        s_pal = s[:l2] + (s[l2] if imp else '') + s[l2-1::-1]
        pal = int(s_pal)
        pals.append(pal)
        reste = n - pal
        pals.extend(palyndrom(reste, mem))
    else:
        s_pal = list(s[:l2] + (s[l2] if imp else '') + s[l2-1::-1])
        if s[l2] == '0':
            pals.append(1)
            pals.extend(palyndrom(n-1, mem))
        else:
            s_pal[l2-1] = s[l2]
            s_pal = ''.join(s_pal)
            pal = int(s_pal)
            pals.append(pal)
            reste = n - pal
            pals.extend(palyndrom(reste, mem))
    mem[n] = pals
    return pals

target = int(input())

if target == 0:
    print(1, flush=True)
    print(0, flush=True)
else:
    pal = palyndrom(target)
    print(len(pal), flush=True)
    for el in pal:
        print(el, flush=True)
