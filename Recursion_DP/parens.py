def parens(n):
    if n==1:
        return ['[]']
    res = []
    l = parens(n-1)
    for comb in l:
        res.append( '[' + comb + ']' )
        res.append('[]' + comb)
        if comb+'[]'!='[]'+comb: 
            res.append(comb + '[]')
    return res
    
n = 3
print(parens(n))