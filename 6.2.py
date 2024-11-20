def substring(s):

    sb=[]

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sb.append(s[i:j])

    return sorted(set(sb))

print(substring("hello"))