def swap(number):
    d = list(str(number))
    results = {number}
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            s = d[:]
            s[i], s[j] = s[j], s[i]
            if s[0] != '0':
                results.add(int(''.join(s)))
    return (max(results), min(results))