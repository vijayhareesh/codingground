
s = 'aaabcbdfe'
fidx = 0
sidx = 0
let = []
i=0
while i < (len(s) -2):
    fidx = i
    let.append(s[i])
    while s[i] == s[i+1] and i<(len(s) - 2):
        i = i+1
    sidx = i+1
    let.append(str(sidx - fidx))
    i=sidx
if len(let)<len(s):
    print ''.join(let)
else:
    print s
