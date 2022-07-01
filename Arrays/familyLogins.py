from re import L


def is_familylogin(str_a,str_b):
    if str_a[0]=='z':
        base = str_a
        new = str_b
    elif str_a[0]>str_b[0]:
        base = str_b
        new = str_a
    else:
        base = str_a
        new = str_b
    for idx in range(len(base)):

        if base[idx]=='z':
           if new[idx]!='a':
            return 0
        elif chr(ord(base[idx])+1) != new[idx]:
            return 0
    return 1

def FamilyLogins(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            print(arr[i],arr[j],is_familylogin(arr[i],arr[j]))
            count += is_familylogin(arr[i],arr[j])
    return count

if __name__=='__main__':
    #arr = ['phykin','yltail','gxgpua','yltail','gxgpua','xkszhk','gxgpua','xkszhk','yltail','hyhqvb']
    #arr = ['yltail','xkszhk']
    arr= ['ab','bc','zz','aa','bb','cc','cc','cc','aa']
    x = FamilyLogins(arr)
    print("count: ",x)